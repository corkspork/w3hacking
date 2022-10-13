import pytest
from brownie import accounts


@pytest.fixture()
def force(Force, accounts):
    return Force.deploy({"from": accounts[0]})


def test_attack(force, ForceAttacker):
    assert force.balance() == 0

    ForceAttacker.deploy(force.address, {"from": accounts[1], "value": 1})

    assert force.balance() > 0
