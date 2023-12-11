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
    # Debug print statement
    print("Debug: The chosen word is", chosen_word)
    
hangryman()

