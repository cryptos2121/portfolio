from web3 import Web3

# Define the RPC URL
rpc_url = "https://gnosischain-rpc.gateway.pokt.network"

# Connect to the network using Web3
web3 = Web3(Web3.HTTPProvider(rpc_url))

# Define the hexadecimal address to convert
address = "0x1534fB3E82849314360C267FE20Df3901A2ED3f9"

# Convert the address to a checksummed version
checksum_address = web3.toChecksumAddress(address)

# Print the result
print(checksum_address)
