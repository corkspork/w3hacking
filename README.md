# web3-hacking

This project contains some contracts, scripts and tests related to web3 hacking.
Using Python and the [brownie](https://github.com/eth-brownie/brownie) framework to interact with EVM networks and contracts.

## Setup

1. Install Ganache (if you don't have it installed already)

   ```sh
   npm install ganache --global
   ```

1. Install pipenv (if you don't have it installed already)

   ```sh
   pip install --user pipenv
   ```

1. Create a `.env` file with the following 2 variables.

   ```
   WEB3_INFURA_PROJECT_ID="<infura_project_id>"
   ETH_ACCOUNT_PRIVATE_KEY="<ethereum_private_key>"
   ```

   Alternatively, export these as evironment variables.

1. Create virtualenv

   ```sh
   pipenv shell
   ```

## Run tests

All the tests do the following:

1. Deploy the Victim contract to a local chain
2. Deploy an Attacker contract (if required)
3. Attack!

This is how we run the tests:

1. Enter a directory

   ```sh
   cd ethernaut
   ```

2. Run tests

   ```sh
   brownie test
   ```

## Attack

1. Enter a directory

   ```sh
   cd ethernaut
   ```

2. Run attack

   ```sh
   brownie run vault_attack.py
   ```
