# Elevator_algorithm 
(The way to run the program is below an explanation of the algorithm)
EX1 – Elevator offline algorithem
Ariel Zidon: 314789264
Afik damri: 208494989

Article 1:
How do smart elevators work?
what are the benefits of this elevators 
 https://riseaboveelevator.com/2020/07/20/smart-elevators-the-next-big-trend/

Article 2:
Which algorithem is work better today: 
https://www.youtube.com/watch?v=xOayymoIl8U

Article 3:
The problem space of waiting times and short waiting times at the expense of too much investment of energy:
https://www.smart-industry.net/smart-elevators-giving-iot-a-lift/




offline Algorithm:
This algorithm works in such a way that each elevator has an ascent list and a descent list so that from any pre-known reading we will embed the elevator with the shortest time to arrive considering the data of all the elevators in the requested building.
We will try to keep an elevator that goes up with appropriate readings going up until it stops on the top floor of the ascent list and then starts going down in the same way.
Each elevator has a calculation of the time it will take it to reach the next call based on the data it has (speed, opening and closing doors ..)


# How to run the program:
- Download all project files
- Select a building in MyAlgo in the cmd function on line 50 to run the Calls file you want on it.
- Then a line below the building selection must select some call so in line 51 we will select the call we want.

For example:

![select building and call](https://user-images.githubusercontent.com/93542763/142505979-1b5c0a69-577b-4331-93e5-0a26d37c7e89.png)

- We will now run the cmd function in main.

![main run](https://user-images.githubusercontent.com/93542763/142506698-24093daf-cc8c-4202-8bcf-e94753e5ad97.png)

- We will now open the terminal and write the following line:

java -jar Ex1_checker_V1.2_obf.jar 1111,2222 (*Building you want.json*).json output.csv out.log

For example:

![terminal](https://user-images.githubusercontent.com/93542763/142507477-93e99f95-7a35-45d9-a754-0fa1abdb383c.png)

-After running the line in the terminal we can see the average time a person waited for an elevator and the number of people who did not receive service.

Enjoy!









