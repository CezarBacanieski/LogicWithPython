#exercise one

value = float(input("Write the first value: "))

descont = 0.12
valueWithDescont = value * descont
print(f"Your descont is: {valueWithDescont}")

#exercise two

seconds = float(input("Write your seconds: "))

hours = seconds // 3600
seconds %= 3600
minuts = seconds // 60
seconds %= 60

print(f"{hours} hours {minuts} minuts and {seconds} seconds")

# #exercise three

ringChip = 0.40
ringFood  = 0.35 * 2
chickens = int(input("Write how many chickens do you have: "))

valueChicken = chickens * ringChip * ringFood
print(f"The totoal value is: {valueChicken}")

#exercise five

whiteVotes = int(input("White votes: "))
nullVotes = int(input("Null votes: "))
niceVotes = int(input("Valid votes: "))

totalVotes = whiteVotes + nullVotes + niceVotes
perWhite = (whiteVotes / totalVotes) * 100
perNull = (nullVotes / totalVotes) * 100
perNice = (niceVotes / totalVotes) * 100
print(f"{perWhite:.2f} {perNull:.2f} {perNice:.2f}")

#exercise six

valuePI = 3.14
valueRadius = float(input("Write the radius: "))
areaRadius = valuePI * (valueRadius * valueRadius)
print("Its here de total area: {areaRadius}")

#exercise seven 

carPrice = int(input("Write the car price: "))
imposts = 0.45
distribuidor = 0.28
custFactory = carPrice 
custWithImpost = carPrice * imposts * distribuidor
custClient = custWithImpost + carPrice

print(f"Factory cust: {custFactory} and the client cust: {custClient:.2f}")

#exercise eigth

currentSalary = int(input("Write you atual salary: "))

plus = 0.25
newSalary = currentSalary + plus
print(f"Your new salary is: {newSalary}")

# exercise nine

total = 780.000
winOne = 0.46
winTwo = 0.32

one = 780000 * winOne
two = 780000 * winTwo

winThree = one - two

print(f"{one:.2f} {two:.2f} {winThree:.2f}")

#exercise three 

daysGo = int(input("How many days did you go to work? "))
priceDay = 80

totalSalary = daysGo * priceDay
impost = totalSalary * 0.08
totalSalaryMinusImpost = totalSalary - impost

print(f"{totalSalaryMinusImpost}")

#exercise eleven 

priceBroad = 0.38
priceLittleBroad = 4.50

totalSaleBroad = int(input("How many broads did you sale? "))
totalSaleLittleBroad = int(input("How many little broads did you sale? "))

totalBroad = totalSaleBroad * priceBroad
totalLittleBroad = totalSaleLittleBroad * priceLittleBroad
valueTotal = totalBroad + totalLittleBroad

bankImpost = 0.10
bank = valueTotal * bankImpost

print(f"The total sale is {valueTotal} and for the bank is {bank}")

#exercise twelve

# dimensionLarge1 = float(input("Write the large: "))
dimensionWidth1 = float(input("Write the width first draw: "))
dimensionHeigth1 = float(input("Write the heigth both draw: "))

# dimensionLarge2 = float(input("Write the large: "))
dimensionWidth2 = float(input("Write the width to the second draw: "))


area1 = dimensionWidth1 * dimensionHeigth1

area2 = dimensionWidth2 * dimensionHeigth1

areaTotal1 = area1 + area1
areaTotal2 = area2 + area2

areaTotal = areaTotal1 + areaTotal2

totalAzuleijo = areaTotal / 1.5

print(f"{areaTotal}")
print(f"{totalAzuleijo:.2f}")