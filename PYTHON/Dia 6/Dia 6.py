# Crear una tupla vacía
tp = ()

# Definir tuplas con nombres de hermanos y hermanas
tp_brothers = ('alpha', 'bravo', 'charlie')
tp_sisters = ('alita',)

# Combinar las tuplas de hermanos y hermanas
tp_siblings = tp_brothers + tp_sisters
print(tp_siblings)  # Muestra todos los hermanos
print(len(tp_siblings))  # Longitud de la tupla (número de hermanos)

# Añadir información sobre los padres
tp_siblings += ('fathername',)
tp_siblings += ('mothername',)
family_members = tp_siblings
print(family_members)  # Muestra a todos los miembros de la familia

# Separar la tupla en hermanos y padres
siblings, parents = family_members[:4], family_members[4:]
print(siblings)  # Lista de hermanos
print(parents)  # Lista de padres

# Crear tuplas de frutas, vegetales y productos animales
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
animal_products = ('milk', 'curd')

# Combinar todo en una sola tupla de alimentos
food_stuff = fruits + vegetables + animal_products
print(food_stuff)  # Imprime la combinación de alimentos

# Encontrar y mostrar el/los elemento(s) del medio de la tupla
if len(food_stuff) % 2 == 0:  # Si la longitud es par
    print(food_stuff[(len(food_stuff)//2)-1])  # Elemento justo antes del centro
    print(food_stuff[len(food_stuff)//2])  # Elemento justo después del centro
else:  # Si la longitud es impar
    print(food_stuff[len(food_stuff)//2])  # Elemento del centro

# Crear una nueva tupla con los 3 primeros y 3 últimos elementos
newtp = food_stuff[:3] + food_stuff[-3:]
print(newtp)  # Muestra los elementos seleccionados

# Eliminar la tupla food_stuff
del food_stuff

# Tupla de países nórdicos
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
if 'Estonia' in nordic_countries:
    print("Estonia es un país nórdico")
if 'Iceland' in nordic_countries:
    print("Iceland es un país nórdico")
