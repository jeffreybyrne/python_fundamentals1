#Ask the user to enter a number. Use an if statement to print "that's a big
# number!" if the number is 100 or more, or "why not dream a little bigger?"
# otherwise.

print("Please enter a number")
user_number = int(input())

if (user_number >= 100):
    print("That's a big number!")
else:
    print("Why not dream a little bigger?")
