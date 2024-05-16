# ONE
# def aprovado(nota1, nota2):
#     media = (nota1 + nota2) / 2
#     if media >= 6:
#         print("Aprovado")
#     else:
#         print("Reprovado")

# nota1 = int(input("Digite a primeira nota: "))
# nota2 = int(input("Digite a segunda nota: "))
# aprovado(nota1, nota2)


# two
# def dobro(num):
#     print(num * 2 ) 

# num = int(input("Digite um numero inteiro: "))
# dobro(num)


#three
# def par_impar(num):
#     if num % 2 == 0:
#         return print("True")
#     else:
#         return print("False")
    
# num = int(input("Digite um numero inteiro: "))
# par_impar(num)

#four

# def area(raio):
#     area = 3.14 ** raio 
#     print(area)

# def perimetro(raio):
#     perimetro = 3.14 * 2 * raio 
#     print(perimetro)

# raio = int(input("Digite o raio: "))

# area(raio)
# perimetro(raio)

# five

# def ler_numero():
#     num = int(input("Digite um numero inteiro: "))
#     return num 

# def tabuada(num):
#     for i in range(1, 11):
#         print(f"{num} x {i} = {num * i}")

# def main():
#     num = ler_numero()
#     tabuada(num)

# main()

# six

def menu():
    print("Calculadora:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair do programa")j
    while True:
        opcao = input("Selecione sua opção: ")
        if opcao in ['1', '2', '3', '4', '5']:
            return opcao
        else:
            print("Opção inválida. Por favor, selecione uma opção válida.")

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    else:
        return a / b

def main():
    while True:
        opcao = menu()
        
        if opcao == '5':
            print("Encerrando o programa.")
            break
        
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        if opcao == '1':
            print("Resultado:", adicao(num1, num2))
        elif opcao == '2':
            print("Resultado:", subtracao(num1, num2))
        elif opcao == '3':
            print("Resultado:", multiplicacao(num1, num2))
        elif opcao == '4':
            print("Resultado:", divisao(num1, num2))

if __name__ == "__main__":
    main()

    
    
    
   
   
    
    
        

