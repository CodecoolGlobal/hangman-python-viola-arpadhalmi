import random

def read_file(file):
    l = []
    with open(file) as f:
        l = f.readlines()
    return l

def get_ascii_arts(file='hangman_ascii.txt'):
    arts = read_file(file)
    art_phases = [arts[art_index:art_index+9] for art_index in range(0, len(arts), 9)]
    return art_phases
  
def get_countries(file='countries-and-capitals.txt'):
    cc = read_file(file)
    countries = [country.split("|")[0][:-1] for country in cc]
    cities = [country.split("|")[1][1:-1] for country in cc]
    return countries, cities

 
# STEP 1
# display a menu with at least 3 difficulty choices and ask the user
# to select the desired level
#difficulty = "1" sample data, normally the user should choose the difficulty
def ask_level():
    levels = 4
    while True:
        level = input('''Please choose one of the following levels: 
        1 - guess a country
        2 - guess a capital 
        3 - guess a country with it's capital!
        ''')
        # generator
        if level.isnumeric():
            if level in (str(x) for x in range(1, levels)):
                return int(level)
            else:
                print(f"The chosen {level} level is not available!")
        else:
            print('Please provide a number between 1-3!')

    

# STEP 2
# based on the chosen difficulty level, set the values 
# for the player's lives
# choose random <- select length lists (by difficulty)
def set_difficulty(level):
    lists = get_countries()
    index = random.randint(0, len(lists[0]))
    if level == 1:
        word_to_guess =  lists[0][index] # sample data, normally the word should be chosen from the countries-and-capitals.txtlives = 5 # sample data, normally the lives should be chosen based on the difficulty
        lives = 8
    elif level == 2:
        word_to_guess = lists[1][index]
        lives = 7
    elif level == 3:
        word_to_guess = lists[0][index] + ' | ' + lists[1][index]
        lives = 6
        
    return (word_to_guess, lives)


# STEP 3
# display the chosen word to guess with all letters replaced by "_"
# for example instead of "Cairo" ddef get     isplay "_ _ _ _ _"
def underlines(word):
    secret_word = ''
    for letter in word:
        if letter == ' ':
            secret_word = secret_word + letter
        elif letter == '-':
             secret_word = secret_word + letter + " "
        elif letter == '|':
            secret_word = secret_word + letter
        else:
            secret_word = secret_word + "_ "
    secret_word = secret_word[0:-1]
    return secret_word

# STEP 4
# ask the user to type a letter
# here you should validate if the typed letter is the word 
# "quit", "Quit", "QUit", "QUIt", "QUIT", "QuIT"... you get the idea :)
# HINT: use the upper() or lower() built-in Python functions
def ask_a_letter():
    while True:
        letter = input('Guess a letter!')
        letter_lowercase = letter.lower()
        if letter.isalpha():
            if letter_lowercase == 'quit':
                print('Thanks for playing, goodbye.')
                exit()
            elif len(letter_lowercase) > 1:
                print('Please provide only one letter!')
            else:
                return letter_lowercase
        else:
            print(f"Sry, but {letter} is not a letter!")


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
        print('Correct guess!')
        return print_word(word_to_guess, already_tried_letters, current_state)
    else:
        tried_invalid = already_tried_letters - print_word(word_to_guess, already_tried_letters, current_state)        
        print('\nThis letter is not present in the word! Already tried wrong letters: ' + ', '.join(tried_invalid))
        return print_word(word_to_guess, already_tried_letters, current_state)


def print_word(word_to_guess, already_tried_letters, current_state):
    low_word = word_to_guess.lower()
    tried_valid = set(low_word).intersection(already_tried_letters)
    for i in range(len(word_to_guess)):
        if word_to_guess[i] == ' ':
            current_state +=  ' '
        elif word_to_guess[i] == '-':
            current_state +=  "-"
        elif word_to_guess[i] == '|':
            current_state +=  "|"
        elif low_word[i] in tried_valid:
            current_state += word_to_guess[i] + ' '
        else:
            current_state += '_ '
    print(current_state)

    return tried_valid

# if the letter is not present in the word decrease the value in the lives variable
# and display a hangman ASCII art. You can search the Internet for "hangman ASCII art",
# or draw a new beautiful one on your own.

def print_hearts(lives):
    hearts = ''
    for i in range(lives):
        hearts = hearts + "♥ "
    print('\nRemaining lives: ' + hearts + '\n')


def win_check(word_to_guess, tried_valid):
    #low_word = (word_to_guess.lower()).alpha()
    alpha_word =  [letter.lower() for letter in word_to_guess if letter.isalpha()]
    low_word = ''.join(alpha_word)
    for i in range(len(low_word)):
        if low_word[i] not in tried_valid:
            return False
    print('#################\nCongrats, you won! Please play again!')
    return True

# STEP 7return 
# check if the variable already_tried_letters already contains all the letters necessary
# to build the value in the variable word_to_guess. If so display a winning message and exit
# the app.
# If you still have letters that are not guessed check if you have a non negative amount of lives
# left. If not print a loosing message and exit the app.
# If neither of the 2 conditions mentioned above go back to STEP 4
ascii_game_over = ''.join(read_file('game_over.txt'))
ascii_start_hangman = ''.join(read_file('hangman_start.txt'))

def hangman_controller():
    print(ascii_start_hangman)
    while True:
        level = ask_level()
        word_to_guess = set_difficulty(level)[0]
        lives = set_difficulty(level)[1]
        win = False
        current_state = ''
        already_tried_letters = set()
        tried = set()
        print(underlines(word_to_guess))
        while lives > 0 and win == False:
            print_hearts(lives)
            letter = ask_a_letter()
            already_tried_letters = tried_letters(letter, already_tried_letters)
            tried_len = len(tried)
            tried = present_letters(letter, word_to_guess, already_tried_letters, current_state)
            tried_len2 = len(tried)
            if tried_len == tried_len2:
                lives -= 1
            print(''.join(get_ascii_arts()[lives]))       
            win = win_check(word_to_guess, tried)           
        
        if lives <=0:
            print(f'{ascii_game_over}\n The word was: {word_to_guess} \n Try again! \n')

hangman_controller()


