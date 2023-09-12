******Problem Statement: Creating a Car Management System******

You are tasked with creating a simple car management system using Python 
classes. The system should be able to create and manage car objects with 
various properties.

  

1. Create a `Car` class with the following attributes:

- `brand` (string): The brand or make of the car.

- `color` (string): The color of the car.

- `maxspeed` (integer): The maximum speed the car can achieve.

- `currentspeed` (integer): The current speed of the car (initially set to 
0).

- `acceleration_rate` (integer): The rate at which the car's speed can be 
increased.

- `mile` (float): The total mileage traveled by the car (initially set to 
0.0).

  

2. Implement the following methods in the `Car` class:

- `____init____(self, brand, color, maxspeed, acceleration_rate)`: The 
constructor to initialize the car object with the provided values.

- Getter methods for all attributes (e.g., `get_brand`, `get_color`, 
`get_maxspeed`, etc.).

- Setter methods for `brand`, `color`, `maxspeed`, `currentspeed`, and 
`acceleration_rate`.

- `increase_speed(self)`: A method to increase the current speed of the 
car by the acceleration rate.

- `increase_mile(self)`: A method to increase the total mileage of the car 
based on the current speed.

  

3. Create multiple car objects, set their properties, and perform the 
following actions:

- Increase the speed of each car object multiple times.

- Calculate and display the total mileage traveled by each car.

- Change the properties (brand, color, etc.) of some cars and display the 
updated information.

  

4. Write a Python program that demonstrates the use of the `Car` class. 
Create car objects, manipulate their properties, and display relevant 
information.

  
  **Question for Car Race Simulation:**

You are tasked with creating a Python program ( main.py ) that simulates a 
car race using the provided `car` class. The program creates three cars 
with random properties and simulates a race over a certain distance. After 
the race, it determines and announces the winner.

Write a Python program that accomplishes the following:

1. Create three cars with random properties:
   - Car 1: Brand "BMW," a random color, a random maximum speed between 
120 and 200, and a random acceleration rate between 1 and 10.
   - Car 2: Brand "Mercedes," a random color, a random maximum speed 
between 120 and 200, and a random acceleration rate between 1 and 10.
   - Car 3: Brand "Volvo," a random color, a random maximum speed between 
120 and 200, and a random acceleration rate between 1 and 10.

2. Display the initial information of each car, including brand, color, 
maximum speed, acceleration rate, current speed, and initial mileage.

3. Simulate the race as follows:
   - Each car accelerates randomly within its acceleration limit for 10 
rounds.
   - Update the current speed and mileage of each car after each round.

4. Display the final information of each car after the race.

5. Determine and announce the winner based on the car with the highest 
mileage. Display the winner's brand and color.

Your task is to implement the missing parts of the Python program to 
achieve the above-described functionality. Ensure that the program is 
well-structured and uses the provided `car` class appropriately.
