#1_______________________________________
def add_two_numbers(a, b):
    return a+b

print(add_two_numbers(1, 2))
#2_______________________________________
def area_of_circle(r):
    return 3.14*r*r

print(area_of_circle(5))
#3_______________________________________
def add_all_nums(*args):
    sum = 0
    for i in args:
        try:
            int(i)
            sum += i
        except:
            return "Only Int"
    return sum

print(add_all_nums(1, 2, 3, 4))
#4_______________________________________

def convert_celcius_to_farenheit(c):
    return (c * (9/5)) + 32


print(convert_celcius_to_farenheit(0))
#5_______________________________________
def check_season(month):
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


check_season("January")

#6_______________________________________
def calculate_slope(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)
#7_______________________________________
def solve_quadratic_eqn(a, b, c):
    sol1 = (-(b) + ((b)**2 - 4*a*c)**0.5)/(2*a)
    sol2 = (-(b) - ((b)**2 - 4*a*c)**0.5)/(2*a)
    print(f"Sol1 : {sol1}")
    print(f"Sol2 : {sol2}")
#8_______________________________________
def print_list(lst):
    for i in lst:
        print(i)

print_list([1, 2, 6, 8, 3])
#9_______________________________________
def reverse_list(lst):
    new_lst = []
    for i in range(-1, -(len(lst))-1, -1):
        new_lst.append(lst[i])
    return new_lst

print(reverse_list([1, 2, 3, 4]))
#10_______________________________________
def capitalize_list_items(lst):
    new_lst = []
    for item in lst:
        new_lst.append(item.capitalize())
    return new_lst

print(capitalize_list_items(['hello', 'world']))
#11_______________________________________
def add_item(lst, item):
    lst.append(item)
    return lst

numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))

#12_______________________________________
def remove_item(lst, item):
    lst.remove(item)
    return lst


numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))

#13_______________________________________
def sum_of_numbers(r):
    sum = 0
    for i in range(r+1):
        sum += i
    return sum


print(sum_of_numbers(5))
#14_______________________________________
def sum_of_odds(r):
    sum = 0
    for i in range(r+1):
        if i % 2 != 0:
            sum += i
    return sum
#15_______________________________________
def sum_of_numbers(r):
    sum = 0
    for i in range(r+1):
        if i % 2 == 0:
            sum += i
    return sum
