import random

options = ("rock","paper","scissors")
player = None
computer = random.choice(options)
running = True
u = 0
c = 0
while running :

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input ("Enter a choice(rock,paper,scissors):")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer :
        print("It's a Tie !")
    elif player == "rock" and computer == "scissors":
        print ("You win !")
        u = u+1
    elif player == "paper" and computer =="rock":
        print ("You win !") 
        u = u+1
    elif player == "scissors" and computer == "paper":
        print ("You win !")
        u = u+1
    else :
        print ("Computer win !")
        c = c+1      
    play_again = input("Play again ? (y/n)").lower() 

    if not play_again == "y":
       running = False
if u>c:
    print("You are the winner !")
elif c>u :
    print ("Computer is the winner !") 
else :
    print ("It's a Draw !")       
print("Thanks for playing")             
