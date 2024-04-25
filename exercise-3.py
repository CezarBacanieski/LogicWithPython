#1
sum = 0
for num in range(1001):
    if num % 3 == 0 or num % 5 == 0:
        sum += num
        print(sum)

#2
for numero in range(2, 1000):
    if numero > 1:
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                break
        else:
            print(numero, end=' ')

#3
salary = 2000
salaryNoGrow = 0
grow = 1.5

for ano in range (2016, 2024):
    
    salary += salary * (grow / 100)
    grow *= 2
    print(f"{salary:.2f}")

#4
a = int(input("Type the number a: "))
b = int(input("Type the number b: "))
sum = 0
for num in range(a, b + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else: sum += num
    
print(f"the sum between {a} and {b} is: {sum}")
        
#5
import random

random_number = random.randint(1, 100)
attempts = 0

print("Welcome to the guessing game!")
print("Try to guess the random number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < random_number:
        print("The number is higher.")
    elif guess > random_number:
        print("The number is lower.")
    else:
        print(f"Congratulations! You guessed the number {random_number} in {attempts} attempts.")
        break
