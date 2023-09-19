import random
import string


# def get_guess():
# check_guess(guess, word)
# update_missed(guess, missed_letters):
# update_board(guess, secret_word, correct_letters):
# check_win(correct_letters, secret_word):


def main():
    print(get_random_word())


def get_random_word():
    f = open("words.txt", "r")
    words = f.readlines()  # open and read the file

    random_word = random.choice(words)

    return random_word


def display_board(missed_char, correct_char):
    m_char = []
    c_char = []

    for char in missed_char:
        m_char.append(char)

    for char in correct_char:
        c_char.append(char)

    return m_char, c_char


def get_guess():
    while True:
        char_guess = input("Guess a letter")
        if len(char_guess) == 1:
            return char_guess
        print("Please only enter one character")


def check_guess(guess, word):
    if guess in word:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
