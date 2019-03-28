

def main():
    """Get a numeric score and display its status."""
    score = float(input("Enter score: "))
    print(determine_status(score))


def determine_status(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


main()

