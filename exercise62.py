# You started the day with energy, but you are going to get tired as you
# travel! Keep track of your energy.
#
# If you walk, your energy should increase. If you run, it should decrease.
# Moreover, you should not be able to run if your energy is zero.
#
# ...then, go crazy with it! Allow the user to rest and eat. Do whatever you
# think might be interesting.
move_count = 0
energy = 10
max_energy = 10
distance_home = 0
still_out = True
print("What would you like to do? Your options are: \nwalk \nrun \ngo home \neat \nrest \nremind (this will list these instructions again)")
while still_out == True:
    if distance_home >= 500:
        print("The Proclaimers would be proud of you but this is kilometres, not miles. Either way you've won the game and it only took you {} moves!".format(move_count))
        still_out = False;
    else:
        response = input()
        if (response.lower() == "walk"):
            distance_home += 1
            energy += 1
            move_count += 1
            if (energy > max_energy):
                energy = max_energy
            print("Distance from home is {}km, and your energy is currently at {}.".format(distance_home, energy))
        elif ((response.lower() == "run") and (energy > 0)):
            distance_home += 5
            energy -= 1
            move_count += 1
            print("Distance from home is {}km, and your energy is currently at {}.".format(distance_home, energy))
        elif ((response.lower() == "run") and (energy == 0)):
            print("Sorry, you're too tired to run right now")
        elif ((response.lower() == "run") and (energy < 0)):
            print("I don't even know how you're typing this considering how low your energy is!")
        elif (response.lower() == "go home"):
            #Had to change what I was looping over, but now if they want
            still_out = False
            print("Hope you had fun on your walk! Your total distance was {}km today.".format(distance_home))
        elif (response.lower() == "eat"):
            energy += 3
            move_count += 1
            if (energy > max_energy):
                energy = max_energy
            print("That was delicious! Your energy is currently at {}.".format(energy))
        elif (response.lower() == "rest"):
            energy = max_energy
            move_count += 1
            print("What a nice rest. Your energy is back at {}.".format(energy))
        elif (response.lower() == "remind"):
            print("Your options are: \nwalk \nrun \ngo home \neat \nrest \nremind")
        elif ((response.lower() == "secret") and (max_energy != 15)):
            print("It's a secret to everyone, max energy increased!")
            max_energy = 15
            move_count += 1
        elif ((response.lower() == "secret") and (max_energy == 15)):
            print("Nice try, but that only works once.")
        elif (response.lower() == "cheat"):
            print("Cheaters never win. A tree falls on you. RIP")
            still_out = False
        else: #Oops, apparently I already did this part earlier
            print("Sorry, that's an invalid input")
