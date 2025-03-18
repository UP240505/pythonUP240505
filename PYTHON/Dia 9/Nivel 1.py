age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18-age} more years to learn to drive.")

my_age = int(input("Enter my age: "))
your_age = int(input("Enter your age: "))
if my_age > your_age:
    print(f"I am {my_age-your_age} years older than you.")
elif my_age == your_age:
    print("Our ages are same")
else:
    print(f"You are {your_age-my_age} years older than me.")

a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a > b:
    print(f"{a} is greater then {b}")
elif a == b:
    print("Both values are same")
else:
    print(f"{b} is greater then {a}.")