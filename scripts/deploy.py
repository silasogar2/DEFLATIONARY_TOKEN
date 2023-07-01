import os
from brownie import ShowToken, accounts
from eth_account import Account


def main():
    account_name = ''
    acct = accounts.load(account_name)
    token_contract = ShowToken.deploy(
        "0x9Ac64Cc6e4415144C455BD8E4837Fea55603e5c3",
        10,
        "2100000000000000000000000000",
        {"from": acct},
        publish_source=True,
    )
    return token_contract

