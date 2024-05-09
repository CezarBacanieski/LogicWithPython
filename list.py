list = [4, 5, 14, 18]
name = ["Cezar", "Marcos", "Lucas"]


list = []
for i in range(10):
    n = int(input("Number: "))
    list.append(n)

print(list)


#percorrer os itens da lista
cont = 0
for item in list:
    if item % 2 == 0:
        cont +=1
print(f"The amount of even numbers is: {cont}")

# percorrer index na lista
for index in range(len(list)):
    if list[index] % 2 == 0:
        list[index] = 100

print(list)

tamanho = len(list)
print(tamanho)

maior = max(list)
print(maior)

menor = min(list)
print(menor)

soma = sum(list)
print(soma)

media = sum(list) / len(list)
print(media)

list.insert(len(list) // 2, 600)
print(list)

list.pop(3)
print(list)

list.remove(5)
print(list)


while 5 in list:
    list.remove(4)
print(list)

num = int(input("Numero: "))
if num in list:
    print("Exist")
else:
    print("Does not exist")

list.sort()
print(list)

list.sort(reverse = True)
print(list)

name.sort()
print(name)

list1 = [3, 6, 7, 7, 8]
list2 = list1.copy()
list2.append(500)
print(list1)
print(list2)

list3 = list1 + list2 + list1
print(list3)



