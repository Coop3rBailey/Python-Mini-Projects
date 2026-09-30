print("Hello, I am your personal Grading Assistant.")
submission = input("Did you turn the final project in?")
if submission == "no":
    print("You have an incomplete grade because you have not turned the final project in. You have failed the class.")
if submission == "yes":
    grade = float(input("What was your grade in the class?"))
    if grade >= 59:
        print("You have passed the class!")
    else:
        print("You have failed the class.")
    retake = input("Would you like to retake the class?")
    retake == "yes"
    print("You must talk to your academic advisor to reschedule the class")
    retake== "no"
    print("You failed.")
    

        
