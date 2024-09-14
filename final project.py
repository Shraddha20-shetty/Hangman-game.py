#Define categories and words
categories = {
    'Animals': ['elephant', 'tiger', 'penguin', 'kangaroo'],
    'Countries': ['canada', 'germany', 'brazil', 'japan'],
    'Movies': ['inception', 'titanic', 'gladiator', 'avatar']
}

# ASCII art for hangman
hangman_graphics = [
    """
      ------
      |    |
           | 
           |
           |
           |
    --------
    """,
    """
      ------
      |    |
      O    |
           |
           |
           |
    --------
    """,
    """
      ------
      |    |
      O    |
      |    |
           |
           |
    --------
    """,
    """
      ------
      |    |
      O    |
     /|    |
           |
           |
    --------
    """,
    """
      ------
      |    |
      O    |
     /|\\   |
           |
           |
    --------
    """,
    """
      ------
      |    |
      O    |
     /|\\    |
     /     |
           |
    --------
    """,
    """
      ------
      |    |
      O    |
     /|\\   |
     / \\   |
           |
    --------
    """,
]

# Function to choose a category
def choose_category():
    print("Choose a category:")
    for index, category in enumerate(categories.keys()):
        print(f"{index + 1}. {category}")
    choice = int(input("Enter the number of your choice: ")) - 1
    category = list(categories.keys())[choice]
    return category, categories[category]

# Function to display hangman state
def display_hangman(tries):
    print(hangman_graphics[tries])

# Function to set difficulty level
def set_difficulty():
    print("Choose a difficulty level:")
    print("1. Easy (8 incorrect guesses allowed)")
    print("2. Medium (6 incorrect guesses allowed)")
    print("3. Hard (4 incorrect guesses allowed)")
    
    difficulty = int(input("Enter the number of your choice: "))
    
    if difficulty == 1:
        max_tries = 8
    elif difficulty == 2:
        max_tries = 6
    else:
        max_tries = 4
    
    return max_tries

# Function to provide a hint
def provide_hint(word):
    hint = f"The word is related to: {word[0].upper()}..."
    return hint

# Function to offer hint during the game
def offer_hint(word, used_hint):
    if not used_hint:
        use_hint = input("Would you like a hint? (y/n): ").lower() == 'y'
        if use_hint:
            print(provide_hint(word))
            return True
    return False

# Simple random selection without importing random
def choose_word(word_list):
    index = int(input(f"Choose a number between 1 and {len(word_list)}: ")) - 1
    return word_list[index]

# Main game loop
def play_hangman():
    category, word_list = choose_category()
    word = choose_word(word_list).lower()  # Use custom word chooser without random
    max_tries = set_difficulty()
    used_hint = False
    
    guessed_letters = []
    tries = 0
    word_completion = "_" * len(word)
    
    print(f"Category: {category}")
    display_hangman(tries)
    print(word_completion)
    
    while tries < max_tries:
        guess = input("Please guess a letter: ").lower()
        
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                tries += 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! {guess} is in the word!")
                guessed_letters.append(guess)
                word_completion = ''.join([letter if letter in guessed_letters else '_' for letter in word])
            
            display_hangman(tries)
            print(word_completion)
        else:
            print("Invalid input. Please guess a single letter.")
        
        if "_" not in word_completion:
            print("Congratulations, you won!")
            break
        
        if offer_hint(word, used_hint):
                    used_hint = True

    if tries == max_tries:
        print(f"Sorry, you lost. The word was {word}.")
        
# Start the game
play_hangman()

