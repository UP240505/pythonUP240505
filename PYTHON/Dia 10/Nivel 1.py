#1_______________________________________
print("Using For")
for i in range(11):
    print(i, end=" ")
print("\nUsing While")
i = 0
while i != 11:
    print(i, end=" ")
    i += 1
#2________________________________________
print("\nUsing For")
for i in range(10, -1, -1):
    print(i, end=" ")
print("\nUsing While")
i = 10
while i != -1:
    print(i, end=" ")
    i -= 1
#3______________________________________
print("\n\npattern1")
for i in range(7):
    for j in range(0, i+1):
        print("#", end="")
    print("\n", end="")
#4________________________________________
print("\n\npattern2")
for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print("\n", end="")
#5____________________________________________-
print("\n\npattern3")
for i in range(11):
    print(f"{i} x {i} = {i*i}")
#6__________________________________________
for item in ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']:
    print(item)
#7__________________________________________
for i in range(0, 101):
    if i % 2 == 0:
        print(i, end=" ")

        print("\n")
#8_________________________________
for i in range(0, 101):
    if i % 2 != 0:
        print(i, end=" ")

print("\n")
