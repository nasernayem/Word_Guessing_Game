import random
from data import words
lives = 6
end_of_the_game = False
random_word = random.choice(words)
print(random_word)

display = []
for word in range(len(random_word)):
    display += "_"
print(display)
while not end_of_the_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print('You have already guessed that letter')

    for position in range(len(random_word)):
        letter = random_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if guess not in random_word:
        lives -= 1
        print("Letter does not exist")
        if lives == 0:
            end_of_the_game = True
    if '_' not in display:
        print("You Win!!!")
        end_of_the_game = True
