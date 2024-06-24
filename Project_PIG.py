import random

print("test")

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")

    else:
        print("Invalid , try agin.")

max_score = 50
players_score = [0 for _ in range(players)]

while max(players_score) < max_score:

    for player_idx in range(players):
        print("\nPlayer number" , player_idx + 1, "turn has jest started!\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)?")
            if should_roll.lower() != "y":  # lower เป็นการทำให้ตัวอักษรเป็นตัวเล็กทั้งหมด
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)

            print("You score is", current_score)

        players_score[player_idx] += current_score
        print("Your total score is:", players_score[player_idx])