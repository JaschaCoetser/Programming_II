"""
Do From Scratch
"""

import random

numbers_per_line = 6
minimum = 1
maximum = 45


def main():
    number_of_quick_picks = int(input("How many Quick Picks? "))
    while number_of_quick_picks < 0:
        print("Invalid number")
        number_of_quick_picks = int(input("How many Quick Picks? "))

    for i in range(number_of_quick_picks):
        quick_picks = []
        for j in range(numbers_per_line):
            number = random.randint(minimum, maximum)
            while number in quick_picks:
                number = random.randint(minimum, maximum)
            quick_picks.append(number)
        quick_picks.sort()

    print(" ".join("{:2}".format(number) for number in quick_picks))


main()