"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    A value error will occur when the numerator and denominator are not valid, example when the two are flipped
    such as having the larger number as the numerator.
2. When will a ZeroDivisionError occur?
    Zero division is when the denominator is zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Ensure that the denominator is not zero
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers.txt!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
