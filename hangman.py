import random
from random_word import RandomWords
r = RandomWords()

# Store words that the computer will use in a list
word_choices = ['test']
# Choose random word from list
# word_to_guess = random.choice(word_choices)
word_to_guess = r.get_random_word()

# Split the letters of the random word into list items
word_to_guess_lst = list(word_to_guess)

board = []

game_on = True


# Function that determines if player has won

def game_over(board, word):
    if ''.join(board) == word_to_guess:
        choice = input('You won!\nPlay again: Y/N: ')
        if choice == 'Y':
            reset_board()
            main_game()
        else:
            return True


# Visual representation of the word spaces on teh command line.

def reset_board():
    board.clear()
    length_of_board = len(word_to_guess)
    for i in range(length_of_board):
        # board_chars = length * '_'
        board.insert(0, '_')


def show_board():
    print(''.join(board))


def main_game():
    chances = 0
    while chances <= 6:
        guess = input("Pick a letter: ")
        if not guess:
            print('Guess cannot be blank.')
        else:
            # Used enumurate and list comprehension to grab  the position of the matches
            positions = [index for index, char in enumerate(word_to_guess) if guess == char]
            if guess in word_to_guess:
                print('Correct!')
                for i in positions:
                    board[i] = guess
            else:
                print('Sorry, try again')
            show_board()
            if game_over(board, word_to_guess):
                break
            chances += 1
    else:
        print(f"Sorry, you ran out of chances.\nThe correct word was {word_to_guess}\nGame over")


reset_board()
main_game()
