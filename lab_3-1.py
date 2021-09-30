# author: DMH 9/29/21

points = input("How many points does your team have?")

if int(points) == 15:
    print("You got a gold medal!")
else:
    if int(points) > 11:
        print("You have a silver medal!")
    else:
        if int(points) > 7:
            print("You have a bronze medal!")
        else:
            print("You did not get a medal")