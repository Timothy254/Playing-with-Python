import random

def randomise():
    list_of_fighters = [1, 2, 3]
    cpu = int(random.choice(list_of_fighters))
    print ("Computer chooses.....",cpu)
    return cpu

def fight(fighter,cpu):
    if fighter == 1 and cpu == 2:
        print ("Paper beats rock. You loose!!")
    elif fighter == 1 and cpu == 3:
        print("Rock beats scissors. You win!!")
    elif fighter == 2 and cpu == 1:
        print("paper beats rock. You win!!")
    elif fighter == 2 and cpu == 3:
        print("scissors beats paper. You loose!!")
    elif fighter == 3 and cpu == 1:
        print("rock beats scissors. You loose!!")
    elif fighter == 3 and cpu == 2:
        print("scissors beats paper. You win!!")
    else:
        print ("Its a draw. Try again.")

fighter = input("Welcome to 1.Rock 2.Paper 3.Scissors! \n Choose your fighters number(1,2,3)!!")
cpu=randomise()
fight(fighter,cpu)









