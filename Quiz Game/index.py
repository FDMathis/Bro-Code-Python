def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("--------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)
        