#Copying & starting with a large part of the exercise we walked through with Natalie during today's lesson, I'll comment
#it all out and just use it as reference
# print("What's your name?")
# user_name = input()
# print("Hi {}!".format(user_name))
#
# print("What year were you born?")
# user_birth_year = input()
# user_age = 2019 - int(user_birth_year)
# print("You are {} years old".format(user_age))
#
# print("What day of the week is it?")
# day_of_week = input()
#
# if day_of_week.lower() == "tuesday":
#     print("Happy Tuesday!")
#     print("Do you like Tuesdays?")
#     like_tues = input()
#     if like_tues.lower() == 'yes' or like_tues.lower() == 'y':
#         print("Yay!")
#     else:
#         print("Sorry :'(")
# elif day_of_week.lower() == "wednesday":
#     print("Happy Wednesday!")
#     print("You're halfway through the week")
# elif day_of_week.lower() == "sunday":
#     print("Happy Sunday!")
# else:
#     print("Goodbye!")
#     print("Have a good day!")

print("What is your name?")
user_name = input()
print("Hello, {}".format(user_name))

secret_password = "please"

print("What's the password?")
password_attempt=input()
correct_or_not = (password_attempt == secret_password)
print("That's {}!".format(correct_or_not))

print("How many cookies have been eaten?")
eaten = input()
#Converting to an integer and subtract it from 12
cookies_left = 12 - int(eaten)
print("There are {} cookies left.".format(cookies_left))

#Ask for the user's birth year
print("What year were you born?")
user_birth_year = input()
#Calculate their initial age value
user_age = 2019 - int(user_birth_year)
#Get all fancy and ask if they've had a birthday yet
print("Have you had your birthday yet this year? (Enter \"yes\" or \"no\")")
birthday = input()
#If they haven't had a birthday yet, subtract one from their assumed age
if birthday.lower() == "no":
    user_age = user_age - 1
    print("You are {} years old, {}.".format(user_age, user_name))
#If they have had a birthday, stick with the value we already had
elif birthday.lower() == "yes":
    print("You are {} years old, {}.".format(user_age, user_name))
#If they give anything else, give them an error
else:
    print("\"{}\" is an invalid response, sorry.".format(birthday))
