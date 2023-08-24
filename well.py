secret_word = "idiot savant"
guesses = []
limit = 5
current_guess = ""
out_of_guesses = False
while current_guess != secret_word and not out_of_guesses:
    current_guess = input("Enter your guess: ")
    if current_guess == secret_word:
        print(f"Congrats! Your guess is correct in {5-limit+1} tries.\nYour previous guesses were {guesses}")
    else:
        limit -= 1
        guesses.append(current_guess)
        if limit == 0:
            out_of_guesses = True
            print(f"Sorry, You are out of guesses. Your previous guesses were {guesses}.")
        else:
            print("Try again.")
