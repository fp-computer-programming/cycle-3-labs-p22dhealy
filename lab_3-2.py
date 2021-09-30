# author: DMH 9/29/21

points = int(input("How many points does your team have?"))

if points == 15:
    print("You got a gold medal!")
elif points > 11:
    print("You got a silver medal!")
elif points > 7:
    print("You got a bronze medal!")
else: 
    print("You did not get a medal!")
    

