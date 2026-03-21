import random

words = ["python", "computer", "science", "mobile", "program"]
word = random.choice(words)

guessed = []
attempts = 6

print("=== Hangman Game ===")

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    guess = input("Enter a letter: ").lower()

    if guess in guessed:
        print("Already guessed!")
        continue

    if guess in word:
        guessed.append(guess)
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

    if all(letter in guessed for letter in word):
        print("\n🎉 You won! Word is:", word)
        break

if attempts == 0:
    print("\n❌ Game Over! Word was:", word)
