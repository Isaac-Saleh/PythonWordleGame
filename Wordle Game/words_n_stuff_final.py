import random


# ------ Global Variables ---------


with open("target_words.txt") as target_words:
    target_content = target_words.read().split()

with open("all_words.txt") as valid_words:
    content = valid_words.read().split()  # Creates the list of valid words to check against

MAX_ATTEMPTS = 6  # No. of attempts before game over this never changes



#   -------- Functions -----------


def random_word_generator(target_content):
    # target_word = "snail" # - Uncomment for testing purposes
    target_word = random.choice(target_content)  # Chooses the target word from list
    return target_word


def welcome_statement():
    print("Welcome to Words-N-Stuff, The fun game that will frustrate you if you lose.")
    print("The RULES are simple:")
    print("\t\t-Guess a 5 letter word, if it is correct you win!")
    print("\t\t-However, If your guess contains some of the letters not in their right place, they will highlight '?'")
    print("\t\t-If some of these letters are in the CORRECT place they will highlight '+' ")
    print("\t\t-Any letters NOT in the word anywhere will be marked with 'X'")
    print("You have", MAX_ATTEMPTS, "attempts....")


def user_input():
    guess = input("Enter you Guess: ")
    guess = guess.lower().strip()
    return guess


def check_validity(guess):
    if len(guess) < 5:
        print("Word is too short")
        return False
    if len(guess) > 5:
        print("Word too long!")
        return False
    if guess not in content:
        print(f"{guess.upper()} is not a valid word")
        return False
    else:
        return True


def guess_score(guess, target_word):
    for i in range(len(guess)):
        if guess[i] == target_word[i]:
            print("🟢", end="")

        elif guess[i] in target_word:
            print("🟡", end="")

        else:
            print("🔴", end="")

    if guess != target_word:

        if remaining_attempts == 1:
            print(f"\nIncorrect, you now have {remaining_attempts} attempt left")
        else:
            print(f"\nIncorrect, you now have {remaining_attempts} attempts left")


def game_signoff(games_played, total_game_guesses):
    average_guess = total_game_guesses / games_played
    print("\nTHANK YOU FOR PLAYING WORDS-N-STUFF")
    print("\nSTATS-N-STUFF:")
    print(f"\tGAMES PLAYED :{games_played}")
    print(f"\tAVERAGE GUESS COUNT :{average_guess}")


# ---------------- Executable Program ------------------------


welcome_statement()

games_played = 0
total_game_guesses = 0
game_guess_count = 0
guess_attempts = 0

play_again = ""
while play_again != "n":
    games_played = games_played + 1
    game_guess_count = 0
    target_word = random_word_generator(target_content)

    while game_guess_count != MAX_ATTEMPTS:

        guess = user_input()
        validity = check_validity(guess)
        if validity:
            game_guess_count = game_guess_count + 1
            print(" ".join(guess.upper()))
            remaining_attempts = MAX_ATTEMPTS - game_guess_count
            guess_score(guess, target_word)

        if guess == target_word:
            print(f"\nNice guess, it is indeed {target_word.upper()}!!")
            if game_guess_count == 1:
                print(f"You got it in {game_guess_count} try")
            else:
                print(f"You got it in {game_guess_count} trys")
            break

        if game_guess_count == MAX_ATTEMPTS:
            print(f"The word you were after was {target_word.upper()}!!")
            break



    total_game_guesses = total_game_guesses + game_guess_count
    play_again = input("Ready to play? Y/N ")
    play_again = play_again.lower()

game_signoff(games_played, total_game_guesses)

















