import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            if guess not in self.word_guessed:
                self.num_letters -= 1
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ").strip()
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break  # Exit the loop after a valid guess

# New function to play the game
def play_game(word_list):
    game = Hangman(word_list, num_lives=5)

    while True:
        if game.num_lives == 0:
            print('You lost! The word was:', game.word)
            break
        elif game.num_letters > 0:
            print(' '.join(game.word_guessed))
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break

# Example usage
word_list = ["apple", "banana", "cherry"]
play_game(word_list)