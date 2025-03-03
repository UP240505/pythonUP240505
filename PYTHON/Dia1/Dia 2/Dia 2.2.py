#Decaramos varibles
name='Braulio Andres' ;last_name='Martinez Picazzo';country='Aguascalientes';city='Aguascalientes';age=18;year=2025;maried=False; is_true=1
print(type(name),type(last_name),type(country),type(city),type(age),type(year),type(maried),type(is_true))
print(len(name),len(last_name))
#operaciones matetaricas vasicas
num_one=5;num_two=4;total=(num_one+num_two);diff=(num_one-num_two);product=(num_one*num_two);division=(num_one/num_two);remainder=(num_one%num_two);exp=(num_one**num_two);floor_division=(num_one//num_two)
print(total, diff, product, division, remainder, exp, floor_division)
#Caculamos las araes de circulo
import math
radio = 30
area_del_circulo = (math.pi * radio ** 2)
circunferencia_del_circulo =( 2 * math.pi * radio)
print("Area de circulo 30 radio y circuferecia=",area_del_circulo, circunferencia_del_circulo)
radio_usuario = float(input("Introduce el radio del círculo: "))
area_usuario = math.pi * radio_usuario ** 2
print("Area de usario =",area_usuario)
#Entrada de usario
nombre_usuario = input("Introduce tu nombre: ")
apellido_usuario = input("Introduce tu apellido: ")
pais_usuario = input("Introduce tu país: ")
edad_usuario = int(input("Introduce tu edad: "))
print(nombre_usuario, apellido_usuario, pais_usuario, edad_usuario)