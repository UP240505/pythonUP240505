from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for country in countries:
    print(country)

for name in names:
    print(name)

for number in numbers:
    print(number)
#1_______________________________________
upper_countries = map(lambda country: country.upper(), countries)
print(list(upper_countries))
#2_______________________________________
squares = map(lambda x: x*x, numbers)
print(list(squares))
#3_______________________________________
upper_names = map(lambda name: name.upper(), names)
print(list(upper_names))
#4_______________________________________
def is_land(s):
    if 'land' in s:
        return True
    else:
        return False
    
land = filter(is_land, countries)
print(list(land))
#5_______________________________________
def six_chars(s):
    if len(s) == 6:
        return True
    else:
        return False

six = filter(six_chars, countries)
print(list(six))
#6_______________________________________
def six_ormore(s):
    if len(s) >= 6:
        return True
    else:
        return False

six_more = filter(six_ormore, countries)
print(list(six_more))
#7_______________________________________
def start_with(s):
    if s[0] == 'E':
        return True
    else:
        return False

start = filter(start_with, countries)
print(list(start))
#8_______________________________________
from functools import reduce
result = reduce(
    lambda x, y: x + y,
    filter(
        lambda num: num % 2 == 0,
        map(lambda num: num ** 2, numbers)
    )
)
print(result)  
#9_______________________________________
def get_string_lists(lst):
    new = []
    for item in lst:
        if type(item) == str:
            new.append(item)
    return new

print(get_string_lists([1, 2, 3, 4, 5, 7, 'hllo']))
#10_______________________________________
def add(x, y):
    return int(x) + int(y)


total = reduce(add, ['1', '2', '3', '4', '5'])
print(total)
#11_______________________________________
def concat(s1, s2):
    return s1+", "+s2


print(reduce(concat, countries), "are noth European countries")
#12_______________________________________
countries = [
    'Afghanistan',
    'Albania',
    'Algeria',
    'Andorra',
    'Angola',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bhutan',
    'Bolivia',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Cape Verde',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Colombi',
    'Comoros',
    'Congo (Brazzaville)',
    'Congo',
    'Costa Rica',
    "Cote d'Ivoire",
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'East Timor (Timor Timur)',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Ethiopia',
    'Fiji',
    'Finland',
    'France',
    'Gabon',
    'Gambia, The',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Grenada',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Korea, North',
    'Korea, South',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Macedonia',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Mauritania',
    'Mauritius',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Qatar',
    'Romania',
    'Russia',
    'Rwanda',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Vincent',
    'Samoa',
    'San Marino',
    'Sao Tome and Principe',
    'Saudi Arabia',
    'Senegal',
    'Serbia and Montenegro',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Swaziland',
    'Sweden',
    'Switzerland',
    'Syria',
    'Taiwan',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Togo',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United States',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
    'Yemen',
    'Zambia',
    'Zimbabwe',
]
land = []
ia = []
island = []
stan = []
#13_______________________________________
for country in countries:
    country = country.lower()
    if 'land' in country:
        land.append(country)
    if 'ia' in country:
        ia.append(country)
    if 'island' in country:
        island.append(country)
    if 'stan' in country:
        stan.append(country)
print(f"countries with 'land' are:\n{land}")
print(f"countries with 'ia' are:\n{ia}")
print(f"countries with 'island' are:\n{island}")
print(f"countries with 'stan' are:\n{stan}")

print("Countries in order")
dic = {}
for country in countries:
    if country[0] in dic:
        dic[country[0]] += 1
    else:
        dic[country[0]] = 1
print(dic)
#14_______________________________________
def get_first_ten_countries(countries):
    lst = []
    for i in range(10):
        lst.append(countries[i])
    return lst

print(get_first_ten_countries(countries))
#15_______________________________________
def get_last_ten_countries(countries):
    lst = []
    for i in range(1, 11):
        lst.append(countries[-i])
    return lst

print(get_last_ten_countries(countries))