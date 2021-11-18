import json
from MyElevator import Elevator




class Building:
    def __init__(self, file):
        with open(file, "r") as ft:
            d = json.load(ft)
            self._maxFloor = d["_maxFloor"]
            self._minFloor = d["_minFloor"]
            self._elevators = []
            for i in d["_elevators"]:
                self._elevators.append(Elevator(i))

