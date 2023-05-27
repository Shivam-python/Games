import random

# no of wrong guesses allowed
wrong_guess = 6

# guessed letters
guess =[]
done = False

# list of all thr words
word_list = '''ant baboon badger bat bear beaver camel cat clam cobra cougar coyote
crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama
mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram
rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger
toad trout turkey turtle weasel whale wolf wombat zebra'''.split()

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