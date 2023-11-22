import numpy as np 


vector = np.arange(1,101)
matriz = vector.reshape(10,10)

print()
print(matriz,'\n')

matriz[0][0] = 0
lista_final = []

multiplos = len(matriz)
divisores = 2

while multiplos > 1:
    for fila in range(len(matriz)):
        for columna in range(len(matriz)):
            if  matriz[fila][columna] != divisores and matriz[fila][columna] % divisores == 0:
                matriz[fila][columna] = 0
    print(f'Matriz sin divisores de {divisores}:\n')
    print(matriz)
    print()
    divisores += 1
    multiplos -=1 
    
          
for resultado in matriz:
    for resultado_1 in resultado:
        if resultado_1 != 0:
            lista_final.append(resultado_1)

print(f'Del 1 al 100 hay : {len(lista_final)} números primos')
print()
print(f'Esta es la lista de números primos del 1 al 100: {lista_final}')
    
 