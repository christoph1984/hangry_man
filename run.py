import random

word_list = [
    "Spaghetti", "Guacamole", "Biscotti", "Zucchini", "Tiramisu",
    "Hamburger", "Croissant", "Quesadilla", "Sushi", "Barbecue",
    "Cheesecake", "Risotto", "Pancakes", "Kimchi",
    "Ratatouille", "Falafel", "Gazpacho",
    "Macarons", "Goulash", "Bruschetta"]

tries = 6

guessed_letters = []

chosen_word = random.choice(word_list).lower()

guess_word = ["_"] * len(chosen_word)


def hangryman():
    global chosen_word
    global guess_word
    random_number = random.randint(0, len(word_list)-1)
    chosen_word = word_list[random_number]
    guess_word = []
    for letter in chosen_word:
        guess_word.append("_")

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
print("\nThe word you need to guess has", len(chosen_word), "characters\n")
print(' '.join(guess_word), "\n")
    # tries = 6
    # guessed_letters = []
    # # Debug print statement
    # print("Debug: The chosen word is", chosen_word)


# ASCII hangman art imported from chrishorton (GitHub Gist)
stages = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# print(stages)

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

hangryman()
