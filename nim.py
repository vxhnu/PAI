import random

def print_piles(piles):
    print("Current piles:")
    for i, pile in enumerate(piles):
        print(f"Pile {i + 1}: {pile}")

def nim_game():
    num_piles = random.randint(2, 5)
    piles = [random.randint(1, 10) for _ in range(num_piles)]

    print("Welcome to Nim!")
    print("In this game, there are several piles of stones.")
    print("Players take turns removing stones from one pile at a time.")
    print("The player who removes the last stone wins.")

    current_player = 1

    while True:
        print_piles(piles)
        pile_index = int(input(f"Player {current_player}, choose a pile (1-{num_piles}): ")) - 1
        while pile_index < 0 or pile_index >= num_piles:
            pile_index = int(input("Invalid pile. Choose a pile (1-{num_piles}): ")) - 1

        stones_to_remove = int(input("How many stones do you want to remove: "))
        while stones_to_remove <= 0 or stones_to_remove > piles[pile_index]:
            stones_to_remove = int(input("Invalid number of stones. How many stones do you want to remove: "))

        piles[pile_index] -= stones_to_remove

        if all(pile == 0 for pile in piles):
            print(f"Player {current_player} wins!")
            break

        current_player = 2 if current_player == 1 else 1

if __name__ == "__main__":
    nim_game()