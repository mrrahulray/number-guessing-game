import random

# unbiased number gussing game gussing game:

def Number_gussing_game():
    print("Welcome to the Number Guessing Game!")
    random_number= random.randint(1,101)

    finished_game = False
    No_of_gusse = 0
    while not finished_game is True:
        No_of_gusse+=1
        user_input = int (input("Gusse the number: "))
        if (user_input== random_number):
            print(f"The game is finished! \n You have gusses {No_of_gusse} time")
            finished_game=True
        elif (user_input> random_number):
            print("Try again! \n You guessed too high")
        elif (user_input< random_number):
            print("Try again! \n You guessed too low")
        
    play_again= (input("Do you want to paly again?(y/n)")).upper()
    if (play_again=="Y"):
        Number_gussing_game()
    elif (play_again=="N"):
        print("Thank you for playing")
    else:
        print("Thank you for playing")



Number_gussing_game()
