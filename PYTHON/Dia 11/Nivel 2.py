#1_______________________________________
def evens_and_odds(r):
    ecount = 0
    ocount = 0
    for i in range(r+1):
        if i % 2 == 0:
            ecount += 1
        else:
            ocount += 1
    print(f"The number of odds are {ocount}.")
    print(f"The number of evenss are {ecount}.")

evens_and_odds(100)

#1_______________________________________
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

print(factorial(5))
#2_______________________________________
def is_empty(a):
    if len(a):
        print("Not Empty")
    else:
        print("Empty")
#3_______________________________________
def unique(lst):
    for i in lst:
        for j in range(i, len(lst)):
            if i == lst[j]:
                return "Not Unique"
    return "Unique"


print(unique([1, 2, 3, 4]))
