# get user input and assign it to variable
user_input = input("Whats's your favorite day of the week? ")

weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# start conditional

if user_input == weekday[0]:
    print("Workaholic")
elif user_input == weekday[1]:
    print("Interesting")
elif user_input == weekday[2]:
    print("Humpday fanatic")
elif user_input == weekday[3]:
    print("Thursdays are the new fridays")
elif user_input == weekday[4]:
    print("Time to relax")
elif user_input == weekday[5]:
    print("Saturday, Partyday")
elif user_input == weekday[6]:
    print("Prepairing the next level...")
else:
    print("That's not a weekday, try again :)")