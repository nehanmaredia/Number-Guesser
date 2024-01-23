import random

total_games_played = 0

while True: 
    min_num = 1
    max_num = 100

    target_number = random.randint(min_num, max_num)

    max_attempts = 10
    attempts = 0

    won = False

    print(f"Welcome to the Number Guessing Game! Guess the number between {min_num} and {max_num}.")
    while attempts < max_attempts:
        attempts += 1
        guess = int(input(f"Attempt {attempts}/{max_attempts}: Enter your guess: "))
        if guess < min_num or guess > max_num:
            print("Invalid guess. Please enter a number within the specified range.")
        elif guess == target_number:
            won = True
            break
        elif guess < target_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

    if won:
        print(f"Congratulations! You guessed the correct number ({target_number}) in {attempts} attempts.")
    else:
        print(f"Sorry, you've run out of attempts. The correct number was {target_number}.")
        total_games_played += 1

    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print(f"Total games played: {total_games_played}")
        print("Thanks for playing!")
        break