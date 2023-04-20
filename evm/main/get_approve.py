from oneinch_py import OneInchSwap, TransactionHelper
import json
from decouple import config

# pip install python-decouple 1inch.py==1.8.2 requests==2.28.1 web3<6.0
investment_token = "ELK"
investment_token = "xDAI"
token = "GNO"
amount = 10000000
chain = 'gnosis'
public_key = config('public_key')
private_key = config('private_key')
rpc_url = "https://gnosischain-rpc.gateway.pokt.network"


def ApproveToken (token, amount):
  print ("Approving token: ", token)
  print ("Amount: ", amount)
  approve_tx = exchange.get_approve(token, amount) # get approval transaction
  built = helper.build_tx(approve_tx) # prepare the transaction for signing, gas price defaults to fast.
  signed = helper.sign_tx(built) # sign the transaction using your private key
  approval_result = helper.broadcast_tx(signed) #broadcast the transaction to the network and wait for the receipt. 

exchange = OneInchSwap(public_key, chain=chain) # initialise the OneInchSwap object as "exchange"
helper = TransactionHelper(rpc_url, public_key, private_key, chain=chain) # initialise the TransactionHelper object as "helper"

get_allowance = exchange.get_allowance(investment_token, public_key)
print ("Allowance: ", get_allowance)
loads = json.loads(json.dumps(get_allowance))
print ("Allowance: ", loads.get("allowance"))
print (type(loads.get("allowance")))

if loads.get("allowance") == '0':
    print ("You need to approve the token first.")
    ApproveToken (investment_token, amount)
else:
    print ("You have allowance.")

exit ()

swap_tx = exchange.get_swap(investment_token, token, 0.001, 0.5) # get the swap transaction
result = helper.build_tx(swap_tx) # prepare the transaction for signing, gas price defaults to fast.
result = helper.sign_tx(result) # sign the transaction using your private key
swap_result = helper.broadcast_tx(result) #broadcast the transaction to the network and wait for the receipt. 


# print(swap_result)