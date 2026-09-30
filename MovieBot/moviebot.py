print("Welcome to the movie theatre!") #Little intro
try:
    age = int(input("This movie is rated R. How old are you? ")) #Asks the user for age
except ValueError:
    print("Please enter your age as a number.")
else:
    if age >= 18: #Checks if age is above 18, if so lets them in
        print("Enjoy the movie!")
    else:
        parent = input("Since you are under 18 is a parent here with you? yes/no ").strip().lower()
        if parent == "yes":
            print("Enjoy the movie!")
        elif parent == "no":
            print("I'm sorry but you are too young to watch this movie without an adult.")
        else:
            print("Please answer yes or no.")
