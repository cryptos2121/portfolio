#!/bin/bash

# List all tokens on 1inch for given blockchain
# Usage: ./list.sh
# URL: https://docs.1inch.io/docs/aggregation-protocol/api/swagger/
# Code for [chainid](https://github.com/RichardAtCT/1inch_wrapper/blob/daa2473a434a6dda4f6a2b0c8bfd4315b44024e9/oneinch_py/main.py#L21)
# List of more [chains](https://chainlist.org/)
#     chains = {
    #     "ethereum": '1',
    #     "binance": '56',
    #     "polygon": "137",
    #     "optimism": "10",
    #     "arbitrum": "42161",
    #     "gnosis": "100",
    #     "avalanche": "43114",
    #     "fantom": "250"
    # }

#export chain_id=100; curl -s https://api.1inch.io/v5.0/${chain_id}/tokens | jq '.tokens[]' | grep "symbol" | cut -d '"' -f 4 | sort

export chain_id=100; curl -s https://api.1inch.io/v5.0/${chain_id}/tokens | jq '.tokens[]' | grep "symbol" | cut -d '"' -f 4 | sort | grep -vi REALTOKEN

# List all tokens on 1inch for given blockchain and 
# List of liquidity sources that are available for routing in the 1inch Aggregation protocol

curl  https://api.1inch.io/v5.0/100/liquidity-sources 

curl -s  https://api.1inch.io/v5.0/100/presets | jq .

curl  https://api.1inch.io/v5.0/100/tokens | jq '.tokens[]' | grep "symbol" | cut -d '"' -f 4 | sort | grep -vi REALTOKEN