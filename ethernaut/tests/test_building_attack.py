import brownie


def deploy_elevator():
    return brownie.Elevator.deploy({"from": brownie.accounts[0]})


def test_attack():
    # Deploy Reentrance contract
    elevator = deploy_elevator()
    assert elevator.top() is False

    # Deploy Building Attacker contract
    building_attacker = brownie.BuildingAttacker.deploy(
        elevator.address, {"from": brownie.accounts[1]}
    )

    building_attacker.goTo()

    assert elevator.top() is True
