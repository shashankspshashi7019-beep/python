import random
	
words = ("banana", "apple", "kiwi", "orange", "mango")
word = random.choice(words)
display = ["_"] * len(word)

attempts = 6
guessed_letters = []

print("Welcome to Hangman!")
print("Guess the word:")
print(" ".join(display))

while attempts > 0 and "_" in display:

    guess = input("Enter a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)
    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess

    else:
        attempts -= 1
        print("Wrong guess!")
        print("Attempts left:", attempts)

    print(" ".join(display))

if "_" not in display:
    print("🎉 You won!")
    print("The word was:", word)

else:
    print("😢 You lost!")
    print("The word was:", word)

