# blackjack_game
Blackjack Game in Python


# Blackjack Game in Python

Welcome to our Python-based Blackjack game! This is a simple text-based version of the classic card game. In this game, you play against the computer, aiming to get a hand value as close to 21 as possible without going over.

### Contents
1. [Overview](#overview)
2. [Rules of Blackjack](#rules-of-blackjack)
3. [Code Structure](#code-structure)
4. [How to Run the Game](#how-to-run-the-game)
5. [Understanding the Code](#understanding-the-code)
6. [Potential Improvements](#potential-improvements)

---

### Overview
This Python program was created to help beginners practice coding, conditionals, functions, and loops in Python. The game is simple, text-based, and uses `random` to deal cards and create unpredictable rounds.

### Rules of Blackjack
- You start with two cards and so does the computer.
- Your goal is to get your hand as close to 21 as possible without going over.
- If you or the computer get exactly 21 with the first two cards (an Ace and a 10, Jack, Queen, or King), it’s called a "Blackjack" and is an automatic win.
- You can "hit" to take another card or "pass" to keep your current hand.

### Code Structure
The game code is organized into two main functions:

1. **`play_blackjack()`**: Contains the game logic, handles the rules, and tracks the player's and computer's hands.
2. **`choice_play_main()`**: This function loops to ask the player if they want to play another round.

### How to Run the Game
1. Ensure you have Python installed on your computer.
2. Save the game code into a file named `blackjack.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory where `blackjack.py` is saved.
5. Run the game by typing:
    ```bash
    python blackjack.py
    ```
6. Follow the on-screen instructions to play.

### Understanding the Code

#### Imports and Card Values
The game begins by importing the `random` module and defining a list `cards` containing values for a standard deck, where:
- 11 represents an Ace (which can be worth either 11 or 1).
- 10 is used four times to represent 10, Jack, Queen, and King.

```python
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
```

#### `play_blackjack()` Function
This function handles:
- Dealing initial hands.
- Checking for Blackjack.
- Asking the player if they want to take another card or pass.
- Calculating the total card values and determining the winner.

1. **Initial Deal**: Each player gets two random cards from the `cards` list.
2. **Blackjack Check**: Both the player and computer check for an automatic win with Blackjack (11 + 10).
3. **Player Actions**: The player chooses whether to "hit" (take another card) or "pass" (keep current hand).
4. **Computer Actions**: The computer takes cards until reaching 17 or higher.
5. **End of Round**: The program prints the final scores and displays the result (win, lose, or draw).

```python
def play_blackjack():
    # Game setup and logic code here...
```

#### `choice_play_main()` Function
This function runs the game loop. It asks the player if they want to play a game and will repeatedly run `play_blackjack()` until the player decides to stop.

```python
def choice_play_main():
    should_continue = True
    while should_continue:
        choice_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if choice_play == "y":
            play_blackjack()
        elif choice_play == "n":
            print("We are sad to see you go 😊, play with us next time\nBye!! 👋")
            should_continue = False
```

### Potential Improvements
This simple game can be expanded in several ways:
- Allow betting and a points system.
- Add multiple players.
- Improve the graphics and user interface.

---

With this README file, you should have a good understanding of how to play the game, what each part of the code does, and potential ways to improve it as you learn more Python! Enjoy your Blackjack game!
