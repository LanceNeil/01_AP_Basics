# ask the user for their name
username = input("What is your name?")

# ask the user for their favorite number (integer)
fave_num = int(input("What is your favorite number?"))

# Double, halve and square the user's favorite number
double = fave_num * 2
halve = fave_num / 2
square = fave_num **2

# Greet the user
print(f"\nHi {username}, your favorite number is {fave_num}")

# Output the result of doubling, halving and squaring their favourite integer
# squaring their favourite integer
print(f"Double {fave_num} is {double}")
print(f"Half {fave_num} is {halve}")
print(f" {fave_num} squared is {square}")
print()
print("Have a nice day!")
