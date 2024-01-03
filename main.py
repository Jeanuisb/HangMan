import secrets


def main():

    secret_word = get_random_word()
    print(secret_word)

    correct_letters = ["_"] * (len(secret_word) - 1)
    missed_letters = []


    while True:
        print("cl: ", ''.join(correct_letters))
        print("sw: ", secret_word)

        display_board(missed_letters, correct_letters)

        guess = get_guess()

        if guess in missed_letters or guess in correct_letters:
            print("You already guessed that letter!")
            continue

        if guess in secret_word:
            correct_letters = update_board(guess, secret_word, correct_letters)
        else:
            missed_letters = update_missed(guess, missed_letters)

        if check_win(correct_letters, secret_word):
            break

    print("You win!")
    print("The word was", secret_word)



def get_random_word():
    f = open("words.txt", "r")
    words = f.readlines()  # open and read the file

    random_word = secrets.SystemRandom().choice(words)

    return random_word


def display_board(missed_letters, correct_letters):
    print("Missed letters:", end=" ")
    for letter in missed_letters:
        print(letter, end=" ")
    print()

    for letter in correct_letters:
        print(letter, end=" ")
    print()


def get_guess():
    while True:
        char_guess = input("Guess a letter: ")
        if len(char_guess) == 1:
            return char_guess
        print("Please only enter one character: ")


def check_guess(guess, word):
    if guess in word:
        return True


def update_missed(guess, missed_letters):
    if guess not in missed_letters:
        missed_letters.append(guess)
    return missed_letters


def update_board(guess, secret_word, correct_letters):
    for i in range(len(secret_word)):
        if guess == secret_word[i]:
            correct_letters[i] = guess
    return correct_letters


def check_win(correct_letters, secret_word):
    if ''.join(correct_letters).__eq__(secret_word):
        return True



if __name__ == "__main__":
    main()
