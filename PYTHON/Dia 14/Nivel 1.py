#1_______________________________________
from functools import reduce
#2_______________________________________
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#3_______________________________________
for country in countries:
    print(country)

for name in names:
    print(name)

for number in numbers:
    print(number)
#4_______________________________________
upper_countries = map(lambda country: country.upper(), countries)
print(list(upper_countries))
#5_______________________________________
upper_names = map(lambda name: name.upper(), names)
print(list(upper_names))
#6_______________________________________
squares = map(lambda x: x*x, numbers)
print(list(squares))