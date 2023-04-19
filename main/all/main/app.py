from oneinch_py import OneInchSwap, TransactionHelper, OneInchOracle
import json, csv, random, wget
import time, sys, requests
from web3 import Web3
from os import system
import boto3
from intial_setup import setup_rpc_url, Exiting
from aws_utils import check_message
from portfolio_utils import read_portfolio_file

# pip install -r main/requirements.txt
# pip install python-lambda-local
# export PATH=$PATH:/Users/user/Library/Python/3.9/bin # On Mac
# python-lambda-local -f lambda_handler main/app.py secret.json -t 6000

def lambda_handler(event, context):
    
    print ("event ==>", event)
    print ("event type: ", type(event))
    if 'body' in event:
        print (type(event))
        # event = json.dumps(json.loads(event['body']),indent=4)
        event = json.loads(event['body'])
        print (type(event))
        print ("Body did exist")
    else:
        event = event
        print ("Body did not exist")
    print ("event ==>", event)
    print ("event type: ", type(event))
 
    if (event.get('local_execution', False)):
        print("This is a local execution. 🖥🖥️🖥️️🖥️️")
    if (event.get('cloud_execution', False)):
        print("This is an AWS Function URL execution. ⛅⛅⛅⛅")
    
    # If the message is not correct, then exit
    message = event['message']
    chain = event['chain']
    if not check_message(message):
        Exiting(443)
    rpc_url = setup_rpc_url(chain)
    print ("chain ==>", event['chain'])
    print ("rpc_url ==>", rpc_url)

    URL = event['portfolio']
    portfolio, header, rows = read_portfolio_file(URL)
    print ("portfolio ==>", portfolio)
    print ("header ==>", header)
    print ("rows ==>", rows)


    total_investment_amount = float(event['total_investment_amount'])
    print ("total_investment_amount ==>", total_investment_amount)
    public_key = event['public_key']
    print ("public_key ==>", public_key)
    private_key = event['private_key']
    # print (private_key)
    destReceiver = event['destReceiver']
    print ("destReceiver ==>", destReceiver)
    file = open(portfolio)

    exchange = OneInchSwap(public_key, chain=chain) # initialise the OneInchSwap object as "exchange"
    helper = TransactionHelper(rpc_url, public_key, private_key, chain=chain) # initialise the TransactionHelper object as "helper"
    # oracle = OneInchOracle(rpc_url, chain=chain) # initialise the OneInchOracle object as "oracle"

    if event['investment_token'] != "USDC":
        investment_token = event['investment_token']
    else:
        investment_token = "USDC"
    # investment_token = "DAI"

    
    tokens = exchange.get_tokens()
    print ("Token: ", tokens[investment_token]['symbol'], "Address: ", tokens[investment_token]['address'], "Decimals: ", tokens[investment_token]['decimals'])
    result = helper.get_ERC20_balance(exchange._token_to_address(investment_token), decimal=tokens[investment_token]['decimals'])
    print ("Token: ", tokens[investment_token])
    print ("result ==>", result)

    print ("")
    if result == 0:
        print ("You don't have any tokens to swap.")
        exit ()
    else:
        print ("\n","Token: ", investment_token, "Balance: ", result, "\n")
    # Compare the balance of the investment token with the total investment amount
    if result < total_investment_amount:
        print ("You don't have enough tokens to swap.")
        print ("\U0001F622 \n\U0001F622")
        exit ()
    

    # TODO: Check if the investment token is approved for spending by the smart contract in function
    approveal_tx = exchange.get_approve (from_token_symbol=investment_token)
    built = helper.build_tx(approveal_tx, 'high') # prepare the transaction for signing, gas price defaults to fast.
    signed = helper.sign_tx(built) # sign the transaction using your private key
    approval_result = helper.broadcast_tx(signed) #broadcast the transaction to the network and wait for the receipt.
    print ("approval_result ==>", approval_result)
    row_count = sum(1 for row in file) - 1
    print("Total coins (Portfolio Size): ",row_count)
    print("Total Investment Ammount: ",total_investment_amount)
    investment_amount = total_investment_amount / row_count
    print("Investment Ammount per coin: ", investment_amount)
    print("Investment Ammount per coin calculated as: Total investment amount / Portfolio size")
    file.close()
    print ("investment_amount ==>", investment_amount)

    file = open(portfolio)
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    rows = []
    i = 0
    print("Buying coins started ...")
    print("Please wait ...")
    # print ("Exiting ...")
    # exit ()
    for row in csvreader:
        print("\n\n")
        print("\n",i+1, " ==> ", row[0]) 
        # buy_token = row[0]
        # TODO: need to check address base buy 
        # example: Kyber Network Crystal v2 (PoS) (KNC)
        # 0x1534fB3E82849314360C267FE20Df3901A2ED3f9
        # if len(buy_token) != 42:
            # print ("This Token address, you please validate yourself: ", len(buy_token), buy_token)
            # result = helper.get_ERC20_balance(exchange._token_to_address(buy_token), decimal=tokens[buy_token]['decimals'])
            # print("Token: ", tokens[buy_token]['symbol'], "Balance: ", result, "Name: ", tokens[buy_token]['name'],  "Address: ", tokens[buy_token]['address'], "Decimals: ", tokens[buy_token]['decimals'])
        # token = row[0]
        # investment_token = "WXDAI"
        # rate = oracle.get_rate(src_token=exchange._token_to_address(token), dst_token=exchange._token_to_address(investment_token), src_token_decimal=18, dst_token_decimal=18)
        # print ("1 ", token,"= ", rate, investment_token)
        swap_tx = exchange.get_swap(investment_token, row[0], investment_amount, 1, destReceiver=destReceiver) # get the swap transaction
        # result = helper.build_tx(swap_tx,'low') # prepare the transaction for signing, gas price defaults to fast.
        result = helper.build_tx(swap_tx,'high') # prepare the transaction for signing, gas price defaults to fast.
        # print("\n\n")
        # print ("swap_tx:", swap_tx)
        # print ("swap_tx.keys ==>", swap_tx.keys())
        # print (type(swap_tx))
        # print("\n\n")
        # print ("result:", result)
        # print (type(result))
        # print("\n\n")
        result = helper.sign_tx(result) # sign the transaction using your private key
        swap_result = helper.broadcast_tx(result) #broadcast the transaction to the network and wait for the receipt. 
        # print("\n\n")
        # print (type(swap_result))
        # print("swap_result:", swap_result)
        # print("\n\n")
        # web3.eth.waitForTransactionReceipt(swap_result)
        # print ("result.keys ==>", result.keys())
        # print("\n\n")
        # print ("swap_result.keys ==>", swap_result.keys())
        # print("\n\n")
        # print (swap_result['transactionHash'])

        rows.append(row)
        i = i + 1
        print(i, " of ", row_count, " coins bought", row[0], " worth $", investment_amount,"successful ✅ \n\n")
        time.sleep (5)
        # sleep for 5 seconds to avoid rate limit
        time.sleep (5)

    print("All coins bought")
    print(rows)
    print("\n\n")
    # print("Check Recever: https://optimistic.etherscan.io/address/"+destReceiver+"#tokentxns")
    print("Check Sender: https://gnosisscan.io/address/"+public_key)
    file.close()
    return {
        "isBase64Encoded": "false",
        "statusCode": 200,
        "body": '{"message": "successful"}',
        # "body": final_body,
        "headers": {
            "content-type": "application/json"
        }
    }