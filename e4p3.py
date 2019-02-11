#Save your name as a string into a variable, then ask the user to enter
#their name. If the two names match, print "We have the same name!".

my_name = "Jeff"
my_full_name = "Jeffrey"
print("What's your name?")
user_name = input()

if (my_name.lower() == user_name.lower()) or (my_full_name.lower() == user_name.lower()):
    print("We have the same name!")
else:
    print("Sadly your name isn't that great")
