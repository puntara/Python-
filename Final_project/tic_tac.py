import random
grid_x=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
player=1
switch=1

human='x'
computer='o'
#first_player=human
mark ='x'
win_value=1
tie_value=-1
run=0
on =0
game=on

while True:
    try:
        print('enter mode vs computer or vs human')
        mode=int(input('1 or 2: '))
        if mode==1 or mode==2:
            break
        else:
            print("Not in range of 0-2: ")
    except ValueError:
        print(" 1 or 2 only")

#________________________________________________________________
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

def board(grid_x):
    print('Position')
    print(' 0 | 1 | 2 ')
    print(' -- -- -- ')
    print(' 3 | 4 | 5 ')
    print(' -- -- -- ')
    print(' 6 | 7 | 8 ')
    print(' -- -- -- ')
    print('Main Board')
    print(' %c | %c | %c ' % (grid_x[0],grid_x[1],grid_x[2]))
    print(' --  -- -- ')
    print(' %c | %c | %c ' % (grid_x[3],grid_x[4],grid_x[5]))
    print(' --  -- -- ')
    print(' %c | %c | %c ' % (grid_x[6],grid_x[7],grid_x[8]))   
#________________________________________________________________
# versus Human
while(game==on and mode==1):
    board(grid_x)
    if (player%2!=0):
        print("players 1 turn")
        mark = 'x'
    else:
        print("players 2 turn")
        mark = 'o'
    while True:
        try:
            position=int(input("0-8 position: "))
            if(position==0 or position==1 or position==2 or position==3 or position==4 or position==5 or position==6 or position==7 or position==8):
                break
            else:
                print("Not in range of 0-8: ")
        except ValueError:
            print('only 0 -8 numbers')
    if(grid_x[position]==' '):
        grid_x[position]=mark
        player=player+1
        win() # check for game win
    if game==tie_value:
        print('The Game is a tie')
    elif game==win_value:
        player-=1
        if player%2!=0:
            print('player 1 is the winner.')
        else:
            print('player 2 is the winner.')

#________________________________________________________________
#x