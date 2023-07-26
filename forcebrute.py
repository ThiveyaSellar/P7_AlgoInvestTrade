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


def get_combinations_of_k_elements(elements, k, combinations, start=0, combination=[]):
    if len(combination) == k:
        combinations.append(list(combination))
        return 
    for i in range(start, len(elements)):
        combination.append(elements[i])
        get_combinations_of_k_elements(elements, k, combinations, i + 1, combination)
        combination.pop()

MAX_BUDGET = 100

start = time.time()
with open('forcebrute_dataset.csv', newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    actions = []
    for row in reader:
        actions.append(row)
    
    # Calculer toutes les combinaisons possibles
    combinations = []
    # Les actions sont listées à partir du deuxième élément [1:]
    for k in range(1, len(actions[1:]) + 1):
        get_combinations_of_k_elements(actions[1:], k, combinations)
    print(f"Nombre total : {len(combinations)}")
    # Garder les combinaisons ou le coût total est dans le budget
    combinations_in_budget = []
    for combination in combinations:
        cost = 0
        for action in combination:
            cost += float(action[1])
        #print(cost)
        if cost <= MAX_BUDGET:
            #print("ok")
            combinations_in_budget.append(combination)
        else:
            pass
            #print("nop")
    print(f"Nombre total dans le budget : {len(combinations_in_budget)}")
    end = time.time()
    print(f"Temps: {end - start}")






