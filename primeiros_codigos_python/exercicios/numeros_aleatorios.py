import random
#gerando uma lista de 10 numeros inteiros de forma aleatória
numeros_aleatorios = {random.randint(1, 100) for elemento in range(10)}

'''
numeros_aleatorios = {}
for elemento range{10}
    numeros_aleatorios.append{randon.randint(1,100)}
'''

#Solicita ao usuario um palpite
palpite = int(input("Qual é o seu palpite? "))

#verifica se o palpite está na lista
if palpite in numeros_aleatorios:
    print("Parabéns, você acertou!")
else:
    print("Que pena, você errou!")

''' ----OUU---- 
palpite = palpite in numeros_aleatorios
'''

#exibe os resultados
print("\nLista de numeros gerados: ", numeros_aleatorios)
print("Mairo numero gerado: ", max(numeros_aleatorios))
print("Menor numero gerado: ", min(numeros_aleatorios))
print("Media dos numeros gerados: ", sum(numeros_aleatorios) / len(numeros_aleatorios))