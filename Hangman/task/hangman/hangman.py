import random


# This function cypher the word with symbol '-'
def cypher_word(word):
    list_letters = [i for i in word]
    for i in range(0, len(list_letters)):
        list_letters[i] = "-"
    return list_letters


# The function Open one letter in the cyphered word
def decypher_word(list, letter, correct):
    if letter not in set(correct):
        return False
    for i in range(len(list)):
        if correct[i] == letter:
            list[i] = letter
    return True


# The function check the correct style of letter
def check_input(_input, set_of_input_letters):
    if _input in set_of_input_letters:
        print("\nYou've already guessed this letter.")
        return False
    if len(_input) == 1:
        if not _input.islower() or not _input.isalpha():
            print("\nPlease, enter a lowercase letter from the English alphabet.")
            return False
        set_of_input_letters.add(_input)
        return True
    else:
        print("\nPlease, input a single letter.")
        return False


# First initializing variable  by empty values
correct_list = []  # Saves list of words, where we can take random word for guessing
correct_word = ""  # Saves chosen word for guessing
# correct_word = correct_list[0] # Just for testing, it should be deleted after
cypher_list = []  # Saves cyphered word, like a list
count_lives = 0  # Number of attempts for guessing the word in the round of the game
set_of_input_letters = set()  # Saves all the letters-attempts which were entered in the round
wins = 0  # Saves number of wins of all rounds the game
losts = 0  # Saves number of losts of all rounds the game

# Start execution here
print("H A N G M A N")
input_menu = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: > ')

# Main execution block
while input_menu != "exit":  # If not input"exit " then quit from the program, otherwise we are in the game
    if input_menu == "play":  # If input "play", start playing

        correct_list = ["python", "java", "swift", "javascript"]
        correct_word = random.choice(correct_list)
        cypher_list = cypher_word(correct_word)
        count_lives = 8
        set_of_input_letters = set()

        # Main Loop for talking to user about attempts
        while count_lives > 0:
            print("\n" + "".join(cypher_list))
            input_letter = input("Input a letter: >")
            if check_input(input_letter, set_of_input_letters) == False:
                continue

            if not decypher_word(cypher_list, input_letter, correct_word):
                print("\nThat letter doesn't appear in the word.")
                count_lives -= 1
                continue
            # print("\n")

            if cypher_list.count("-") == 0:
                count_lives = 0

        if (cypher_list.count("-") == 0):
            # print("\n" + correct_word)
            print("\nYou guessed the word {}!".format(correct_word))
            print("\nYou survived!")
            wins += 1
        else:
            print("\nYou lost!")
            losts += 1
    elif input_menu == "results":
        print("\nYou won: {} times.".format(wins))
        print("You lost: {} times.".format(losts))
    elif input_menu == "exit":
        break

    input_menu = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: > ')
