#1__________________________________
sum = 0
for i in range(0, 101):
    sum += i
print(f"The sum of all numbers is {sum}.")

sum = 0
for i in range(0, 101):
    if i % 2 == 0:
        sum += i

print(f"The sum of all evens is {sum}.")

sum = 0
for i in range(0, 101):
    if i % 2 != 0:
        sum += i

print(f"The sum of all odds is {sum}.")
