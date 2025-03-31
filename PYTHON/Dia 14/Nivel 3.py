#1___________________________________
import json
from functools import reduce
from collections import Counter

with open('countries_data.py', 'r') as file:
    countries_data = json.load(file)

sorted_by_name = sorted(countries_data, key=lambda x: x['name'])
sorted_by_capital = sorted(countries_data, key=lambda x: x['capital'])
sorted_by_population = sorted(countries_data, key=lambda x: x['population'])

languages = [lang for country in countries_data for lang in country['languages']]
most_spoken_languages = Counter(languages).most_common(10)

top_10_populated = sorted(countries_data, key=lambda x: x['population'], reverse=True)[:10]

print("Sorted by Name:", sorted_by_name[:5])
print("Sorted by Capital:", sorted_by_capital[:5])
print("Sorted by Population:", sorted_by_population[:5])
print("Top 10 Most Spoken Languages:", most_spoken_languages)
print("Top 10 Most Populated Countries:", [(c['name'], c['population']) for c in top_10_populated])
