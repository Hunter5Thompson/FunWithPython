import random
import hangman_art
import hangman_words
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def hint():
    print("Here's a hint: " + chosen_word[:2] + "...")

def play_game():
    global lives
    global display
    global guessed_letters
    global chosen_word
    lives = 6
    word_list = hangman_words.word_list
    chosen_word = random.choice(word_list)
    stages = hangman_art.stages
    logo = hangman_art.logo
    win = hangman_art.win
    lose = hangman_art.loose
    display = ["_"] * len(chosen_word)
    guessed_letters = []

    print(logo)
    hint_prompt = True
    while "_" in display and lives > 0:
        clear_screen()
        print(stages[lives])
        print(" ".join(display))
        print("Guessed letters: " + " ".join(guessed_letters))
        if hint_prompt:
            hint_choice = input("Do you want a hint? (y/n): ").lower
            if hint_choice == 'y':
                hint()
                hint_prompt = False
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            if guess in chosen_word:
                print("You already guessed that letter, it is correct")
            else:
                print("You already guessed that letter, but it is not in the word.")
            continue
        guessed_letters.append(guess)
        if guess in chosen_word:
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    display[i] = guess
        else:
            lives -= 1

    if "_" not in display:
        clear_screen()
        print("Congratulations! You have won!")
        print(win)
    else:
        clear_screen()
        print("You have run out of lives. Better luck next time!")
        print(lose)
    print(stages[lives])
    while True:
        replay = input("Do you want to play again? (y/n) ").lower()
        if replay == 'y':
            hint_prompt = True # reset hint_prompt for the next game
            play_game()
            break
        elif replay == 'n':
            print("Thanks for playing!")
            break
        else:
            print("Please enter y or n")

play_game()



