# Concatenación de cadenas (strings)
ew1 = "Thiry " + "Days " + "Of " + "Python"  # Crea una cadena uniendo varias palabras
new2 = "Coding " + "For " + "All"  # Otra cadena formada por concatenación

# Asignación de valores
company = new2
print(company)  # Imprime el valor de la variable "company"
print(len(company))  # Imprime la longitud de la cadena "company"

# Métodos de cambio de formato en cadenas
upper_company = company.upper()  # Convierte todo el texto a mayúsculas
lower_company = company.lower()  # Convierte todo el texto a minúsculas
cap = new2.capitalize()  # Convierte la primera letra a mayúscula
tit = new2.title()  # Convierte cada palabra para que comience en mayúscula
swp = new2.swapcase()  # Invierte las mayúsculas y minúsculas
print(cap, tit, swp)  # Muestra los resultados de las conversiones

# Slicing (cortar cadenas)
cut = new2[:6]  # Extrae los primeros 6 caracteres de la cadena
print(new2.index("Coding"))  # Encuentra el índice de la palabra "Coding"

# Reemplazo de palabras en cadenas
new3 = new2.replace("Coding", "Python")  # Reemplaza "Coding" por "Python"

# Más reemplazo
new4 = "Python for Everyone"
new4 = new3.replace("Everyone", "All")  # Cambia "Everyone" por "All"

# División de cadenas
new2_lst = new2.split()  # Divide la cadena "new2" en una lista por espacios
new5 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
new5_lst = new5.split(",")  # Divide la cadena "new5" en una lista por comas

# Indexación de caracteres
print(new2[0])  # Primer carácter
print(new2[-1])  # Último carácter
print(new2[10])  # Carácter en el índice 10

# Acrónimos
new4_acr = "PFE"  # Acrónimo de "Python For Everyone"
new2_acr = "CFA"  # Acrónimo de "Coding For All"

# Índices específicos
print(new2.index("C"))  # Encuentra el índice de "C"
print(new2.index("F"))  # Encuentra el índice de "F"

# Búsqueda en cadenas
print("Coding For All People".rfind("I"))  # Encuentra la última "I"
print("You cannot end a sentence with because because because is a conjunction".find('because'))  # Encuentra "because"
print("You cannot end a sentence with because because because is a conjunction"[31:54])  # Corta el fragmento "because because because"

# Verificar inicios y finales
print("Coding For All".startswith("Coding"))  # Verifica si comienza con "Coding"
print("Coding For All".endswith("coding"))  # Verifica si termina con "coding"

# Remover espacios en blanco
print('   Coding For All      '.strip())  # Quita los espacios al principio y final

# Identificadores válidos
print("30DaysOfPython".isidentifier())  # Verifica si es un identificador válido
print("thirty_days_of_python".isidentifier())

# Lista de frameworks
lst = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# ".join(lst))  # Une los elementos de la lista con " # "

# Secuencia de escape
print("I am enjoying this challenge.\nI just wonder what is next.")  # Salto de línea
print("Name\tAge\tCountry\nAsabeneh\t250\tFinland")  # Separación con tabulaciones

# Cálculo del área de un círculo
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a cricle with radius {radius} is {area} meters square.")  # Usa f-strings para interpolación

# Operaciones matemáticas
print(f"8 + 6 = {8+6}\n8 - 6 = {8-6}\n8 * 6 = {8*6}\n8 / 6 = {8/6:.2f}\n8 % 6 = {8%6}\n8 // 6 = {8//6}\n8 ** 6 = {8**6}")
