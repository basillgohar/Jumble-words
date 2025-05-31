import random

def hangman():
    words = ["ball","basil","python","and","dot","chess"]
    word_to_guess = random.choice(words)
    
    guessed_word = []
    for i in word_to_guess:
        guessed_word.append("_")

    attempts = 0
    max_attempts = 6

    guessed_letter = []
    print(" wellcome to hangman guess the word one letter at a time")
    print("word: "," ".join(guessed_word))

    while attempts < max_attempts and  "_" in guessed_word:
        guess  = input("enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("please enter a single valid letter ")
            continue
        
        if guess in guessed_letter:
            print("you've already guessed it try again")
            continue
        guessed_letter.append(guess)
        

