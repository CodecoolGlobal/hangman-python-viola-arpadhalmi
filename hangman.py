# STEP 1
# display a menu with at least 3 difficulty choices and ask the user
# to select the desired level
difficulty = "1" # sample data, normally the user should choose the difficulty
def ask_level():
    level = input("Please choose one of the following levels: 1 2 3 4!")
    if level in ["1", "2", "3", "4"]:
        return int(level)
    else:
        return f"The chosen {level} level is not available!"

    

# STEP 2
# based on the chosen difficulty level, set the values 
# for the player's lives
def set_difficulty(level):
    if level == 1:
        word_to_guess = "Cairo" # sample data, normally the word should be chosen from the countries-and-capitals.txtlives = 5 # sample data, normally the lives should be chosen based on the difficulty
        lives = 10
    if level == 2:
        word_to_guess = "Budapest"
        lives = 8
    if level == 3:
        word_to_guess = "Albuquerque"
        lives = 7
    else:
        word_to_guess = "Nyugotifelsőszombatfalva"
        lives = 6
        
    return (word_to_guess, lives)


# STEP 3
# display the chosen word to guess with all letters replaced by "_"
# for example instead of "Cairo" display "_ _ _ _ _"
def underlines(word):
    secret_word = ''
    for letter in word:
        secret_word = secret_word + "_ "
    secret_word = secret_word[0:-1]
    return secret_word

# STEP 4
# ask the user to type a letter
# here you should validate if the typed letter is the word 
# "quit", "Quit", "QUit", "QUIt", "QUIT", "QuIT"... you get the idea :)
# HINT: use the upper() or lower() built-in Python functions
def ask_a_letter():
    #word_lowercase = word_to_guess.lower()
    while True:
        letter = input('Guess a letter!')
        try:
            letter_lowercase = letter.lower()
        except ValueError:
            return f"Sry, but {letter} is not a letter!"
            
        if letter_lowercase == 'quit':
            print('Thanks for playing, goodbye.')
            exit()
        elif len(letter_lowercase) > 1:
            print('Please provide only one letter!')
        else:
            return letter_lowercase


# STEP 5
# validate if the typed letter is already in the tried letters
# HINT: search on the internet: `python if letter in list`
# If it is not, than append to the tried letters
# If it has already been typed, return to STEP 5. HINT: use a while loop here
def tried_letters():
    already_tried_letters = [] # this list will contain all the tried letters
    while True:
        guess = ask_a_letter()
        if guess in already_tried_letters:
            print('You already tried this letter, try again.')
        else:
            already_tried_letters.append(guess)
            return already_tried_letters



# STEP 6
# if the letter is present in the word iterate through all the letters in the variable
# word_to_guess. If that letter is present in the already_tried_letters then display it,
# otherwise display "_".
def present_letters(letter, word_to_guess, lives):
    secret_word = underlines(word_to_guess)
    word_to_guess = " ".join(word_to_guess)
    if already_tried_letters(letter) == False:
        if letter in word_to_guess:
            for index in range(len(word_to_guess)):
                if letter == word_to_guess[index]:
                    secret_word[index] = letter
            return secret_word
        else:
            lives -= 1
            return (lives, secret_word, hangman)
    else:
        already_tried_letters(letter)
        return secret_word

# if the letter is not present in the word decrease the value in the lives variable
# and display a hangman ASCII art. You can search the Internet for "hangman ASCII art",
# or draw a new beautiful one on your own.



# STEP 7
# check if the variable already_tried_letters already contains all the letters necessary
# to build the value in the variable word_to_guess. If so display a winning message and exit
# the app.
# If you still have letters that are not guessed check if you have a non negative amount of lives
# left. If not print a loosing message and exit the app.
# If neither of the 2 conditions mentioned above go back to STEP 4
def hangman_controller():
    print('Welcome to Kiakasztó.')
    while True:
        level = ask_level()
        set_difficulty(level)