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

def play_game(answer, start_value, end_value):
    """
    Play the game, user guesses an int, if higher, provide hint, recurse
    if lower, provide hint, recurse
    if == return you win
    """
    user_guess = int(input(f"Please guess a number between {start_value} and {end_value}: "))
    if user_guess > answer:
        print(f"Sorry, {user_guess} is higher than the answer, please try again")
        user_guess -= 1
        play_game(answer, start_value, user_guess)
    elif user_guess < answer:
        print(f"Sorry, {user_guess} is lower than the answer, please try again")
        user_guess += 1
        play_game(answer, user_guess, end_value)
    else:
        print(f"You guessed it, the answer was {answer}")

def main():
    print("Welcome to the number_guessing_game")
    start_value, end_value = (get_range())
    answer = get_answer(start_value, end_value)
    play_game(answer, start_value, end_value)

if __name__ == "__main__":
    try: 
        main()
    except KeyboardInterrupt:
        print("\nExiting due to keyboard interrupt")