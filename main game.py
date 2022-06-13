import random

# Game 
game = {'R': 'Rock', 'P': "Paper", 'S': 'Scissors'}

# Computer_logic
def computer_move():
    game_options = ['R', 'P', 'S']
    computer_choice = random.choice(game_options)
    if computer_choice in game:
        return game[computer_choice]


# Player_logic
def player_move():
    while True:
        player_choice = input('Pick a move "R", "P", "S":  ')
        player_choice = player_choice.upper()

        if player_choice in game:
            return game[player_choice]  
        else:
            print('Invalid input, Please pick from the options given \n')


# Condition for winning
def winner_condition():
    list1 = ('Rock', 'Paper', 'Scissors')
    list2 = ('Scissors', 'Rock', 'Paper')
    winner = list(zip(list1, list2))
    return winner

# Main game logic
def game_flow():
    # Game loop
    while True:
        computer = computer_move()
        player = player_move()
        winner = winner_condition()
        
        # Player and Computer move displayed
        print(f'\nPlayer ({player}) : CPU ({computer}) \n')

        # Winner check
        #set player to False
player = False

while player == False:
#set player to True
        if player == computer:
                print('It\'s a tie Play again \n')
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
            
        if player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
        if player == "Scissors":
            if computer == "Rock":
                print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)

        if (player, computer) in winner:
            print('Player Wins')
            break
        if (computer, player) in winner:
            print('Computer Wins')
            break
        player=False
        computer = t[randint(0,2)]

# Game prompt
print('Welcome to the Rock, Paper, Scissors game  \nThis game is Player vs CPU  \nYour avaliable moves are:')
print('"R" for "Rock"  \n"P" for "Paper" \n"S" for "Scissors" ')

game_flow()
