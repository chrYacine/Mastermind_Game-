import random  as rd
#import time
# Etape 1 : Création de la fonction pour générer une combinaison 
def generate_secret_combination(size=4, values=['1', '2', '3', '4', '5', '6']):
    """Génère une combinaison secrète aléatoire."""
    return [rd.choice(values) for _ in range(size)]
#####
# secret_combination = generate_secret_combination()
# print("Combinaison secrète générée (aléatoire) :", secret_combination)

#Etape 3 : Interation joueur
def get_player_guess(size=4, values=['1', '2', '3', '4', '5', '6']):
    """Demande au joueur une combinaison valide."""
    while True:
        player_input = input(f"Entrez une combinaison de {size} chiffres parmi {values} (ex: 1234) : ")
        if len(player_input) == size and all(char in values for char in player_input):
            return list(player_input)
        print("Entrée invalide. Veuillez réessayer.")
# ##### Test
# player_guess = get_player_guess()
# print("Proposition du joueur :", player_guess)
# Etape 4 : Evaluation de la proposition
def check_guess(proposed_combination, secret_combination):
    """Verifie la combinaison et retourne les indices."""
    correct_positions = sum(p == s for p, s in zip(proposed_combination, secret_combination))
    incorrect_positions = sum(min(proposed_combination.count(value), secret_combination.count(value)) for value in set(proposed_combination)) - correct_positions
    return correct_positions, incorrect_positions
### Test 
# test_secret = ['1', '2', '3', '4']
# test_guess = ['1', '3', '2', '5']
# result = check_guess(test_guess, test_secret)
# print("Reultat pour la tentative :", result)  

#Etape 5 : Boucle de jeu

def mastermind():
    """Boucle principale du jeu Mastermind."""
    combination_size = 4
    possible_values = ['1', '2', '3', '4', '5', '6']
    max_attempts = 10

    print("Bienvenue dans le jeu Mastermind !")
    secret_combination = generate_secret_combination(combination_size, possible_values)

    for attempt_number in range(1, max_attempts + 1):
        print(f"\nTentative {attempt_number}/{max_attempts}")
        player_guess = get_player_guess(combination_size, possible_values)

        correct_positions, incorrect_positions = check_guess(player_guess, secret_combination)

        print(f"Résultat : {correct_positions} bien placé(s), {incorrect_positions} mal placé(s).")

        if correct_positions == combination_size:
            print("\nBravo ! Vous avez deviné la combinaison secrète.")
            return

    print(f"\nDommage ! Vous avez épuisé vos essais. La combinaison était : {''.join(secret_combination)}")