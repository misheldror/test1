#if:
#1
num1: float = float(input('enter a num: '))
num2: float = float(input('enter a num: '))

if num1 < num2:
    smaller: float = num1
else:
    smaller: float = num2

print(smaller)
print(smaller)
print(smaller)

#2
num1: int = int(input('enter a num: '))
num2: int = int(input('enter a num: '))
snums: int = num1 + num2
av: float = snums / 2
print(av)

#3
num1: int = int(input('enter a num: '))
num2: int = int(input('enter a num: '))
num3: int = int(input('enter a num: '))

if num1 >= num2 and num1 >= num3:
    biggest: int = num1
elif num2 >= num1 and num2 >= num3:
    biggest: int = num2
else:
    biggest: int = num3

print(biggest)

#4
minutes: int = int(input('Enter the number of minutes: '))
hours: int = minutes // 60
leftmins: int = minutes % 60

print(f"{hours} hours and {leftmins} minutes.")

#5
num: int = int(input("Enter a 4-digit number: "))
rightd: int = num % 10
print(right)

#6
num: int = int(input("Enter a 4-digit number: "))
secondig: int = (num // 10) % 10
print(secondig)

#7
num: int = int(input("Enter a two-digit number: "))
asarot: int = number // 10
ahadot: int = number % 10
digit_sum: int = asarot + ahadot
print(digit_sum)

#8
num: int = int(input("Enter a two-digit number: "))
asarot: int = number // 10
ahadot: int = number % 10
swapped_number: int = ahadot * 10 + asarot
print(swapped_number)

#9
num: int= int(input("Enter a number: "))
if num % 2 == 0:
    print("even")
else:
    print("odd")


#loops:
#1
top: int = int(input('enter a num: '))
for i in range(1, top + 1):
    print(i, end='')

#2
num1: int = int(input('enter a num: '))
num2: int = int(input('enter a num: '))

if num2 > num1:
    for i in range(num1, num2 + 1):
        print(i, end=' ')
else:
    for i in range(num2, num1 + 1):
        print(i, end=' ')

#3
n: int = int(input('enter a num: '))
for i in range(0, n + 1, 2):
    print(i, end='')


#data:
#1
SENTINAL: int = -99
snum: int = 0

while True:
    num: int = int(input('enter a num: '))
    if num == SENTINAL:
        print(None)
        break
    snum += num
print(snum)

#2
SENTINAL: int = -99
largest: int = None
smallest: int = None

while True:
    num: int = int(input("Enter a number: "))
    if num == SENTINAL:
        print(None)
        break
    if num <= 0:
        break
    if largest is None or num > largest:
        largest = num
    if smallest is None or num < smallest:
        smallest = num

if largest is not None and smallest is not None:
    print(f"Largest number: {largest}")
    print(f"Smallest number: {smallest}")

#3
largest: int = None
index: int = -1

for i in range(1, 6):
    num = int(input(f"Enter number: "))
    if largest is None or num > largest:
        largest = num
        index = i

print(f"largest num is in index {index}.")


#comp loops:
#1
temperatures: list[float] = []
x: float = None

while len(temperatures) < 12:
    try:
        temp: float = float(input(f"Enter temperature: "))
        if temp < -5 or temp > 40:
            print("Wrong data")
            break
        else:
            temperatures.append(temp)
            x = temp
            print("Correct data")
        if temp == 0 and x == 0:
            temp: float = float(input(f"Enter temperature: "))
            continue

    except ValueError:
        print("enter only numbers")

if len(temperatures) == 12:
    average: float = sum(temperatures) / len(temperatures)
    lowest: float = min(temperatures)
    highest: float = max(temperatures)

    print(f"Average temperature: {average}")
    print(f"Lowest temperature: {lowest}")
    print(f"Highest temperature: {highest}")