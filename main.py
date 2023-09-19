import random

counter = 0
lineNumber = random.randint(0, 10001)

f = open("words.txt", "r")
words = f.readlines()  # open and read the file

lengthOfWord = len(words[lineNumber])  # find the length of the random word

guessLength = []
for lengthOfWord in words[lineNumber]:  # create necessary lines for the word
    guessLength.append("_")
guessLength.pop()  # there was an extra "_"


print("Lets play Hangman! Your letter is", len(words[lineNumber]), "words long.\n")

userGuess = input("Enter a letter: ")
while counter != 3:
    for i in range(len(words[lineNumber])):
        if words[lineNumber] == userGuess:
            print(i)
            print(" The letter", userGuess, " is there")
        else:
            counter += 1
            print("you have chosen wrong", counter)
            userGuess = input("Enter a letter: ")


print(words[lineNumber])
print(*guessLength)

