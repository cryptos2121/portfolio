# main.py

from oneinch_py import OneInchSwap, TransactionHelper
import json
from decouple import config
from intial_setup import Check_Allowance

# pip install python-decouple 1inch.py==1.8.2 requests==2.28.1 web3<6.0


# #  (investment_token, amount, exchange, helper)
# def ApproveToken (token, amount, exchange, helper):
#   print ("Approving token: ", token)
#   print ("Amount: ", amount)
#   approve_tx = exchange.get_approve(token, amount) # get approval transaction
#   built = helper.build_tx(approve_tx) # prepare the transaction for signing, gas price defaults to fast.
#   signed = helper.sign_tx(built) # sign the transaction using your private key
#   approval_result = helper.broadcast_tx(signed) #broadcast the transaction to the network and wait for the receipt. 



def main():
    investment_token = "USDC"
    token = "DAI"
    amount = 10000000
    chain = 'gnosis'
    public_key = config('public_key')
    private_key = config('private_key')
    rpc_url = "https://gnosischain-rpc.gateway.pokt.network"
    exchange = OneInchSwap(public_key, chain=chain) # initialise the OneInchSwap object as "exchange"
    helper = TransactionHelper(rpc_url, public_key, private_key, chain=chain) # initialise the TransactionHelper object as "helper"

    Check_Allowance (investment_token, amount, exchange, helper, public_key)


    exit ()

    swap_tx = exchange.get_swap(investment_token, token, 0.001, 0.5) # get the swap transaction
    result = helper.build_tx(swap_tx) # prepare the transaction for signing, gas price defaults to fast.
    result = helper.sign_tx(result) # sign the transaction using your private key
    swap_result = helper.broadcast_tx(result) #broadcast the transaction to the network and wait for the receipt. 


    # print(swap_result)

if __name__ == "__main__":
    main()