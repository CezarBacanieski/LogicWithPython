# word = input("Writte a letter: ").lower()

# match word:
#     case "a" | "e" | "i" | "o" | "u":
#         print("vogal")
#     case _:
#         print("Consoante")


# one

totalValue = float(input("Write the total value of shop: "))
typePerson = int(input("Write your identify code: (1 commoun client), (2 employee) or (3 vip): "))

descountEmployee = totalValue -  0.10 * totalValue
descountVip = totalValue -  0.05 * totalValue
match typePerson:
    case 1:
        print(f"The total is: {totalValue}")
    case 2: 
        print(f"Your total is: {descountEmployee}")
    case 3:
        print(f"Your total is: {descountVip}")

# two
status = input("Write your status (S, C, V, D): ").lower()

match status:
    case "s":
        print("Single")
    case "c":
        print("Married")
    case "v":
        print("Widow")
    case "d":
        print("Divorcied")
    case _:
        print("You need to write a correct letter!")

# three
number = float(input("Write some number: "))
type = int(input("Select the calculate type: (1)The double, (2)The half, (3)0.10 of the number: "))

double = number * 2
half = number // 2 
percent = number * 0.10

match type:
    case 1:
        print(double)
    case 2:
        print(half)
    case 3:
        print(percent)
    
# four
intNumber = int(input("Write a int number: "))

match intNumber % 3:
    case 0:
        print("The number is divisible by three!")
    case _:
        print("The number isnt divisible by three!")

# five
codeLecture = int(input("Write the lecture code: "))

match codeLecture:
    case 1:
        print("Lecture: Linux | Auditorium: 1 ")
    case 2:
        print("Lecture: Database | Auditorium: 2 ")
    case 3:
        print("Lecture: Windows server | Auditorium: 3 ")
    case 4:
        print("Lecture: Logic and programming | Auditorium: 4 ")

# six
choosePlate = int(input("Choose de plate for code: \n (1) Picanha R$25 \n (2) Lasanha R$20 \n (3) Strogonoff R$20 \n (4) Bife acebolado R$15 \n (5) Bread with egg R$5: \n"))


match choosePlate:
    case 1:
        print("To pay: Picanha R$25")
        valuePlate = 25
    case 2:
        print("To pay:  Lasanha R$20")
        valuePlate = 20
    case 3:
        print("To pay:  Strogonoff R$20")
        valuePlate = 20
    case 4:
        print("To pay:  Bife acebolado R$15")
        valuePlate = 25
    case 5:
        print("To pay:  Bread with egg R$5")
        valuePlate = 5


tip = input("Do you accept to pay a tip to the waiter? (Y / N) ").lower()
valueTip = valuePlate + 0.10 * valuePlate

match tip:
    case "y":
        print(f"To pay: {valueTip}")
    case "n":
        print(f"To pay: {valuePlate}")





