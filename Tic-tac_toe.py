# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 23:58:06 2018
The classic family friendly tic tac toe game!
@author: Vick
"""

###### TIC-TAC-TOE########################################

#### Tic tac toe winning combinations for a 3x3 board 
#####Horizontal 
horizontal1=(0,1,2)
horizontal2=(3,4,5)
horizontal3=(6,7,8)

horizontal_win=(horizontal1,horizontal2,horizontal3)

####Vertical 
vertical1=(0,3,6)
vertical2=(1,4,7)
vertical3=(2,5,8)

vertical_win=(vertical1,vertical2,vertical3)
    
###Diagonal 
diag1=(0,4,8)
diag2=(2,4,6)

diagonal_win=(diag1,diag2)
win=(horizontal_win,vertical_win,diagonal_win)

####################################FUNCTIONS#################################################
def check_board_status(board):
    counter=0
    for item in board: 
        if item ==0:
            counter+=1

    if counter>0:
        board_status='empty'
    else:
        board_status='full'

    return board_status

def forbidden_moves(board):
    forbidden=[]
    for value,item in enumerate(board):
        
        if item=='X' or item=='O':
            forbidden.append(value+1)
            
    return forbidden

def check_selection_constraint(player_1=0,player_2=0):
    if player_2==0: 
        if player_1 in range(1,10):
            return 'Correct'   
        else:
            return 'Not_correct'
    else:
        if player_2 in range(1,10):
            return 'Correct'     
        else:
            return 'Not_correct'
        
def available_positions(positions_occuppied):
    available=[]
    original_board=(1,2,3,4,5,6,7,8,9)
    
    for item in original_board:
        if item not in positions_occuppied:
            available.append(item)
    return available

import itertools ###Module to enumerate all possible play combinations 
        
def check_win(win,turn,tup_1=0,tup_2=0):
    if turn<3:
        return 'none' 
    
    elif turn>=3:
        checklist1=[]
        checklist2=[]
        if turn==3:

            if tup_2==0: ###Operate tup 1 only
                tup_1.sort()
                tup_1=tuple(tup_1)

                for tup_of_tup in win:
                    for tup in tup_of_tup:
                        if tup_1==tup:
                            checklist1.append('1WIN')
                            break
                        else:
                            checklist1.append('none')
            else: ###Operate tup 2 only
                tup_2.sort()
                tup_2=tuple(tup_2)

                for tup_of_tup in win:
                    for tup in tup_of_tup:
                        if tup_2==tup:
                            checklist2.append('2WIN')
                            break
                        else: 
                            checklist2.append('none')        
        else:
     
            if tup_2==0: ###Operate tup 1 only
                for perm in itertools.permutations(tup_1,3):
                    for tup in win: 
                        if perm in tup: 
                            checklist1.append('1WIN')
                            break
                        else:
                            checklist1.append('none')
                            
            else: ###Operate tup 2 only
                for perm in itertools.permutations(tup_2,3):
                    for tup in win: 
                        if perm in tup: 
                            checklist2.append('2WIN')
                            break
                        else:
                            checklist2.append('none')
     
    if tup_2==0:
        if '1WIN' in checklist1:
            return('1WIN')
        else:
            return('none')

    else:
        if '2WIN' in checklist2:
            return('2WIN')
        else:
            return('none')
    
def board_current(board,positions_occuppied):
    update=available_positions(positions_occuppied)
    
    original_list=[1,2,3,4,5,6,7,8,9]

    for item in original_list:
        if item not in update:
            idx=original_list.index(item)
            update.insert(idx,'*')
    
    new_list=[]
    for step in range(0,7,3):
        if step==0:
            new_list.append(board[step:step+3]+update[step:step+3])
        else:
            new_list.append(board[step:step+3]+update[step:step+3])
        
    final_list=[]
    for sub_list in new_list:
        for item in sub_list:
            final_list.append(item)

    print(" {0}      {1}".format('Game', 'Available positions'))
    print("|{}|{}|{}|    |{}|{}|{}| \n|{}|{}|{}|    |{}|{}|{}| \n|{}|{}|{}|    |{}|{}|{}| \n".format(*final_list))

import random     
def player_start():
    who_starts=['P1','P2']
    start=random.randint(0,1)
    
    return [start,who_starts]

############################################################################################################

##########################################BEGIN GAME########################################################

#####X-0 assignment for each player 

mark=('X','O') ##Each player will be assigned a mark, either 'X' or 'O', in a random fashion.  

assignment=random.randint(0,1)

print('TIC TAC TOE')
print('\n')
print('GAME ON!')
print('\n')

player1_mark=mark[assignment]
print('**Player 1 you have been assigned the mark "{}" for the current game!'.format(player1_mark))
print('\n')

player2_mark=mark[abs(assignment-1)]
print('**Player 2 you have been assigned the mark "{}" for the current game!'.format(player2_mark))
print('\n')

board=[0,0,0,0,0,0,0,0,0]

board_status='empty'         ###Initial status of the board
positions_occuppied=[]       ###Because board is empty, there are no occuppied positions 
turn=1
tup_1=[]
tup_2=[]
check_winner='none'

print("Let's determine who goes first:")
print("...")

[start,who_starts]=player_start()
print('\n')
print('**Player {} starts!'.format(who_starts[start]))
print('\n')

############################################MAIN LOOP######################################

while check_winner is 'none' or board_status is 'empty':
    
################################PLAYER 1###################################################
    if who_starts[start]=='P1':
    
        player_1_done=False
        while player_1_done==False: 

            player_1_position_selection='Not_correct'
            while player_1_position_selection=='Not_correct':

                player_1=int(input('\t Player 1 "{}" please input your move:'.format(player1_mark)))
                player_1_position_selection=check_selection_constraint(player_1,0)

                if player_1_position_selection=='Not_correct':
                    print('\tPlease select a number between 1 and 9 within the available positions')

            ###
            if positions_occuppied==[]:
                board[player_1-1]=player1_mark
                positions_occuppied=forbidden_moves(board)

                tup_1.append(player_1-1)

                player_1_done=True

            elif player_1 not in positions_occuppied:
                board[player_1-1]=player1_mark
                positions_occuppied=forbidden_moves(board)

                tup_1.append(player_1-1)
                check_winner=check_win(win,turn,tup_1,0)

                player_1_done=True

            else:
                print('Player 1 Please choose a position in the board which has not been chosen')
                print('\n')

                available=available_positions(positions_occuppied)
                print('The current available position(s) are the following {}'.format(available))
                continue

        print('\n')
        board_current(board,positions_occuppied)
        print('\n')

        ###Main loop check 

        if check_winner=='1WIN':
            print('Player 1 wins!!!!!')
            break

        board_status=check_board_status(board)
        if board_status=='full':
            print('You tied!!!!!!')
            break
            
        start=not start

################################PLAYER 2#################################################### 
    elif who_starts[start]=='P2':
        
        player_2_done=False
        while player_2_done==False: 

            player_2_position_selection='Not_correct'
            while player_2_position_selection=='Not_correct':  

                player_2=int(input('\t Player 2 "{}" please input your move:'.format(player2_mark)))
                player_2_position_selection=check_selection_constraint(0,player_2)

                if player_2_position_selection=='Not_correct':
                    print('Please select a number between 1 and 9 within the available positions')
                else:
                    continue

            ###
            if positions_occuppied==[]:
                board[player_2-1]=player2_mark
                positions_occuppied=forbidden_moves(board)

                tup_2.append(player_2-1)
                player_2_done=True

            elif player_2 not in positions_occuppied:
                board[player_2-1]=player2_mark
                positions_occuppied=forbidden_moves(board)

                tup_2.append(player_2-1)
                check_winner=check_win(win,turn,0,tup_2)

                player_2_done=True    

            else:
                print('Player 2 Please choose a position in the board which has not been chosen')
                print('\n')

                available=available_positions(positions_occuppied)
                print('The current available position(s) are the following {}'.format(available))
                continue

        print('\n')
        board_current(board,positions_occuppied) 
        print('\n') 

        #####Main loop check 
        if check_winner=='2WIN':
            print('Player 2 wins!!!!')
            break

        board_status=check_board_status(board)
        if board_status=='full':
            print('You tied!!!!!')
            break
            
        start=not start

        turn+=1
    