# Space Man - By: Noah Woodward for my CS 1.1 Class 

import random

secret_word = ""
easy_words = ["dog","cat","hat","bat","mat","tap","jam","pen","new","old","that","trap","stack","rat","eat","dance","hand","stand","land"]
hard_words = ["fjord","gypsy","dwarves","ivory","jinx","kayak","kiosk","pixel","polka","unzip","yacht","swivel","rogue","zealous","zippy","oxygen","hyphen","fervid"]

def pickDifficulty(): 
    while True:
        difficulty_level = raw_input("Type easy or hard to set your spaceman difficulty: ")
        if difficulty_level.lower() not in ("easy","hard"):
            print("Not an appropriate choice.")
        else:
            return difficulty_level
def pick_random_word(difficuly_level): 
   
    if difficuly_level == "easy":
        return random.choice(easy_words)
    else: 
        return random.choice(hard_words)

        
def play_game(secret_word):
    incorrect_guesses = 7
    incorrect_bank = "Guessed: "
    guessed_list = []
    actual_word_list = []
    blank_board = draw_board(secret_word)
    
    for letter in blank_board:
        guessed_list.append("_")
    blank_board = ""
  
    for letter in secret_word:
        actual_word_list.append(letter)
  
    for elements in guessed_list: 
        blank_board += " _ "
    print(blank_board)

    while guessed_list != actual_word_list and incorrect_guesses != 0:
         guess = raw_input("Guess a letter from a to z: ")
         display_word = ""
         if guess in secret_word:
            index = secret_word.find(guess)
            guessed_list[index] = guess
            for items in guessed_list:
                display_word += " " + items
            print(display_word)
         else:
            incorrect_guesses -= 1 
            incorrect_bank += guess
            print("Thats wrong!")
            print("You have " + str(incorrect_guesses) + " incorrect guesses left.")
            print(incorrect_bank)

    if(guessed_list == actual_word_list):
        print("You Won! Congratz!")
    else: 
        print("Im sorry, you lost!")
        print("The word was: " + secret_word)




   
    
 



   



def draw_board(secret_word):
     initial_board = ""
     for letters in secret_word:
         initial_board += "_"
     
     return initial_board 

def display(display_text): 
    print(display_text)




def test(): 
    difficulty = pickDifficulty()
    secret_word = pick_random_word(difficulty)
    play_game(secret_word)
    

test()

    