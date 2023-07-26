"""
Notes :
- Vérifier respect du PEP8

1) Lecture du fichier CSV
- Mettre en forme un fichier csv avec les données séparées par une virgule (comma seperated) OK
- Lire les données OK
- Afficher les données OK


"""

import csv

with open('forcebrute_dataset.csv', newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for row in reader:
        print(row)


print("----------------------------")
print("Combinaisons de 2 éléments")
print("----------------------------")
a = [1,2,3,4]
size = len(a)

for i in range(1,size):
    for j in range(i+1,size+1):
        print("{"+str(i)+";"+str(j)+"}")

print("----------------------------")
print("Combinaisons de 2 éléments")
print("----------------------------")

for i in range(0,size-1):
    for j in range(i+1,size):
        print("{"+str(a[i])+";"+str(a[j])+"}")

print("----------------------------")
print("Combinaisons de 3 éléments")
print("----------------------------")

for i in range(1,size):
    for j in range(i+1,size+1):
        for k in range(j+1, size+1):
            print("{"+str(i)+";"+str(j)+";"+str(k)+"}")

print("----------------------------")
print("Combinaisons de 4 éléments")
print("----------------------------")

for i in range(1,size+1):
    for j in range(i+1,size+1):
        for k in range(j+1, size+1):
            for l in range(k+1, size+1):
                print("{"+str(i)+";"+str(j)+";"+str(k)+";"+str(l)+"}")

print("----------------------------")
print("")
print("----------------------------")

def combination(data_set,n,k):
    size = len(data_set)
    for i in range(1,size):
        for j in range(i+1,size+1):
            print("{"+str(i)+";"+str(j)+"}")

def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(3))

def fibonacci_lineaire(n):
    a = 0
    b = 1
    c = 0

    for i in range(1,n):
        c = a + b
        a = b 
        b = c
    return b

for l in range(1,8):
    print(fibonacci_lineaire(l), end=" ")  

'''for l in range(3):
    print(show_combinations(l), end=" ")'''


def show_combinations(elements):
    print("recursif")
    size = len(elements)
    if size == 1:
        return elements[0]
    else:
        for i in range(0, size-1):
            return str(elements[i]) + " " + str(show_combinations(elements[1:]))

print()
print("test")
print(show_combinations(a))

def get_combinations(elements, k, start=0, combination=[]):
    if len(combination) == k:
        print(combination)
        return
    for i in range(start, len(elements)):
        combination.append(elements[i])
        get_combinations(elements, k, i + 1, combination)
        combination.pop()

a = [1, 2, 3, 4]

for k in range(2, len(a) + 1):
    get_combinations(a, k)
