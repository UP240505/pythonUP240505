#Declaramos variavles
age=(18)
height=(1.85)
coplex=(1j)
#Calculamos el area y perimetro de un traigulo
B = float(input("B: "));H = float(input("H: "));areaT = (B * H) / 2
print(f"El área del triángulo es: {areaT}")
L1 = float(input('L1: '));L2 = float(input('L2: '));L3 = float(input('L3: '));perimeterT=(L1+L2+L3)
print(f"Perimetro de un Triagulo es: {perimeterT}")
#Calculamos Area y perimetro de un reatgulo
length=float(input('L:'));width=float(input('A:'));PerimeterC=2(length+width);AreaC=length*width
print(f"El área del triángulo es: {AreaC}")
print(f"Perimetro de un Triagulo es: {PerimeterC}")
#Calculamos Area y circuferecia de un circulo
import math
radio = float(input("Introduce el radio del círculo: "));area = math.pi * radio ** 2;circunferencia = 2 * math.pi * radio
print(f"El área del círculo es: {area}")
print(f"La circunferencia del círculo es: {circunferencia}")
#Calculamos la pediete de la recta
pendiente = 2;intersección_y = -2  ;intersección_x = 1   
print(f"La pendiente es: {pendiente}")
print(f"La intersección con el eje y es: {intersección_y}")
print(f"La intersección con el eje x es: {intersección_x}")
#Calculamos la pediete de dos rectas
x1, y1 = 2, 2;x2, y2 = 6, 10
pendiente = (y2 - y1) / (x2 - x1);distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"La pendiente es: {pendiente}")
print(f"La distancia euclidiana es: {distancia}")
#coparamos las pedientes anteriores
pendiente_tarea_8 = 2  
pendiente_tarea_9 = (y2 - y1) / (x2 - x1)  
comparación_pendientes = pendiente_tarea_8 == pendiente_tarea_9
print(f"Las pendientes son iguales: {comparación_pendientes}")
#igalamos dos valores hasta que de cero
valores_x = [-10, -6, -3, 0, 3, 6, 9]
for x in valores_x:
    y = x**2 + 6*x + 9
    print(f"Para x = {x}, y = {y}")
x = -3;y = x**2 + 6*x + 9
print(f"El valor de x para el cual y es 0 es: {x}")
#comparamos dos letras el tamaño
longitud_python = len("python");longitud_dragon = len("dragon");comparación_falsa = longitud_python == longitud_dragon
print(f"Comparación falsa: {comparación_falsa}")
#verifcaomos que las variables si se ecuentren
contiene_on_python = "on" in "python";contiene_on_dragon = "on" in "dragon";verificación_on = contiene_on_python and contiene_on_dragon
print(f"'on' se encuentra en 'python' y 'dragon': {verificación_on}")
#verificamos si la oracion tiene una palabra
oración = "I hope this course is not full of jargon";contiene_jargon = "jargon" in oración
print(f"La oración contiene 'jargon': {contiene_jargon}")
#verificamos que las palavras no contegan on
no_contiene_on = "on" not in "dragon" and "on" not in "python"
print(f"No hay 'on' en 'dragon' y 'python': {no_contiene_on}")
#Convertir la longitud de "python" a float y luego a string:
longitud_python = len("python");longitud_python_float = float(longitud_python);longitud_python_str = str(longitud_python_float)
print(f"Longitud de 'python' en float y luego en string: {longitud_python_str}")
#verificamos si un numero es par
numero = int(input("Introduce un número: "));es_par = numero % 2 == 0
print(f"El número {numero} es par: {es_par}")
#Verificar si la división entera de 7 entre 3 es igual al valor convertido a int de 2.7:
resultado = 7 // 3 == int(2.7)
print(f"La división entera de 7 entre 3 es igual al valor convertido a int de 2.7: {resultado}")
#Verificar si el tipo de '10' es igual al tipo de 10:
tipo_igual = type('10') == type(10)
#Verificar si int('9.8') es igual a 10:
print(f"El tipo de '10' es igual al tipo de 10: {tipo_igual}")
try:
    comparación = int('9.8') == 10
except ValueError:
    comparación = False
print(f"int('9.8') es igual a 10: {comparación}")
#Escribir un script que solicite horas y tasa por hora y calcule el pago:
horas = float(input("Introduce las horas trabajadas: "));tasa_por_hora = float(input("Introduce la tasa por hora: "));pago = horas * tasa_por_hora
print(f"El pago de la persona es: {pago}")












