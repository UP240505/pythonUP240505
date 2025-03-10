# Crear y trabajar con una lista vacía
lst = []
lst = [1, 2, 3, 4, 5, 6, 7]  # Crea una lista con números del 1 al 7
print(lst)

print(len(lst))  # Muestra la longitud de la lista

# Primer, último y elemento medio
fitem = lst[0]  # Primer elemento
litem = lst[len(lst)-1]  # Último elemento
mitem = lst[(len(lst)//2)+1]  # Elemento del medio
print(fitem, mitem, litem)

# Crear una lista de tipos de datos mixtos
mixed_data_types = ["sumanth", 12, 185, "single", "LA,USA"]  # Diferentes tipos de datos en una lista
print(mixed_data_types)

# Lista de empresas tecnológicas
it_companies = ["Facebook", "Goolge", "Microsoft",
                "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print(f"No de empresas: {len(it_companies)}")  # Número de empresas

# Manipular y modificar elementos en la lista
it_companies[0] = "Cisco"  # Cambiar el primer elemento
it_companies.append("Palo Alto")  # Añadir un elemento al final
it_companies.insert((len(it_companies)//2)+1, "Juniper")  # Insertar en el medio

it_companies[0] = it_companies[0].upper()  # Convertir a mayúsculas el primer elemento
print("#; ".join(it_companies))  # Unir elementos con un delimitador

# Ordenar, invertir y manipular la lista
it_companies.sort()  # Ordenar alfabéticamente
it_companies.reverse()  # Invertir el orden
print(it_companies[:3])  # Primeros tres elementos
print(it_companies[-3:])  # Últimos tres elementos

# Vaciar y eliminar la lista
it_companies.clear()
print(it_companies)
del it_companies

# Listas de tecnologías web
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']  # Tecnologías frontend
back_end = ['Node', 'Express', 'MongoDB']  # Tecnologías backend
web_technologies = front_end + back_end  # Combinar ambas listas
print(web_technologies)

# Trabajar con edades
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()  # Ordenar las edades
print(f"Mínima: {ages[0]}, Máxima: {ages[-1]}")  # Edad mínima y máxima
median = (ages[len(ages)//2] + ages[(len(ages)//2)-1]) / 2  # Calcular mediana
average = sum(ages) / len(ages)  # Calcular promedio
print(average)
