from web3 import Web3

# Define the RPC URL
rpc_url = "https://gnosischain-rpc.gateway.pokt.network"

# Define the token contract address
token_address = "0x1534fB3E82849314360C267FE20Df3901A2ED3f9"
token_address = "0x9C58BAcC331c9aa871AFD802DB6379a98e80CEdb"

address = token_address
# Connect to the network using Web3
web3 = Web3(Web3.HTTPProvider(rpc_url))

# Define a function to get the contract instance
def get_contract_instance(address):
    # Define the contract ABI dynamically
    abi = web3.eth.contract(address=address).abi

    # Create a contract instance using the address and ABI
    contract = web3.eth.contract(address=address, abi=abi)

    return contract

# Get the contract instance for the given token address
token_contract = get_contract_instance(token_address)

# Call the symbol() method on the contract to get the token symbol
symbol = token_contract.functions.symbol().call()

# Print the token symbol
print(symbol)
