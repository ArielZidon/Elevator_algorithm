# Elevator_algorithm
EX1 – Elevator offline algorithem
Ariel Zidon: 314789264
Afik damri: 208494989

Article 1:
How do smart elevators work? + what are the benefits of this elevators 
 https://riseaboveelevator.com/2020/07/20/smart-elevators-the-next-big-trend/

Article 2:
Which algorithem is work better today: 
https://www.youtube.com/watch?v=xOayymoIl8U

Article 3:
The problem space of waiting times and short waiting times at the expense of too much investment of energy
https://www.smart-industry.net/smart-elevators-giving-iot-a-lift/





offline Algorithm:
This algorithm works in such a way that each elevator has an ascent list and a descent list so that from any pre-known reading we will embed the elevator with the shortest time to arrive considering the data of all the elevators in the requested building.
We will try to keep an elevator that goes up with appropriate readings going up until it stops on the top floor of the ascent list and then starts going down in the same way.
Each elevator has a calculation of the time it will take it to reach the next call based on the data it has (speed, opening and closing doors ..)
