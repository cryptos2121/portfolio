# intial_setup.py

# https://app.infura.io/dashboard/ethereum/d162e1d2d54e4fd5b07a78b9b9176728/settings/endpoints

# https://github.com/RichardAtCT/1inch_wrapper/blob/f515f0dc807d0654edfc845b4ef265b8b6ae2d97/oneinch_py/main.py#L325
# class OneInchOracle:
#     chains = {
#         "ethereum": '1',
#         "binance": '56',
#         "polygon": "137",
#         "optimism": "10",
#         "arbitrum": "42161",
#         "gnosis": "100",
#         "avalanche": "43114",
#         "fantom": "250"
#     }

# Write a function to setup RPC URL based on the chain
def setup_rpc_url(chain):
    if chain == "polygon":
        rpc_url = "https://polygon-mainnet.infura.io/v3/d162e1d2d54e4fd5b07a78b9b9176728"
    elif chain == "bsc":
        rpc_url = "https://bsc-dataseed.binance.org/"
    elif chain == "ethereum":
        rpc_url = "https://mainnet.infura.io/v3/d162e1d2d54e4fd5b07a78b9b9176728"
    elif chain == "arbitrum":
        rpc_url = "https://arbitrum-mainnet.infura.io/v3/d162e1d2d54e4fd5b07a78b9b9176728"
    elif chain == "optimism":
        rpc_url = "https://optimism-mainnet.infura.io/v3/d162e1d2d54e4fd5b07a78b9b9176728"
    elif chain == "avalanche":
        rpc_url = "https://avalanche-mainnet.infura.io/v3/d162e1d2d54e4fd5b07a78b9b9176728"
    # https://chainlist.org/chain/250
    elif chain == "fantom":
        rpc_url = "https://fantom-mainnet.gateway.pokt.network/v1/lb/62759259ea1b320039c9e7ac"
    # https://chainlist.org/chain/100
    elif chain == "gnosis":
        rpc_url = "https://gnosischain-rpc.gateway.pokt.network"
    return rpc_url


def Exiting(statusCode):
    statusCode = statusCode
    print ("Exiting")
    return {
      "isBase64Encoded": "false",
      "statusCode": statusCode,
      "body": '{"message": "successful"}',
      # "body": final_body,
      "headers": {
          "content-type": "application/json"
      }
    }
    # logger.info('Total Errors: {}'.format("Exiting"))
    # sys.exit(0)