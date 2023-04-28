
# This task was done by Mateusz Kielan

def findOccurrences(s, ch):
    """
    Function takes two parameters.
    :param s: string that you want to check.
    :param ch: character that you want to match.

    if there is a match :
        function returns list with the indexes of matche
    if there is no match :
        funtion returns False
    """
    result = [i for i, letter in enumerate(s) if letter == ch]

    if (len(result) == 0):
        return False
    else:
        return result


# here change the word that you want user to guess and number of tries that user has
tries = 6
word = "java"
# making a template for the hame
guess_word = ["_" for i in range(0, len(word))]
used_letters = " "

while True:
    if ("_" in guess_word):

        # print results of every round
        print(f"You have {tries} left.")
        print(f"Used letters: {used_letters}")
        print(f"Word: {' '.join(guess_word)}")
        user_guess = input("Guess a letter: ")
        print(" ")

        used_letters = used_letters + user_guess + " "

        #find if the users letter is in the word
        match = findOccurrences(word, user_guess)

        if (tries > 1):
            if (match):
                # replacing blanks with correctly guessed letters
                for occurence in match:
                    temp = list(guess_word)
                    temp[occurence] = user_guess
                    guess_word = "".join(temp)
            else:
                # if the guess is incorrect reduce number of tries
                tries -= 1
        else:
            print(f"You lost. The word is {word}.")
            break
    else:
        print("Congratulations, you won!")
        break