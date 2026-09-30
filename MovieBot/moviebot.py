print("Welcome to the movie theatre!") #Little intro
age = int(input("This movie is rated R. How old are you?")) #Asks the user for age
if age >= 18: #Checks if age is above 18, if so lets them in
    print("Enjoy the movie!")
else:
    parent =(input("Since you are under 18 is a parent here with you? yes/no"))
    if parent == "yes":
        print("Enjoy the movie!")
    if parent == "no":
        print("I'm sorry but you are too young to watch this movie without an adult.")





    
    
    

