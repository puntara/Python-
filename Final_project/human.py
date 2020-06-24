import random
grid_x=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
player=1
switch=1


#first_player=human
mark ='x'
win_value=1
tie_value=-1
run=0
on =0
randomNumber=range(0,9)
game=on

HUMAN='x'
COMPUTER='o'
turn=1
first_player=HUMAN


while True:
    try:
        print('enter mode 1 for human 2 for computer')
        mode=int(input('1 or 2: '))
        if mode==1 or mode==2:
            break
    except ValueError:
        print(" 1 or 2 only")

def win():
    global game
    if(grid_x[0]==grid_x[3] and grid_x[3]==grid_x[6] and grid_x[0]!=" "):
            game=win_value
    elif(grid_x[1]==grid_x[4] and grid_x[4]==grid_x[7] and grid_x[1]!=" "):
        game=win_value
    elif(grid_x[2]==grid_x[5] and grid_x[5]==grid_x[8] and grid_x[2]!=" "):
        game=win_value

    elif(grid_x[1]==grid_x[0] and grid_x[1]==grid_x[2] and grid_x[0]!=" "):
        game=win_value
    elif(grid_x[3]==grid_x[4] and grid_x[4]==grid_x[5] and grid_x[3]!=" "):
        game=win_value
    elif(grid_x[6]==grid_x[7] and grid_x[7]==grid_x[8] and grid_x[6]!=" "):
        game=win_value

    elif(grid_x[0]==grid_x[4] and grid_x[4]==grid_x[8] and grid_x[0]!=" "):
        game=win_value
    elif(grid_x[2]==grid_x[4] and grid_x[4]==grid_x[6] and grid_x[2]!=" "):
        game=win_value
    #draw
    elif(grid_x[0]!=' ' and grid_x[1]!=' ' and grid_x[2]!=" " 
        and grid_x[3]!=" " and grid_x[4]!=' ' and grid_x[5]!=' ' 
        and grid_x[6]!=" " and grid_x[7]!=" " and grid_x[7]!=" "):
        game=tie_value
    else:
        game=run

def take_turn(player, turn):
    while True:
        if player is COMPUTER:
            box=get_computer_move()
        else:
            box=int(input('Player %s '% player))
#________________________________________________________________
def get_computer_move():
    return random.ranint(0,8)
def switch_player(turn):
    current_player=COMPUTER if turn%2==0 else HUMAN
    return current_player
#________________________________________________________________
# versus Computer

while(game==on and mode==2):
    print('%c | %c | %c ' % (grid_x[0],grid_x[1],grid_x[2]))
    print('%c | %c | %c ' % (grid_x[3],grid_x[4],grid_x[5]))
    print('%c | %c | %c ' % (grid_x[6],grid_x[7],grid_x[8]))




if game==tie_value:
    print('tie')
elif game==win_value:
    player-=1
    if human%2!=0:
        print('Human is the winner.')
    else:
        print('Computer is the winner.')
#________________________________________________________________

    