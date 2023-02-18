#blackjack game
#made in my way
import random
from logo import logo
print(logo)
game_cont=True
letter =[11,2,3,4,5,6,7,8,9,10,10,10,10]
player = [random.choice(letter),random.choice(letter)]
computer = [random.choice(letter),random.choice(letter)]
def calculate():
    player_score=sum(player)
    computer_score=sum(computer)
    print(f"Your cards are {player}, Your current score is {player_score} ")
    print(f"The first computer card is {computer[0]}")
calculate()
proceed = input("Do you want to Draw new card: 'yes' or 'no'\n")
def new_score():
    player.append(random.choice(letter))
def new_card():
    player_score=sum(player)
    if player_score>21 and 11 in player:
        player.remove(11)
        player.append(1)
        player_score=sum(player)
    else:
        pass
    computer_score=sum(computer)
    if player_score>21 or player_score<computer_score:
        print(f"{player} and computer {computer}")
        print(f"You Failed, your score is {player_score} and computer score is {computer_score}")
    elif player_score>computer_score:
        print(f"{player} and computer {computer}")
        print(f"You won with score of {player_score}")
if proceed=="yes":
        new_score()
        new_card()
elif proceed=="no":
    new_card()
cool = input("Do you want to continue: 'yes' or 'no':\n")
if cool=="yes":
    game_cont=True
elif cool=="no":
    game_cont=False
def game():
    letter =[11,2,3,4,5,6,7,8,9,10,10,10,10]
    player = [random.choice(letter),random.choice(letter)]
    computer = [random.choice(letter),random.choice(letter)]
    def calculate():
        player_score=sum(player)
        computer_score=sum(computer)
        print(f"Your cards are {player}, Your current score is {player_score} ")
        print(f"The first computer card is {computer[0]}")
    calculate()
    proceed = input("Do you want to Draw new Card: 'yes' or 'no'\n")
    def new_score():
        player.append(random.choice(letter))
    def new_card():
        player_score=sum(player)
        if player_score>21 and 11 in player:
            player.remove(11)
            player.append(1)
            player_score=sum(player)
        else:
            pass
        computer_score=sum(computer)
        if player_score>21 or player_score<computer_score:
            print(f"{player} and computer {computer}")
            print(f"You Failed, your score is {player_score} and computer score is {computer_score}")
        elif player_score>computer_score:
            print(f"{player} and computer {computer}")
            print(f"You won with score of {player_score}")
    if proceed=="yes":
            new_score()
            new_card()
    elif proceed=="no":
        new_card()
    cool = input("Do you want to continue playing Game: 'yes' or 'no':\n")
    if cool=="yes":
        game_cont=True
    elif cool=="no":
        game_cont=False
if game_cont==False:
    print("Thank you")
    exit()
while game_cont==True:
    game()
    