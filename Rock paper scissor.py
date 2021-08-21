import random
choices = ["Rock","Paper","Scissor"]
pc = random.choice(choices)
cpu_score = 0
player_score = 0
flag = False
while True:
    player = input("Rock, Paper or  Scissor, else write q to quit ").capitalize()
    if(player=="Q"):
        break
    elif(pc == player):
        print("Tie")
    elif(player == "Rock"):
        if(pc == "Scissor"):
            print("You win")
            player_score+=1
        else:
            print("You Lose")
            cpu_score+=1
    elif(player == "Scissor"):
        if(pc=="Rock"):
            print("You Lose")
            cpu_score+=1
        else:
            print("You win")
            player_score+=1
    elif(player == "Paper"):
        if(pc=="Scissor"):
            print("You lose")
            cpu_score+=1
        else:
            print("You win")
            player_score+=1
print(f"CPU Score is '{cpu_score}' and your Score is '{player_score}")
