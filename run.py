import random

word_list = ["Spaghetti", "Guacamole", "Biscotti", "Zucchini", "Tiramisu",
                 "Hamburger", "Croissant", "Quesadilla", "Sushi", "Barbecue",
                 "Cheesecake", "Risotto", "Pancakes", "Kimchi",
                 "Ratatouille", "Falafel", "Gazpacho",
                 "Macarons", "Goulash", "Bruschetta"]

tries = 6

guessed_letters = []

chosen_word = random.choice(word_list).lower()

guess_word = ["_"] * len(chosen_word)

def hangryman():
    random_number = random.randint(0, len(word_list)-1)
    chosen_word = word_list[random_number]
    guess_word = []
    for letter in chosen_word:
        guess_word.append("_")
    print("The word you need to guess has", len(chosen_word), "characters")
    print(' '.join(guess_word))
    # tries = 6
    # guessed_letters = []
    # # Debug print statement
    # print("Debug: The chosen word is", chosen_word)


# ASCII hangman art imported from chrishorton (GitHub Gist)
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# print(stages)

while tries > 0:
    print(stages[6-tries])
    print("You have", tries, "tries left")
    guess = input("Guess a letter or the whole word: ")
    if guess in guessed_letters:
        print("You've already guessed this letter.")
        continue
    guessed_letters.append(guess)
    if len(guess) == 1:
        correct_guess = False
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            guess_word[i] = guess
            correct_guess = True
    print(' '.join(guess_word))
    if correct_guess:
        print("Good job! You've guessed a letter correctly.")
    else:
        tries -= 1
        print("Wrong guess. You have", tries, "tries left")

    if len(guess) == len(chosen_word):
        if guess == chosen_word:
            print("Congratulations, you won!")
            break
        else:
            tries -= 1
            print("Wrong guess. You have", tries, "tries left")

    if tries == 0:
            print(stages[6])
            print("You lost! The word was:", chosen_word)

hangryman()
