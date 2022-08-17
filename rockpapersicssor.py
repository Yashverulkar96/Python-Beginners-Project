import random

you=0
cpu=0
while True:
    choices=["Rock","Paper","Scissor"]
    computer=random.choice(choices)
    player=input("Rock,Paper or Scissor?").capitalize()
    # if both are same then tie
    if player==computer:
        print("Tie")
        # if player select rock then
    elif player=="Rock":
        if computer=="Paper":
            print("Computer wins:Paper wrap Rock")
            cpu+=1
        else:
            print("Player wins:rock can't be cut using scissor")
            you+=1
    elif player=="Paper":
        if computer=="Scissor":
            print("Computer wins:Scissor can cut Paper")
            cpu+=1
        else:
            print("Player wins:Paper Wrap Rock")
            you+=1
    elif player=="Scissor":
        if computer=="Rock":
            print("Computer wins:Rock can't be cut using scissor")
            cpu+=1
        else:
            print("Player wins:Scissor can cut Paper")
            you+=1
    elif player=="End":
        print("Computer Score:{}\nYour Score:{}\n".format(cpu,you))
        if(you>cpu):
            print("You win the Battle")
        elif(cpu>you):
            print("Computer win the battle")
        else:
            print("It is a Tie")
        break
