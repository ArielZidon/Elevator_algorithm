import csv
import random
import MYBuilding
from MyCalls import CallForElevator
from MYBuilding import Building
from MyElevator import Elevator

count = 1
# algo:
def alo(Call, building:Building):
    global count
    counter = -1
    for i in building._elevators:
        counter+=1

        if i.callListup.isEmpty():
            if i.state<=int(Call.src) and int(Call.src)<int(Call.dest):
                i.callListup.insert(Call.src)
                i.callListup.insert(Call.dest)
                print("elevator ", i._id, " take the call")
                return i._id

        if i.callListdown.isEmpty():
            if i.state >= int(Call.src) and int(Call.src) > int(Call.dest):
                i.callListdown.insert(Call.src)
                i.callListdown.insert(Call.dest)
                print("elevator ",i._id," take the call")
                return i._id
    rand = count % len(building._elevators)
    count +=1
    print("elevator ",rand,"take the call")
    return rand


def total_time(src, dest, Elevator):
    x = abs(int(src) - int(dest))
    y = abs(int(Elevator.state) - int(src))
    dis = x + y
    total = (dis / Elevator._speed) + stop(Elevator)*(Elevator.callListup.__sizeof__()+Elevator.callListdown.__sizeof__())
    return total


def stop(Elevator):
    return (Elevator._stopTime + Elevator._startTime + Elevator._closeTime + Elevator._openTime)




def cmd():
    building = Building("B5.json")
    Calls = readCalls("Calls_d.csv")
    end = float(Calls[-1].time)
    end = int(end) + 2
    counter = 0
    for t in range(0,end):

        move(building)

        now = float(Calls[counter].time)
        try:
            while (t == int(now)):
                Calls[counter].elevator = alo(Calls[counter], building)
                writeCalls(Calls)
                counter += 1
                now = float(Calls[counter].time)
        except:
            print("finish")
            break




def move(building):
    for i in building._elevators:

        if i.callListdown.isEmpty() == False:
                if i.state <= i.callListdown.peek():
                    i.state = i.callListdown.peek()
                    i.callListdown.delete()
                    print("elevator ",i._id," going down")
                else:
                      i.state = i.state - i._speed

        if i.callListup.isEmpty() == False:
                if i.state <= i.callListup.peek():
                    i.state = i.callListup.peek()
                    i.callListup.delete()
                    print("elevator ",i._id," going up")
                else:
                    i.state = i.state + i._speed



# read and write

def readCalls(file_name):
    calls = []
    with open(file_name, "r") as fp:
        data = csv.reader(fp)
        for i in data:
            calls.append(CallForElevator(i))
    return calls


def writeCalls(calls):
    dataCalls = []
    for i in calls:
        dataCalls.append(i.__dict__.values())
    with open("output.csv", "w", newline="") as fu:
        csvwriter = csv.writer(fu)
        csvwriter.writerows(dataCalls)


#  run
if __name__ == '__main__':
    cmd()

