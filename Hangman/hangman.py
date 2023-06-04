import random
from words import word_list

# no of wrong guesses allowed
wrong_guess = 6

# guessed letters
guess =[]
done = False

# picking random words from the word list
word = (random.choice(word_list)).upper()

# running a while loop till user get's it right or out of guesses
while not done:
    # putting empty _ at the start of the game
    for letter in word:
        if letter.upper() in guess:
            print(letter,end =" ")
        else:
            print("_",end=" ")
    print("")

    # taking guess input
    guesses = input(f"Number of Guess Left {wrong_guess}, Next Guess:")
    guess.append(guesses.upper())

    # TODO: Add the hanging man drawing to the output.
    if guesses.upper() not in word.upper():
        wrong_guess -=1
        if wrong_guess == 0:
            break
    done= True
    
    # checking of player got it right.
    for letter in word:
        if letter.upper() not in guess:
            done = False

# end message
if done:
    print(f"You found the word. It was {word}")
else:
    print(f"Game Over! The word was {word}")