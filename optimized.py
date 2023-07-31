import csv
import sys
import time

import combinations as cb

MAX_BUDGET = float(sys.argv[2])

filename = sys.argv[1]

start = time.time()

actions = cb.get_actions_from_csv(filename)
nb_actions = len(actions)

for action in actions:
    action.append(action[1]*action[2]/100)

# Trier par le profit
actions.sort(key=lambda x: x[2],reverse=True)

i = 0
total_cost = 0
total_profit = 0
selected_actions = []

while total_cost <= MAX_BUDGET and i <= nb_actions-1:
    if total_cost + actions[i][1] <= MAX_BUDGET:
        total_cost += actions[i][1]
        total_profit += actions[i][3]
        selected_actions.append(actions[i])
    i += 1
        
print(f"Nombre d'actions au total : {nb_actions}")
print(f"Nombre d'actions sélectionnées au total : {len(selected_actions)}")
for action in selected_actions:
    print(action)
print(f"Coût total : {total_cost}")
print(f"Profit total : {total_profit}")

cb.execution_time(start)
    