import csv
import sys
import time

import combinations as cb

MAX_BUDGET = float(sys.argv[2])

filename = sys.argv[1]

start = time.time()

actions = cb.get_actions_from_csv(filename)
nb_actions = len(actions)

cb.show_combinations_number(nb_actions)

combinations = []
cb.get_all_combinations(actions, combinations)

combinations_in_budget = []
cb.get_all_combinations_in_budget(combinations, combinations_in_budget, MAX_BUDGET)

cb.calculate_combinations_profit(combinations_in_budget)

combinations_in_budget.sort(key=lambda x: x[-1], reverse=True)
cb.show_combination_details(combinations_in_budget[0])

cb.execution_time(start)

# Vérifier les floats 
# Intéressant quand on transsforme les données en float dès le début on passe de 14 à 7 secondes
# Nom du fichier sur ligne de commande
# Vérifier si header ?

# Force brute : test de toutes les combinaisons possibles
# Commentaire sur le temps que ça prends et que si nombre d'actions plus longue
# Risque de prendre beaucoup plus de temps

# Logique de l'algo optimisé
# Pas toutes les combinaisons
# Trie de la liste par rapport au bénéfice
# Récupère les actions pourcentage de bééfice éléevé et rentre dans le budget
# Mais au bout d'un moment il ne fait pas attention au pourcentage le plus intéressant 
# Peut être donner l'exemple
# Il donne le meilleur relativement même prix mais légère perte de bénéfice relativement mais gain de temps
# Présenter et analyser
# Big O force brute :
# Big O optimisé :

# Partie 3
# Télécharger les fichiers
# Corriger 
# Comparer résultats avec exécution en optimisé