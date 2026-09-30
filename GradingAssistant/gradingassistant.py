print("Hello, I am your personal Grading Assistant.")
submission = input("Did you turn the final project in? ").strip().lower()
if submission == "no":
    print("You have an incomplete grade because you have not turned the final project in. You have failed the class.")
elif submission == "yes":
    try:
        grade = float(input("What was your grade in the class? "))
    except ValueError:
        print("Please enter your grade as a number.")
    else:
        if grade >= 59:
            print("You have passed the class!")
        else:
            print("You have failed the class.")
            retake = input("Would you like to retake the class? ").strip().lower()
            if retake == "yes":
                print("You must talk to your academic advisor to reschedule the class")
            else:
                print("You failed.")
else:
    print("Please answer yes or no.")
