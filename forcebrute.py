"""
Notes :
- Vérifier respect du PEP8

1) Lecture du fichier CSV
- Mettre en forme un fichier csv avec les données séparées par une virgule (comma seperated) OK
- Lire les données OK
- Afficher les données OK


"""

import csv
import time
import math

MAX_BUDGET = 100

def show_combinations_number(nb_actions):
    # Calculer le nombre de combinaisons possibles
    somme = 0
    for k in range(0,nb_actions):
        somme += math.factorial(nb_actions)/(math.factorial(k) * math.factorial(nb_actions-k))
    print(f"Nombre d'actions : {nb_actions}")
    print(f"Nombre total de combinaisons possibles : {int(somme)}")

def get_combinations_of_k_elements(elements, k, combinations, start=0, combination=[]):
    if len(combination) == k:
        combinations.append(list(combination))
        return 
    for i in range(start, len(elements)):
        combination.append(elements[i])
        get_combinations_of_k_elements(elements, k, combinations, i + 1, combination)
        combination.pop()

def get_all_combinations(actions, combinations):
    # Les actions sont listées à partir du deuxième élément [1:]
    for k in range(1,len(actions)+1):
        get_combinations_of_k_elements(actions, k, combinations)
    print(f"Nombre total trouvé: {len(combinations)}")

def get_all_combinations_in_budget(combinations, combinations_in_budget):
    for combination in combinations:
        cost = 0
        for action in combination:
            cost += float(action[1])
        if cost <= MAX_BUDGET:
            combinations_in_budget.append(combination)
    print(f"Nombre total dans le budget : {len(combinations_in_budget)}")

def calculate_combinations_profit(combinations_in_budget):
    for combination in combinations_in_budget:
        profit = 0
        for action in combination:
            profit += float(action[1]) * float(action[2])/100
        combination.append(profit)

def show_combination_details(combination):
    total_cost = 0
    for action in combination[:-1]:
        print(f"{action[0]}, coût : {action[1]}")
        total_cost += float(action[1])
    print(f"Coût total : {total_cost}")
    print(f"Profit : {combination[-1]}")

start = time.time()
with open('forcebrute_dataset.csv', newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    actions = []
    for row in reader:
        actions.append(row)
    actions = actions[1:]
    nb_actions = len(actions)

    show_combinations_number(nb_actions)

    combinations = []
    get_all_combinations(actions, combinations)
    
    combinations_in_budget = []
    get_all_combinations_in_budget(combinations, combinations_in_budget)

    calculate_combinations_profit(combinations_in_budget)

    combinations_in_budget.sort(key=lambda x: x[-1], reverse=True)
    show_combination_details(combinations_in_budget[0])
    

    end = time.time()
    print(f"Temps: {end - start}")



