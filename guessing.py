secret_num = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guesses_num = int(input("Guess "))
    guess_count += 1

    if guesses_num == secret_num:
        print("You Won ")
        break
else:
    print("Sorry !! All the chances are done")
