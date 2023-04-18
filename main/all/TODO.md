# Tasks List

# TODO: Created lambda template by copying existing lambda code
# TODO: Created new Portfolio, upload on github
* Using [CoinGecko](https://www.coingecko.com/en/categories)
# TODO: Create "secret.json" with appropriate values
# TODO: Update code for new chain 
* Using [Infura Account](https://app.infura.io/dashboard/ethereum/), get RPC address.
# TODO: Add fund into given wallet and test with minimum investment amount for small portfolio.
* Using [https://chainlist.org/](https://chainlist.org/) and MetaMask or any other Web3 Wallet.
* Using MM please give permission to spend "USDC". i.e. Set a spending cap for your coin/contract.
# TODO: Add allowance support
* USDC: 0xddafbb505ad214d7b80b1f830fccc89b60fb7a83
* USDT: 0x4ecaba5870353805a9f068101a40e0f32ed605c6
* 1inch: 0x1111111254fb6c44bac0bed2854e76f90643097d
* Spender: 0x1111111254eeb25477b68fb85ed929f73a960582

# TODO: Refacor the code to break into small functions 
# TODO: Test everything on Mac without using docker 


# pip install -r main/requirements.txt
# pip install python-lambda-local
# export PATH=$PATH:/Users/user/Library/Python/3.9/bin # On Mac
# python-lambda-local -f lambda_handler main/app.py secret.json -t 6000