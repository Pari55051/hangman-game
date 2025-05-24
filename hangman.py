# Hangman Game

# dataset #
word_categories = {
    "animals": [
        "elephant", "giraffe", "kangaroo", "zebra", "alligator",
        "tiger", "lion", "panda", "koala", "rhinoceros"
    ],
    "fruits": [
        "apple", "banana", "mango", "pineapple", "orange",
        "grape", "cherry", "peach", "kiwi", "strawberry"
    ],
    "colors": [
        "red", "blue", "green", "yellow", "purple",
        "orange", "black", "white", "brown", "pink"
    ],
    "countries": [
        "canada", "brazil", "france", "germany", "japan",
        "india", "china", "mexico", "egypt", "australia"
    ],
    "sports": [
        "soccer", "cricket", "tennis", "baseball", "basketball",
        "hockey", "volleyball", "rugby", "golf", "badminton"
    ]
}
# dataset #


import random

# selecting category + word
category = random.choice(list(word_categories.keys()))
word = random.choice(word_categories[category])
# print(f"Category: {category}")
# print(f"Word: {word}")


# start up message display
print("I have chosen a word! Guess it before the man is hanged! You get 6 tries!")
print(f"CATEGORY: {category.upper()}")


# making + displaying the blanks
guess_word = list("_"*len(word))
print(guess_word)

for attempt in range(1, 6+1):
    guess = input("Enter your guess: ").lower()
    for actual in range(0, len(word)):
        for g in range(0, len(guess)):
            if guess[g] == word[actual]:
                guess_word[actual] = guess[g]
    print(guess_word)
    if guess_word == list(word):
        print("You Win!")
        break
    if attempt == 6 and guess_word != list(word):
        print("You Lose!")
