"""
UnreliableCar class tests
"""

from Prac_08.unreliable_car import UnreliableCar


def main():
    """Test some UnreliableCars."""

    good_car = UnreliableCar("Good Car", 100, 90)
    bad_car = UnreliableCar("Not a good Car", 100, 9)

    for i in range(1, 12):
        print("Attempting to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(good_car.name, good_car.drive(i)))
        print("{:12} drove {:2}km".format(bad_car.name, bad_car.drive(i)))

    print(good_car)
    print(bad_car)


main()

