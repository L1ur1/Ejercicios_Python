#Condicionales Simples:

'''temperature = 40
if temperature > 35:
    print('Aviso por alta temperatura')
else:
    print('Parámetros normales')'''


#Condicionales Anidadas:

'''temperature = 28

if temperature < 20:
    if temperature < 10:
        print('Nivel azul')
    else:
        print('Nivel verde')
else:
    if temperature < 30:
        print('Nivel naranja')
    else:
        print('Nivel rojo')'''


#Asignación de Condicionales:

'''temperature = 35

if temperature < 30:
    fire_risk = 'LOW'
else:
    fire_risk = 'HIGH'

print(fire_risk)'''


#Match-Case Comparando Valores

'''color = '#FF0000'

match color:
    case '#FF0000':
        print('🔴')
    case '#00FF00':
        print('🟢')
    case '#0000FF':
        print('🔵')'''


#Patrones Avanzados

'''point = (2, 5)

match point:
    case (x, y):
        print(f'({x},{y}) is in plane')
    case (x, y, z):
        print(f'({x},{y},{z}) is in space')'''


#Operador Morsa - Versión Tradicional

'''radius = 4.25
perimeter = 2 * 3.14 * radius

if perimeter < 100:
    print('Increase radius to reach minimum perimeter')
    print('Actual perimeter: ', perimeter)'''


#Operador Morsa - Versión con Operador Morsa

radius = 4.25

if (perimeter := 2 * 3.14 * radius) < 100:
    print('Increase radius to reach minimum perimeter')
    print('Actual perimeter: ', perimeter)