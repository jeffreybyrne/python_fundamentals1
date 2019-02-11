#Ask the user to enter their age, and then display a message telling them
#how many years apart in age you are from them. If they enter a number
# larger than 105, print "I'm not sure I believe you".

jeff_age = 30
print("How old are you?")
user_age = int(input())
age_diff = abs(jeff_age-user_age)
if (user_age > 105):
    print("I'm not sure I believe you")
elif (age_diff == 0):
    print("We're the same age!")
elif (age_diff == 1):
    print("The age difference between us is {} year.".format(age_diff))
else:
    print("The age difference between us is {} years.".format(age_diff))
