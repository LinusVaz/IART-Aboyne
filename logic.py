# game_logic.py
import pygame
from board import game_board, draw_board, CELL_SIZE

def change_turn(player_turn):
    if player_turn == 1:
        return 2
    else:
        return 1

def get_pieces(player_turn):
    pieces = []
    moves = 0
    for y,row in enumerate(game_board):
        for x, cell in enumerate(row):
            if cell == player_turn+1:
                pieces.append((x, y))
    return pieces
                    
def valid_moves(player_turn, pieces):
    moves = 0
    for piece in pieces:
        for y,row in enumerate(game_board):
            for x, cell in enumerate(row):    
                if valid_move(piece, (x, y), player_turn):
                    moves += 1
    return moves
                    

def is_adjacent(cell1, cell2):
    if cell1[1] == cell2[1] and (cell1[0] == cell2[0] + 2 or cell1[0] == cell2[0] - 2):
        return True
    if cell1[0] == cell2[0] + 1 and (cell1[1] == cell2[1] + 1 or cell1[1] == cell2[1] - 1):
        return True
    if cell1[0] == cell2[0] - 1 and (cell1[1] == cell2[1] + 1 or cell1[1] == cell2[1] - 1):
        return True

def valid_move(selected_cell, destination_cell, player_turn):
    if(game_board[selected_cell[1]][selected_cell[0]] == player_turn+1):
        if(game_board[destination_cell[1]][destination_cell[0]] == 1 or winning_way(selected_cell,destination_cell)):
            if(is_adjacent(selected_cell, destination_cell)):
             if(not blocked_cell(selected_cell,destination_cell)):
                  return True
            
def blocked_cell(cell3, cell4):  
    if game_board[cell3[1]][cell3[0]] == 2 and (game_board[cell3[1]-1][cell3[0]-1] == 3 or game_board[cell3[1] +1][cell3[0]-1] == 3 or game_board[cell3[1]-1][cell3[0]+1] == 3 or game_board[cell3[1] +1][cell3[0]+1] == 3 or game_board[cell3[1]][cell3[0] - 2] == 3 or game_board[cell3[1]][cell3[0] + 2] == 3):
        return True
             
    elif game_board[cell3[1]][cell3[0]] == 3 and (game_board[cell3[1]-1][cell3[0]-1] == 2 or game_board[cell3[1] +1][cell3[0]-1] == 2 or game_board[cell3[1]-1][cell3[0]+1] == 2 or game_board[cell3[1] +1][cell3[0]+1] == 2 or game_board[cell3[1]][cell3[0] - 2] == 2 or game_board[cell3[1]][cell3[0] + 2] == 2):
        return True
           
    else:
        return False
    
def winning_way(cell2, cell3):
    
    if game_board[cell2[1]][cell2[0]] == 2 and game_board[cell3[1]][cell3[0]] == 4:
        return True
        
    elif game_board[cell2[1]][cell2[0]] == 3 and game_board[cell3[1]][cell3[0]] == 5:
        return True
           
    else:
        return False  
        
def check_goal(destination_cell, player_turn):
    if game_board[destination_cell[1]][destination_cell[0]] == 4 and player_turn == 1:
        print("Blue wins!")
        return True
    if game_board[destination_cell[1]][destination_cell[0]] == 5 and player_turn == 2:
        print("Red wins!")
        return True
    return False

def check_no_moves(player_turn):
    if(valid_moves(player_turn, get_pieces(player_turn)) == 0):
        if(player_turn == 1):
            print("Red wins!")
        else:
            print("Blue wins!")
        return True
    return False

def game_loop(screen, OFFSET_X, OFFSET_Y):
    running = True
    player_turn = 1 # 1 for blue, 2 for red
    selected_cell = None
    destination_cell = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                cell_y = (mouse_y - OFFSET_Y) // CELL_SIZE
                cell_x = (mouse_x - OFFSET_X) // (CELL_SIZE//2)
                if 0 <= cell_x < len(game_board[0]) and 0 <= cell_y < len(game_board):
                    if(game_board[cell_y][cell_x]==0):
                        cell_x = cell_x - 1
                    if game_board[cell_y][cell_x] >= 1:
                        if selected_cell is None:
                            selected_cell = (cell_x, cell_y)
                        elif destination_cell is None:
                            destination_cell = (cell_x, cell_y)

        if selected_cell is not None and destination_cell is not None:
            if(valid_move(selected_cell, destination_cell, player_turn)):
                player_turn = change_turn(player_turn)   
                if check_goal(destination_cell, player_turn):
                    running = False
                    break
                game_board[destination_cell[1]][destination_cell[0]] = game_board[selected_cell[1]][selected_cell[0]]
                game_board[selected_cell[1]][selected_cell[0]] = 1    
                print(valid_moves(player_turn, get_pieces(player_turn)))  
                if check_no_moves(player_turn):
                    running = False   
                    break    
                selected_cell = None
                destination_cell = None
            else:
                selected_cell = None
                destination_cell = None
        screen.fill((100, 100, 100))
        draw_board(screen, OFFSET_X, OFFSET_Y)
        if selected_cell is not None:
            pygame.draw.circle(screen, (0, 0, 0), (OFFSET_X + (selected_cell[0]*CELL_SIZE//2) + CELL_SIZE//2, OFFSET_Y + selected_cell[1]*CELL_SIZE + CELL_SIZE//2), CELL_SIZE//2, 2)
        pygame.display.flip()  
