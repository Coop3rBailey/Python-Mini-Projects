def teen_age():
    try:
        age = int(input("How old are you? "))
    except ValueError:
        print("Please enter your age as a number.")
        return
    if age<13 or age>19:
        print("You are not a teenager")
    else:
        print("You are a teenager")

teen_age()
