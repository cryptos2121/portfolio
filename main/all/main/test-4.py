import requests
from web3 import Web3
from web3.exceptions import InvalidAddress


# Define the RPC URL for Polygon network
rpc_url = "https://polygon-rpc.com"

# Define the token contract address for KNC on Polygon network
token_address = "0x1c954e8fe737f99f68fa1ccda3e51ebdb291948c"

def get_contract_instance(address):
    try:
        # convert address to checksum address
        checksum_address = Web3.toChecksumAddress(address)
        # get contract ABI from Etherscan API
        api_url = f"https://api.polygonscan.com/api?module=contract&action=getabi&address={checksum_address}"
        response = requests.get(api_url)
        abi = response.json()
        # create contract instance
        contract = web3.eth.contract(address=checksum_address, abi=abi)
        return contract
    except InvalidAddress:
        print(f"Invalid address: {address}")
        return None

# Create a Web3 object
web3 = Web3(Web3.HTTPProvider(rpc_url))

# Get the contract instance for the given token address
token_contract = get_contract_instance(token_address)

# Call the symbol() method on the contract to get the token symbol
symbol = token_contract.functions.symbol().call()

# Print the token symbol
print(symbol)
