secret_word = "cat" #sets the word to be found
guess = ""
z = 0
limit = 5
attempt = []
while guess != secret_word and limit > 0:
    guess = input("Enter your guess: ")
    z += 1
    limit -= 1
    if guess == secret_word:
        print(f"Congrats! Your guess is correct in {z} tries!")
    else:
        print(f"Try again. You have {limit} guesses left.")
        attempt.append(guess)
if limit == 0:
    print(f"sorry. no more attempts left.")
print(f"Your guesses: {attempt}")
