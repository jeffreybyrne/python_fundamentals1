#Question 1: How would you calculate a good tip for a 55 dollar meal? Use print to print the answer.
baseCost = 55
print("$" + str(baseCost) + " is the base cost, let's give a 20% tip of $" + str(baseCost*0.2) + " for a final cost of $" + str(baseCost*1.2)) #Let's give it a

#Question 2: Try adding a string and an integer with the + operator. What happens? Find a way to convert the integer
# into a string first and use print to print the result.
#I may have accidentally done this as part of the previous exercise, but let's do it again anyway!
print("If we start with 10 and add 5 to it, we end up with " + str(10+5))

#Question 3: Try outputting the result of 45628 multiplied by 7839 in a sentence by using string interpolation.
#Also may have made the first two into sentences, but let's continue on for good measure...
print("This question wanted me to output the result of 45628 times 7839, which we all know is " + str(45628*7839))

#Question 4: What's the value of the expression (10 < 20 and 30 < 20) or not(10 == 11)?
# Try figuring it out on your own before typing it in.
# First thought is that this will be True: the first set of parenthesis will be False because the second comparison fails,
# but we're using an or to compare it with the second parenthesis which will be True because 10 doesn't equal 11, so
# using not on that will be True, so the or comparison returns True
print((10 < 20 and 30 < 20) or not(10 == 11))
#Running this from the terminal shows that it is indeed True, so that's cool!
