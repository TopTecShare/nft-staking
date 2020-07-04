from brownie import *
from .settings import *
from .contracts import *
from .contract_addresses import *
import time


def main():
    load_accounts()

    # User to get Genesis NFT
    user = web3.toChecksumAddress('0x66d7Dd55646100541F2B6ec15781b6d4C8372b1c')

    # Get Contracts 
    genesis_nft_address = CONTRACTS[network.show_active()]["genesis_nft"]
    genesis_nft = DigitalaxGenesisNFT.at(genesis_nft_address)

    # Mint NFTs
    genesis_nft.adminBuy(user, {'from':accounts[0]})



