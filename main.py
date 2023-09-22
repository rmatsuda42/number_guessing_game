import random

def get_range():
    """
    Get the start and end values from the user.
    Must be an int
    """
    try:
        start_value = int(input("Please enter start value: "))
        end_value = int(input("Please enter end value: "))
    except ValueError:
        return f"Please enter a valid integer value"
    return start_value, end_value

def get_answer(start_value, end_value):
    """
    Get a random int between start_value and end_value
    """
    return random.randint(start_value, end_value)

def play_game(answer, start_value, end_value, guess_count, remaining_guesses):
    """
    Play the game, user guesses an int, if higher, provide hint, recurse
    if lower, provide hint, recurse
    if == return you win
    """
    user_guess = int(input(f"Please guess a number between {start_value} and {end_value}: "))
    if remaining_guesses == 0:
        print(f"You lose, the correct answer was {answer}")
    elif user_guess > answer:
        print(f"Sorry, {user_guess} is higher than the answer, please try again.\nYou have {remaining_guesses} remaining guesses.")
        user_guess -= 1
        guess_count += 1
        remaining_guesses -= 1
        play_game(answer, start_value, user_guess, guess_count, remaining_guesses)
    elif user_guess < answer:
        print(f"Sorry, {user_guess} is lower than the answer, please try again.\nYou have {remaining_guesses} remaining guesses.")
        user_guess += 1
        guess_count += 1
        remaining_guesses -= 1
        play_game(answer, user_guess, end_value, guess_count, remaining_guesses)
    else:
        if guess_count == 1:
            print(f"You guess it, the answer was {answer} on your first try!!")
        else:
            print(f"You guessed it, the answer was {answer} and you guessed it in {guess_count} tries")

def main():
    print("Welcome to the number_guessing_game")
    start_value, end_value = (get_range())
    answer = get_answer(start_value, end_value)
    remaining_guesses = (end_value - start_value) - 1
    guess_count = 1
    play_game(answer, start_value, end_value, guess_count, remaining_guesses)

if __name__ == "__main__":
    try: 
        main()
    except KeyboardInterrupt:
        print("\nExiting due to keyboard interrupt")