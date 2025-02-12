import random

# Úkol 1
soucet = 0
for i in range(20):
    number = random.randint(0,99999999999999999999999999999999999999999)
    print(number)
    soucet += number
print(soucet)

# Úkol 2
pocet = 0
for i in range(10):
    number = random.randint(0,99999999999999999999999999999999999999999)
    print(number)
    if number % 2 == 0:
        pocet += 1
print(pocet)

# Úkol 3
randlist = []
positivelist = []
print("seznam:")
for i in range(15):
    number = random.randint(-10,10)
    print(number)
    randlist.append(number)
print("kladny seznam:")
for i in range(15):
    if randlist[i] > 0:
        print(randlist[i])
        positivelist.append(randlist[i])

# Úkol 4
randlist = [random.randint(1, 100) for _ in range(10)]
print("Seznam:", randlist)
first, second = sorted(randlist[-2:])
for num in randlist[:-2]:
    if num > first:
        second, first = first, num
    elif num > second:
        second = num
print("Druhé největší číslo:", second)

# Úkol 5
randlist = [random.randint(1, 20) for _ in range(15)]
print("Původní seznam:", randlist)
seen = set()
unique_list = [x for x in randlist if x not in seen and not seen.add(x)]
print("Seznam bez duplicit:", unique_list)

# Úkol 6
N = int(input("Zadej počet členů Fibonacciho posloupnosti: "))
fib = [0, 1]
for _ in range(N-2):
    fib.append(fib[-1] + fib[-2])
print("Fibonacciho posloupnost:", fib[:N])

# Úkol 7
randlist = [random.randint(1, 50) for _ in range(10)]
target = int(input("Zadej cílový součet: "))
found = False
for i in range(len(randlist)):
    for j in range(i+1, len(randlist)):
        if randlist[i] + randlist[j] == target:
            print("Čísla:", randlist[i], randlist[j])
            found = True
            break
if not found:
    print("Žádná dvojice nenalezena.")

# Úkol 8
import time
randlist = []
print("seznam:")
for i in range(10):
    number = random.randint(-10,10)
    randlist.append(number)
print(randlist)
print("sorting...")
for j in range(10):
    for i in range(10 - 1):
        if randlist[i] > randlist[i + 1]:
            randlist[i], randlist[i + 1] = randlist[i + 1], randlist[i]
        print(randlist)
        time.sleep(0.1)
print("serazeny list:")
print(randlist)

# Úkol 9
binary = input("Zadej binární číslo: ")
decimal = 0
for i, digit in enumerate(reversed(binary)):
    decimal += int(digit) * (2 ** i)
print("Desítková reprezentace:", decimal)

# Úkol 10
randlist = [random.randint(1, 50) for _ in range(10)]
print("Seznam:", randlist)
print("Je palindrom" if randlist == randlist[::-1] else "Není palindrom")

# Úkol 11
randlist = [random.randint(1, 20) for _ in range(10)]
print("Seznam:", randlist)
for num in randlist:
    if randlist.count(num) == 1:
        print("První unikátní prvek:", num)
        break

# Úkol 12
randlist = sorted(random.sample(range(1, 30), 10))
print("Seřazený seznam:", randlist)
missing = [x for x in range(randlist[0], randlist[-1]) if x not in randlist]
print("Chybějící hodnoty:", missing)

# Úkol 13
randlist = sorted([random.randint(1, 100) for _ in range(10)])
print("Seřazený seznam:", randlist)
max_diff = max(randlist[i+1] - randlist[i] for i in range(len(randlist)-1))
print("Největší rozdíl mezi sousedními prvky:", max_diff)

# Úkol 14
randlist = [random.randint(1, 50) for _ in range(20)]
print("Seznam:", randlist)
longest = []
current = [randlist[0]]
for i in range(1, len(randlist)):
    if randlist[i] > randlist[i-1]:
        current.append(randlist[i])
    else:
        if len(current) > len(longest):
            longest = current
        current = [randlist[i]]
if len(current) > len(longest):
    longest = current
print("Nejdelší rostoucí sekvence:", longest)

# Úkol 15
randlist = [random.randint(1, 100) for _ in range(10)]
print("Seznam:", randlist)
first, second = sorted(randlist[-2:])
for num in randlist[:-2]:
    if num > first:
        second, first = first, num
    elif num > second:
        second = num
print("Dvě čísla s největším součtem:", first, second)
