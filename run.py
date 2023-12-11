import random

def hangryman():
    word_list = ["Spaghetti", "Guacamole", "Biscotti", "Zucchini", "Tiramisu",
                 "Hamburger", "Croissant", "Quesadilla", "Sushi", "Barbecue", 
                 "Cheesecake", "Risotto", "Pancakes", "Kimchi",
                 "Ratatouille", "Falafel", "Gazpacho",
                 "Macarons", "Goulash", "Bruschetta"]

    random_number = random.randint(0, len(word_list)-1)
    chosen_word = word_list[random_number]
    guess_word = []
    for letter in chosen_word:
        guess_word.append("_")
    print("The word you need to guess has", len(chosen_word), "characters")
    print(' '.join(guess_word))
    tries = 6
    guessed_letters = []
  
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

print(stages)

hangryman()

