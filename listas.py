#Creando Listas

'''empty_list = []
languages = ['Python', 'Ruby', 'Javascript']
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13]
data = ['Tenerife', {'cielo': 'limpio', 'temp': 24}, 3718, (28.2933947, -16.5226597)]'''


#Operaciones con Listas - Obtener un Elemento

'''shopping = ['Agua', 'Huevos', 'Aceite']
shopping[0]
print(shopping)'''


#Añadir al final de la Lista

'''shopping = ['Agua', 'Huevos', 'Aceite']

shopping.append('Atún')
print(shopping)'''



#Creando desde vacío

'''even_numbers = []

for i in range(20):
    if i % 2 == 2:
        even_numbers.append(i)
print(even_numbers)'''


#Añadir en cualquier posición de una lista

shopping = ['Agua', 'Huevos', 'Aceite']
shopping.insert(1, 'Jamón')
print(shopping)