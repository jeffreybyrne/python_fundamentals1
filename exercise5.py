# You decide to get some exercise and fresh air, but you want to keep track
# of how far from home you are.
#
# Ask the user for input on what action to take - walk or run. If they walk,
# the total distance should go up by one, and you should update the user on
# their total distance traveled as follows:
#
# "Distance from home is 6 km."
#
# If they run, their total distance should go up by 5. Your program should
# keep asking for input - you don't know where you're going until you get
# there! Each time, you should print the total distance traveled.
distance_home = 0

while distance_home >= 0:
    print("Would you like to walk or run?")
    response = input()
    if (response.lower() == "walk"):
        distance_home = distance_home + 1
        print("Distance from home is {}km".format(distance_home))
    elif (response.lower() == "run"):
        distance_home = distance_home + 5
        print("Distance from home is {}km".format(distance_home))
    else:
        print("Sorry, that's an invalid input")
