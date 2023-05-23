import random

def hangman():
    word_list = ['python', 'hangman', 'game', 'programming', 'openai']
    chosen_word = random.choice(word_list)
    guessed_letters = []
    tries = 5
    
    while tries > 0:
        word_status = ""
        for letter in chosen_word:
            if letter in guessed_letters:
                word_status += letter
            else:
                word_status += "_"
        
        if word_status == chosen_word:
            print("Congratulations! You guessed the word:", chosen_word)
            return
        
        print("Word:", word_status)
        print("Tries remaining:", tries)
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in chosen_word:
            print("Correct guess!")
            guessed_letters.append(guess)
        else:
            print("Wrong guess!")
            tries = tries - 1  # Decrease the try count
            guessed_letters.append(guess)
        
        print("-------------")
    
    print("Game over! The word was:", chosen_word)

hangman()
