# Hangman Game in Python

## 1. Project Title
**Hangman Game – Python**

## 2. Project Description
The Hangman Game is a simple text-based game developed using Python. The computer randomly selects a word, and the player tries to guess the word one letter at a time. The player has a maximum of 6 incorrect guesses to find the word.

## 3. Objective
The objective of this project is to practice Python programming concepts such as loops, conditional statements, lists, strings, functions, and random word selection.

## 4. Technologies Used
- Python
- Visual Studio Code (VS Code)
- Git and GitHub

## 5. Step-by-Step Project Development

### Step 1: Set Up the Environment
I installed Python and Visual Studio Code on my laptop. I created a project folder to store the Hangman Game program.

### Step 2: Create the Python File
I created a Python file named `python hangman.py` and wrote the game code in it.

### Step 3: Import the Random Module
I used Python's built-in `random` module to select a random word from a predefined list.

### Step 4: Create a Word List
I created a list containing different words. The computer randomly selects one word whenever the game starts.

### Step 5: Display Hidden Letters
I displayed underscores (`_`) to represent the letters the player needs to guess.

### Step 6: Accept Player Guesses
I used input statements to allow the player to enter one letter at a time.

### Step 7: Check the Guessed Letters
The program checks whether the guessed letter is present in the selected word. If it is correct, the corresponding letter is revealed.

### Step 8: Track Incorrect Guesses
The game allows a maximum of 6 incorrect guesses. Each new incorrect guess reduces the remaining attempts by one. Repeated guesses do not reduce the attempts.

### Step 9: Display Hangman Stages
I created ASCII art stages to show the Hangman figure as the player makes incorrect guesses.

### Step 10: Check Win or Lose
The player wins by guessing all the letters before running out of attempts. If all 6 incorrect attempts are used, the game displays the correct word and a losing message.

### Step 11: Run and Test the Program
I ran the program in the VS Code terminal using Python and tested the game with correct and incorrect guesses.

### Step 12: Upload the Project to GitHub
I used Git to track the project files and uploaded the Hangman Game project to GitHub so that others can view the source code.

## 6. How to Run the Project

1. Install Python on your computer.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Open the terminal.
5. Run the following command:

```bash
python "python hangman.py"
```

## 7. Features
- Random word selection
- Letter-by-letter guessing
- Maximum of 6 incorrect attempts
- ASCII Hangman display
- Duplicate guesses do not reduce attempts
- Win and lose messages

- ## Demo Video

[Click here to Watch Hangman Game Demo Video](https://drive.google.com/file/d/1zXVpmNkDfPibKKm4dK61TDsOgYOo1eVf/view)


## 8. Learning Outcomes
Through this project, I practised Python basics, conditional statements, loops, lists, strings, user input, random selection, and debugging.

## 9. Conclusion
This project helped me improve my Python programming skills by building a simple interactive game. It also gave me practice using VS Code, Git, and GitHub.

## 10. Author
**Gowri Devi**
# Hangman-Game
A Python-based terminal Hangman game featuring random word selection, ASCII gallows art, letter guessing, duplicate guess prevention, and a maximum of 6 incorrect attempts.
