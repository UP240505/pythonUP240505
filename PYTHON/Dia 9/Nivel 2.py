a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a > b:
    print(f"{a} is greater then {b}")
elif a == b:
    print("Both values are same")
else:
    print(f"{b} is greater then {a}.")

s = int(input("Enter score: "))
if s >= 80 and s <= 100:
    print("A")
elif s >= 70 and s <= 79:
    print("B")
elif s >= 60 and s <= 69:
    print("C")
elif s >= 50 and s <= 59:
    print("C")
else:
    print(F)

month = input("Enter month")
if month in ['September', 'October', 'November']:
    print("Autumn")
elif month in ['December', 'January', 'February']:
    print("Winter")
elif month in ['March', 'April', 'May']:
    print("Spring")
elif month in ['June', 'July', 'August']:
    print("Summer")
else:
    print("Enter month correctly")

fruits = ['banana', 'orange', 'mango', 'lemon']
name = input("Enter a fruit")
if name not in fruits:
    fruits.append(name)
    print(fruits)
else:
    print("That fruit already exist in the list")