import random
import math

# Preencha uma lista com 10 números aleatórios únicos (sorteados de 1 a 20), ou seja, 
# sem elementos repetidos.
lista = []

while len(lista) < 10:
    num_aleatorio = random.randint(1, 20)
    if num_aleatorio not in lista:
        lista.append(num_aleatorio)

# Preencha uma lista com 30 números aleatórios (sorteados de 1 a 50). 
# A partir dessa lista, gere uma nova lista contendo apenas os números primos da lista.
        
listPrimos = []
lista = []

for i in range(30):
    lista.append(random.randint(1, 50)) 
print("Lista original:", lista)

for num in lista:
    if num <= 1:
        continue
    is_prime = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        listPrimos.append(num)

print("Lista de primos:", listPrimos)

# Preencha uma lista com 30 números aleatórios (sorteados de 1 a 50).
# A seguir solicite um número inteiro e multiplique todos os itens da lista por esse número.

lista = [random.randint(1, 50) for _ in range(30)]

print("Lista original:", lista)

numero_inteiro = int(input("Digite um número inteiro: "))

for i in range(len(lista)):
    lista[i] *= numero_inteiro

print("Lista após multiplicação:", lista)

# Preencha uma lista com 10 itens e verifique se ela é um palíndromo, ou seja, se ela é 
# igual quando lida da esquerda para a direita e da direita para a esquerda.

lista3 = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]

if lista3 == lista3[::-1]:
    print("A lista é um palíndromo.")
else:
    print("A lista não é um palíndromo.")


# Preencha duas listas com 10 elementos cada. Gere uma terceira lista de 20 elementos, 
# cujos valores deverão ser compostos pelos elementos intercalados das duas outras listas.
    
lista4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista5 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lista_intercalada = []

for i in range(len(lista4)):
    lista_intercalada.append(lista4[i])
    lista_intercalada.append(lista5[i])

print(lista_intercalada)









                











