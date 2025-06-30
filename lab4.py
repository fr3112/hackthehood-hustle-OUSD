# Set up a control variable (e.g., continue_checking = "yes")

# Use a while loop that checks if continue_checking is "yes"
# Inside the loop:
    # Ask the user for an age
    # Check if they are eligible to vote (if age >= 18)
	#-> if they are, what should we display?
	#-> if they aren’t, what should we display?
    # Ask if user wants to check another age (i.e., update continue_checking)

check_age = "yes"

while check_age == "yes" :
    age = input("Put your age: ")
    if int(age) >= 18:
        print("You can vote")

    else :
        print("You can't vote")
    
    check_age = input("Do you want to put another age?(write \"yes\" or \"no\"): ")

#task 2
list = [0, 1, -5, -8, 15, 8, -38]

for x in list:
    if x == 0:
        print("Zero value")
    elif x<0:
        print("Negative value")
    else:
        print("Positve value")

#task 3

backpack = ["Coal", "Dirt", "Diamond", "Gravel", "Stone"]

for i in backpack:
    if i == "Diamond":
        print("Jackpot!")
    else:
        print("You are poor")


check_age = "yes"

while check_age == "yes" :
    age = input("Put your age: ")
    if int(age) >= 18:
        print("You can vote")

    else:
        print("You can't vote")
    
    check_age = input("Put \"yes\" if you want to check again or write \"stop\" to exit, otherwise the check will be repeated: ")

    