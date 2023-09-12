import car
import random

def main():
    firstcar = car.Car("bmw", "red", random.randint(120,200), random.randint(1,10))
    secondcar = car.Car("mercedes", "blue",random.randint(120,200), random.randint(1,10))
    thirdcar = car.Car("volvo", "black", random.randint(120,200), random.randint(1,10))

    print("Display 1st car information: ")
    display(firstcar)
    print()
    print("Display 2nd car information: ")
    display(secondcar)
    print()
    print("Display 3rd car information: ")
    display(thirdcar)
    
    print("\n")
    print("\n")
    print("\n")

    print("Race Begins\n\n\n")

    for i in range(10):
        if firstcar.get_maxspeed() > firstcar.get_currentspeed() + firstcar.get_accelaration_rate() :
            firstcar.increase_speed()
        if secondcar.get_maxspeed() > secondcar.get_currentspeed() + secondcar.get_accelaration_rate() :
            secondcar.increase_speed()
        if thirdcar.get_maxspeed() > thirdcar.get_currentspeed() + thirdcar.get_accelaration_rate() :
            thirdcar.increase_speed()
        firstcar.increase_mile()
        secondcar.increase_mile()
        thirdcar.increase_mile()
    
    print("Race Ends and Final Values of Cars\n")
    print("Display 1st car information: ")
    display(firstcar)
    print()
    print("Display 2nd car information: ")
    display(secondcar)
    print()
    print("Display 3rd car information: ")
    display(thirdcar)

    if firstcar.get_mile() > secondcar.get_mile() and firstcar.get_mile() > thirdcar.get_mile() :
        print("\n\n Winner prize goes to  ", firstcar.get_color(), " ", firstcar.get_brand())

    if secondcar.get_mile() > firstcar.get_mile() and secondcar.get_mile() > thirdcar.get_mile() :
        print("\n\n Winner prize goes to  ", secondcar.get_color(), " ", secondcar.get_brand())

    if thirdcar.get_mile() > secondcar.get_mile() and thirdcar.get_mile() > firstcar.get_mile() :
        print("\n\n Winner prize goes to  ", thirdcar.get_color(), " ", thirdcar.get_brand())
        
    

def display(car):
    print('Brand: ', car.get_brand())
    print('Color: ', car.get_color())
    print('Max Speed: ', car.get_maxspeed())
    print('Accelaration Rate: ', car.get_accelaration_rate())
    print('Current Speed:', car.get_currentspeed())
    print('Currenct mile:', car.get_mile())



main()