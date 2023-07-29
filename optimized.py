# Le programme ne doit plus explorer toutes les combinaisons 

import csv
import time
import math

MAX_BUDGET = 500

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
    for k in range(len(actions)+1,1,-1):
        get_combinations_of_k_elements(actions, k, combinations)

    print(f"Nombre total trouvé: {len(combinations)}")

start = time.time()
with open('forcebrute_dataset.csv', newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    
    actions = []
    next(reader)
    for row in reader:
        row[1] = float(row[1])
        row[2] = float(row[2])
        actions.append(row)
    nb_actions = len(actions)
    for action in actions:
        action.append(float(action[1]) * float(action[2])/100)

    # Sort by profit column
    actions.sort(key=lambda x: x[2],reverse=True)
    print("--------Liste des actions---------")

    for action in actions:
        print(action)

    print("--------Meilleure liste des actions---------")

    total_cost = 0
    total_profit = 0
    i = 0
    selected_actions = []
    while total_cost <= MAX_BUDGET and i <= nb_actions-1:
        if total_cost + actions[i][1] <= MAX_BUDGET:
            total_cost += actions[i][1]
            total_profit += actions[i][3]
            selected_actions.append(actions[i])
            i += 1
        else:
            i += 1
            
    for action in selected_actions:
        print(action)
    print(f"Coût total : {total_cost}")
    print(f"Profit total : {total_profit}")
    end = time.time()
    print(f"Temps: {end - start}")