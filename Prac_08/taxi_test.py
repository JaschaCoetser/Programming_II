"""
Test Taxi
"""

from Prac_08.taxi import Taxi


def main():
    """Test the Taxi Class"""
    my_taxi = Taxi("Pruis 1", 100)
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)


main()
