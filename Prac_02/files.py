def main():
    name = input("Please enter your name: ")
    with open('name.txt', 'w') as data:
        data.write(name)

    with open("name.txt", 'r') as data:
        print("Your name is:", data.read())

    with open('numbers.txt', 'r') as data:
        total = 0
        for line in data:
            total += int(line)
        print(total)


main()
