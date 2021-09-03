while(True):
    try:
        int(input("Enter a number: "))
    except ValueError:
        print("That's not a number! Try again..")
    else:
        break