from PriorityQueue import PriorityQueueup
from PriorityQueue import PriorityQueuedown



class Elevator:
    def __init__(self, d):
        self._id = int(d["_id"])
        self._speed = float(d["_speed"])
        self._minFloor = int(d["_minFloor"])
        self._maxFloor = int(d["_maxFloor"])
        self._closeTime = float(d["_closeTime"])
        self._openTime = float(d["_openTime"])
        self._startTime = float(d["_startTime"])
        self._stopTime = float(d["_stopTime"])
        self.state = 0 # location
        self.updo = 0  # 1 up , -1 down , 0 level
        self.callListup = PriorityQueueup()
        self.callListdown = PriorityQueuedown()




