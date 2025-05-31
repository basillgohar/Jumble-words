import random
word_list = ["basil","jet_learn","python","computer","machine","pakistan","sweden"]

def jumble_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return " ".join(word_list)   

def get_hint(word):
    return "the first letter of the word is: {}".format(word[0].upper()) 

def play_game():
    score = 0 
    rounds = 5
    print("wellcome to jumble word")
    for i in range(1,rounds+1):
        word = random.choice(word_list)
        scrambled_words = jumble_word(word)
        print ("round {}".format(i))
        print("here is a jumble word {}".format(scrambled_words))
        
        hint = input("do you want  a hint? yes/no ").lower()
        if hint == "yes":
            print(get_hint(word))
    
        guess = input("guess the original word: ").lower()
        
        while not guess .isalpha():
            print("please enter a vaild word")
            
            guess = input("guess the original word: ").lower()
        
        
        if guess == word:
            print("you guessed corractly!!! ")
            score += 1 

        else: 
            print("you got it wrong :( the awnser was {}".format(word))

    print("game over your final score is {}/{}".format(score,rounds))

play_game()

""" FORMAT ____F-STRING ____ CONCATENATION
age = 36
txt = f"My name is John, I am {age}"

#txt = "my name is BAsil " , "i am " , age , "years old"

print(txt)

# FORMAT and f-strings
country= input("enter the name of your country:")
s = "Hello , I am from {}".format(country)

"""

