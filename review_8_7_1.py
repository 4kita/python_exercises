while True:

    try:
        someNum = int(input("Enter a number: "))
        someString = input("Enter a string: ")
        print(someString[someNum])
        break

    except(ValueError):
        print("You didn't enter a number!")
    except(IndexError):
        print("Your integer was too large for the string!")


