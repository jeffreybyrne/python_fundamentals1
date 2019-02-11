# Allow the user to go home when they are done exercising. The program should
# stop asking for input if the user enters 'go home'.
#
# See if you can also make the program tell the user when they have entered a
# command that does not exist.

distance_home = 0
still_out = True
while still_out == True:
    print("Would you like to walk, run, or go home?")
    response = input()
    if (response.lower() == "walk"):
        distance_home += 1
        print("Distance from home is {}km".format(distance_home))
    elif (response.lower() == "run"):
        distance_home += 5
        print("Distance from home is {}km".format(distance_home))
    elif (response.lower() == "go home"):
        #Had to change what I was looping over, but now if they want to go home, they can
        still_out = False
        print("Hope you had fun on your walk! Your total distance was {}km today.".format(distance_home))
    else: #Oops, apparently I already did this part earlier
        print("Sorry, that's an invalid input")
