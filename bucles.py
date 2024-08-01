#Sentencia While

'''want_greet = 'S'  # importante dar un valor inicial
while want_greet == 'S':
    print('Hola qué tal!')
    want_greet = input('¿Quiere otro saludo? [S/N] ')
print('Que tenga un buen día')'''


#Romper un Bucle While

'''MAX_GREETS = 4
num_greets = 0
want_greet = 'S'

while want_greet == 'S':
    print('Hola qué tal!')
    num_greets += 1
    if num_greets == MAX_GREETS:
        print('Máximo número de saludos alcanzado')
        break
    want_greet = input('¿Quiere otro saludo? [S/N] ')

print('Que tenga un buen día')'''


#Sentencia For

'''word = 'Python'

for letter in word:
    print(letter)'''


#Usando el Guión Bajo

'''for _ in range(10):

    print('Repeat me 10 times!')'''


#Bucles Anidados

for num_table in range(1, 10):
    for mul_factor in range(1, 10):
        result = num_table * mul_factor
        print(f'{num_table} * {mul_factor} = {result}')


