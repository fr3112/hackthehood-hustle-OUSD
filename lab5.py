# Lab5 Erika Ramos

# Step 1
def cat_greeting(word):
    print(f"Cat says {word}")

cat_greeting("Meow")

# Step 2
name = "Laura"
superPower = "Teletransportation"

def generate_superhero_power():

    print(f"This superhero name is {name}, this superhero has the power of {superPower}")

generate_superhero_power()

# Step 3
def generate_superhero_power1():
    superPower = "Flying"
    return superPower
print(generate_superhero_power1())

# Step 4
def generate_superhero_power2(user_name, super_power):
    message =  f"{user_name} is a super hero  with {super_power}"
    return message
print(generate_superhero_power2("Carlos", "invisibility"))

# Step 5
def cat_greeting_loop():
    for i in range(5):
        print("Meow!")
cat_greeting_loop()

# Step 6
def generate_multiple_powers(powers):
    for i in powers:
        print(i)

powers = ["Flying", "Invisiblity", "Teletransportation", "Super Strength"]
generate_multiple_powers(powers)
