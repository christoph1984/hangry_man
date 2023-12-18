# Hangry Man Game

Hangry Man is a fun, food-themed version of the classic game Hangman. The game selects a random food-related word, and the player must guess the word one letter at a time.

## Code Explanation

1. **Import necessary modules**: The `random` module is used to select a random word from a list, and the `colorama` module is used to color the text output.

```python
import random
from colorama import Fore, Style, init
```

2. **Initialize colorama**: This is necessary for the colorama module to function properly.
   
```init()```

3. **Set text colour**:
   
```print(Fore.YELLOW)```

4. **Word list**: This is a list of food-related words that the game can choose from.

```
word_list = [
    "Spaghetti", "Guacamole", "Biscotti", "Zucchini", "Tiramisu",
    "Hamburger", "Croissant", "Quesadilla", "Sushi", "Barbecue",
    "Cheesecake", "Risotto", "Pancakes", "Kimchi",
    "Ratatouille", "Falafel", "Gazpacho",
    "Macarons", "Goulash", "Bruschetta"]
```

5. **Game variables**: The `tries` variable keeps track of how many guesses the player has left, `guessed_letters` is a list of letters the player has already guessed, `chosen_word` is the word the player needs to guess (selected randomly from the word list and converted to lowercase), and `guess_word` is a list of underscores representing the letters in the chosen word.

```
tries = 6
guessed_letters = []
chosen_word = random.choice(word_list).lower()
guess_word = ["_"] * len(chosen_word)
```

6. **Hangryman function**: This function resets the `chosen_word` and `guess_word` variables for a new game. It selects a new random word from the word list and creates a new list of underscores for the `guess_word`.

```
def hangryman():
    global chosen_word
    global guess_word
    random_number = random.randint(0, len(word_list)-1)
    chosen_word = word_list[random_number]
    guess_word = []
    for letter in chosen_word:
        guess_word.append("_")
```

7. **Welcome message**: This prints a welcome message and asks the player if they want to see the instructions.

```
print('''
Welcome to Hangry Man, the most delicious hangman game you've ever played!

In this game, your taste buds are put to the test as you guess food-related
words. From appetizers to desserts, cuisines from around the world,
there's a smorgasbord of culinary terms waiting for you.
''')

show_instructions = input("Would you like to see the instructions? (yes/no): ")
if show_instructions.lower() == "yes":
    print('''
Here's how it works:
1. A random food-related word will be chosen, and you'll see a series of
underscores representing each letter in the word.

2. You can guess one letter at a time or try to guess the whole word.
Incorrect guesses will start to build the hangry man.

3. With each wrong guess, our hangry man gets closer to losing his patience.
You have six tries before he loses his cool.

4. If you guess the word correctly before the hangry man is complete, you win!
If not, the hangry man will have to go hungry, and you'll get to know the
correct word.

So, put on your chef's hat, and let's get cooking! Can you guess the word
before the hangry man loses his cool? Good luck, and may the best foodie win!
''')
```

8. **Game loop**: This is the main game loop. It continues as long as the player has tries left. In each iteration, it prints the current state of the hangman, asks the player for a guess, checks if the guess is correct, and updates the game state accordingly. 

```
while tries > 0:
    print("\n", stages[6-tries])
    print("\nYou have", tries, "tries left\n")
    guess = input("Guess a letter or the whole word: ")
    if guess in guessed_letters:
        print("\nYou've already guessed this letter.\n")
        continue
    guessed_letters.append(guess)
    if len(guess) == 1:
        correct_guess = False
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            guess_word[i] = guess
            correct_guess = True
    print(' '.join(guess_word))

    if "_" not in guess_word:
        print("\nCongratulations, you won!\n")
        break
    if correct_guess:
        print("\nGood job! You've guessed a letter correctly.\n")
    else:
        tries -= 1
        print("\nWrong guess. You have", tries, "tries left\n")

    if len(guess) == len(chosen_word):
        if guess == chosen_word:
            print("\nCongratulations, you won!\n")
            break
        else:
            tries -= 1
            print("Wrong guess. You have", tries, "tries left")

    if tries == 0:
        print("\n", stages[6])
        print("\nYou lost! The word was:", chosen_word, "\n")
```

9. **Start the game**: Finally, the `hangryman()` function is called to start the game.

```
hangryman()
```

## Testing

VALIDATOR TESTING
Python code tested and no significant errors shown. Code passed through:

![python_linter_pass](assets/readme_files/python_linter_pass.jpg)

[**CI PYTHON LINTER**](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/) 

### Manual testing results

| Test Case | Steps | Expected Outcome | Status |
| --- | --- | --- | --- |
| Game Initialization | Start the game | The game should print the welcome message and ask if the user wants to see the instructions | Passed |
| Instructions | Enter 'yes' when asked if you want to see the instructions | The game should print the instructions | Passed |
| Word Selection | Start a new game | The game should select a random word from the word list and display the correct number of underscores | Passed |
| Correct Guess | Guess a letter that is in the word | The game should reveal the letter in the correct position(s) | Passed |
| Incorrect Guess | Guess a letter that is not in the word | The game should decrement the number of tries left and display the next stage of the hangman | Passed |
| Repeat Guess | Guess a letter that has already been guessed | The game should inform the user that the letter has already been guessed | Passed |
| Win Game | Correctly guess all the letters in the word | The game should congratulate the user for winning | Passed |
| Lose Game | Make 6 incorrect guesses | The game should inform the user that they lost and reveal the correct word | Passed |







![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
