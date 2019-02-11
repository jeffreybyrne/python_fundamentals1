# You started the day with energy, but you are going to get tired as you
# travel! Keep track of your energy.
#
# If you walk, your energy should increase. If you run, it should decrease.
# Moreover, you should not be able to run if your energy is zero.
#
# ...then, go crazy with it! Allow the user to rest and eat. Do whatever you
# think might be interesting.

#Set some initial variables, most of which are extras.
move_count = 0 #Count the total number of moves the user has made
energy = 10 #User starts off with 10 energy
max_energy = 10 #Max energy to start is 10
distance_home = 0 #User starts at home, so the initial distance is 0
run_count = 0 #Will be used to track how many times in a row the user has run
run_distance = 5 #Distance the user moves by running, starts at 5
still_out = True #Tracking whether or not they're still playing, basically
print("What would you like to do? Your options are: \nwalk \nrun \ngo home \neat \nrest \nremind (this will list these instructions again)")
while still_out == True:
    if distance_home >= 500: #Easter egg! You've won the game if you get this far
        print("The Proclaimers would be proud of you but this is kilometres, not miles. Either way you've won the game and it only took you {} moves!".format(move_count))
        still_out = False;
    else:
        response = input()
        if (response.lower() == "walk"):
            #Increase distance by one, regain one energy, increment the total move tracker, and reset the run tracker
            distance_home += 1
            energy += 1
            move_count += 1
            run_count = 0
            #Make sure they aren't going over their energy cap
            if (energy > max_energy):
                energy = max_energy
            print("Distance from home is {}km, and your energy is currently at {}.".format(distance_home, energy))
        elif ((response.lower() == "run") and (energy > 0)):
            #If they still have energy, they can run. Add the run distance to their total distance, decrease energy by one, increment the move counter and the run counter
            distance_home += run_distance
            energy -= 1
            move_count += 1
            run_count += 1
            #If they've run ten times in a row give them a penalty
            if (run_count >= 10):
                run_distance -= 1
                run_count = 0
                print("Oh no, you ran too many times in a row! Now you can't run that far because your legs are really tired. Maybe try resting for a while. Distance from home is {}km, and your energy is currently at {}.".format(distance_home, energy))
            else:
                print("Distance from home is {}km, and your energy is currently at {}.".format(distance_home, energy))
        elif ((response.lower() == "run") and (energy == 0)):
            #If they're out of energy, don't let them run
            print("Sorry, you're too tired to run right now")
        elif ((response.lower() == "run") and (energy < 0)):
            #If they somehow end up with negative energy, don't let them run
            print("I don't even know how you're typing this considering how low your energy is!")
        elif (response.lower() == "go home"):
            #If they want to end the game, they can
            still_out = False
            print("Hope you had fun on your walk! Your total distance was {}km today.".format(distance_home))
        elif (response.lower() == "eat"):
            #Let them eat! Restore three energy, increment the move counter, reset the run counter
            energy += 3
            move_count += 1
            run_count = 0
            #Again just making sure they aren't going over the energy cap
            if (energy > max_energy):
                energy = max_energy
            print("That was delicious! Your energy is currently at {}.".format(energy))
        elif (response.lower() == "rest"):
            #Let the user take a rest. Restores all energy, increments the move counter, resets the run counter, and set their run distance back to 5 in case they tired themselves out earlier
            energy = max_energy
            move_count += 1
            run_count = 0
            run_distance = 5
            print("What a nice rest. Your energy is back at {}.".format(energy))
        elif (response.lower() == "remind"):
            #Remind the user of the suggested input
            print("Your options are: \nwalk \nrun \ngo home \neat \nrest \nremind")
        elif ((response.lower() == "secret") and (max_energy != 15)):
            #Just a little secret I added in, inreases max energy :D
            print("It's a secret to everyone, max energy increased!")
            energy = 15
            max_energy = 15
            move_count += 1
            run_count = 0
        elif ((response.lower() == "secret") and (max_energy == 15)):
            #Secrets only work once, okay?
            print("Nice try, but that only works once.")
        elif (response.lower() == "cheat"):
            #Cheaters never prosper
            print("Cheaters never win. A tree falls on you, and nobody is around to hear you scream. RIP")
            still_out = False
        else: #Handle unsupported input
            print("Sorry, that's an invalid input.")
