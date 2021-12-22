def get_ascii_arts(file='hangman_ascii.txt'):
    arts = []
    with open(file) as art:
        arts = art.readlines()
    art_phases = [arts[art_index:art_index+9] for art_index in range(0, len(arts), 9)]
    return art_phases   


# STEP 1
# display a menu with at least 3 difficulty choices and ask the user
# to select the desired level
#difficulty = "1" sample data, normally the user should choose the difficulty
def ask_level():
    levels = 4
    level = input("Please choose one of the following levels: 1 2 3 4!")
    # generator
    if level in (str(x) for x in range(1, levels)):
        return int(level)
    else:
        return f"The chosen {level} level is not available!"

    

# STEP 2
# based on the chosen difficulty level, set the values 
# for the player's lives
# choose random <- select length lists (by difficulty)
def set_difficulty(level):
    if level == 1:
        word_to_guess = "Cairo" # sample data, normally the word should be chosen from the countries-and-capitals.txtlives = 5 # sample data, normally the lives should be chosen based on the difficulty
        lives = 8
    elif level == 2:
        word_to_guess = "Budapest"
        lives = 7
    elif level == 3:
        word_to_guess = "Albuquerque"
        lives = 6
    else:
        word_to_guess = "Nyugotifelsőszombatfalva"
        lives = 5
        
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
def tried_letters(letter, already_tried_letters):
    if letter in already_tried_letters:
        print('You already tried this letter, try again.')
        return already_tried_letters
    else:
        already_tried_letters.add(letter)
        return already_tried_letters



# STEP 6ters(letter, word_to_guess, lives, already_tried_letters, hangman)
# if the letter is present in the word iterate through all the letters in the variable
# word_to_guess. If that letter is present in the already_tried_letters then display it,
# otherwise display "_".
def present_letters(letter, word_to_guess, already_tried_letters, current_state):
    low_word = word_to_guess.lower()
    if letter in low_word:
        return print_word(word_to_guess, already_tried_letters, current_state)
    else:        
        print('The letter is not present in the word!')
        return print_word(word_to_guess, already_tried_letters, current_state)



def print_word(word_to_guess, already_tried_letters, current_state):
    low_word = word_to_guess.lower()
    tried_valid = set(low_word).intersection(already_tried_letters)
    for i in range(len(word_to_guess)):
            if low_word[i] in tried_valid:
                 current_state += word_to_guess[i] + ' '
            else:
                current_state += '_ '
    print(current_state)
    return tried_valid

# def present_letters(letter, word_to_guess, lives, already_tried_letters, hangman):
#     indexes = []
#     spaced_word_to_guess = " ".join(word_to_guess)
#     for index in range(len(spaced_word_to_guess)):
#         if letter == spaced_word_to_guess[index]:
#             indexes.append(index)
#     printed_word = underlines(word_to_guess)
#     printed_word = list(printed_word)
#     for position in indexes:
#         printed_word[position] = letter
#     printed_word = ''.join(printed_word)
#     return printed_word
#('Please provide only one letter!')

# if the letter is not present in the word decrease the value in the lives variable
# and display a hangman ASCII art. You can search the Internet for "hangman ASCII art",
# or draw a new beautiful one on your own.

def print_hearts(lives):
    hearts = ''
    for i in range(lives):
        hearts = hearts + "♥ "
    print(hearts)


def win_check(word_to_guess, tried_valid):
    low_word = word_to_guess.lower()
    for i in range(len(low_word)):
        if low_word[i] not in tried_valid:
            return False
    print('Congrats, you won! Please play again!')
    return True

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
        print("###################")
        level = ask_level()
        word_to_guess = set_difficulty(level)[0]
        lives = set_difficulty(level)[1]
        win = False
        current_state = ''
        already_tried_letters = set()
        tried = set()
        print(underlines(word_to_guess))
        while lives >= 0 or win == False:
            print_hearts(lives)
            letter = ask_a_letter()
            already_tried_letters = tried_letters(letter, already_tried_letters)
            tried_len = len(tried)
            tried = present_letters(letter, word_to_guess, already_tried_letters, current_state)
            tried_len2 = len(tried)
            if tried_len == tried_len2:
                lives -= 1
            print (''.join(get_ascii_arts()[lives]))       
            win = win_check(word_to_guess, tried)
            print(win)
            
        if lives <= 0:
            print('Game over! Play again!')

hangman_controller()
