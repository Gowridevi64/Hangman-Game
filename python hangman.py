
import random

# List of secret words
words = [
    "python",
    "computer",
    "developer",
    "programming",
    "hangman",
    "database",
    "project",
    "software",
    "keyboard",
    "internet"
]

# ASCII gallows stages: 0 to 6 wrong guesses
stages = [
    """
     +---+
     |   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]

# Select a random secret word
secret_word = random.choice(words).upper()

# Track guessed letters
guessed_letters = set()
wrong_guesses = 0
max_attempts = 6

print("=" * 35)
print("       WELCOME TO HANGMAN")
print("=" * 35)
print("Guess the hidden word letter by letter.")
print("You have 6 incorrect attempts.")
print()

# Main game loop
while wrong_guesses < max_attempts:

    # Display gallows
    print(stages[wrong_guesses])

    # Display hidden word
    display_word = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )

    print("Word:", display_word)
    print("Guessed letters:", " ".join(sorted(guessed_letters)))
    print("Attempts left:", max_attempts - wrong_guesses)

    # Get user input
    guess = input("Enter a letter: ").strip().upper()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.\n")
        continue

    # Prevent duplicate guesses
    if guess in guessed_letters:
        print("You already guessed that letter. Try another!\n")
        continue

    guessed_letters.add(guess)

    # Check the guess
    if guess in secret_word:
        print("Correct guess!\n")
    else:
        wrong_guesses += 1
        print("Wrong guess!\n")

    # Check victory
    if all(letter in guessed_letters for letter in secret_word):
        print("=" * 35)
        print("       CONGRATULATIONS!")
        print("       YOU WIN!")
        print("The word was:", secret_word)
        print("=" * 35)
        break

# Check defeat
if wrong_guesses == max_attempts:
    print(stages[wrong_guesses])
    print("=" * 35)
    print("       GAME OVER!")
    print("The correct word was:", secret_word)
    print("=" * 35)
