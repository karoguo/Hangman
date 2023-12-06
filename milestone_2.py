# Import the random module
import random

# Step 1 and 2: Create a list of 5 favorite fruits and assign it to word_list
word_list = ["Apple", "Banana", "Cherry", "Peach", "Strawberry"]

# Ask the user to enter a single letter
guess = input("Please enter a single letter: ")

# Check if the input is one letter and is alphabetical
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

# Step 3 and 4: Use random.choice to select a random word from word_list
word = random.choice(word_list)

# Step 5: Print out the randomly chosen word
print(word)