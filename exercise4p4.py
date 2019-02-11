#Pick a number and save it in a variable called secret_number. Ask the user
#to enter a number. If they enter the secret number, print "You win!". If
#they are off by 1, print "So close!". Otherwise, print "Try again".

secret_number = 99
print("Please enter a number")
user_number = int(input())

if (user_number == secret_number):
    print("You win!")
elif (abs(secret_number-user_number) == 1):
    print("So close!")
else:
    print("Try again")
