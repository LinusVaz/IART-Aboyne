# game_logic.py
import pygame
from board import game_board, draw_board, CELL_SIZE

def change_turn(player_turn):
    if player_turn == 1:
        return 2
    else:
        return 1

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
             if(blocked_cell(selected_cell,destination_cell)):
                  return True
            
def blocked_cell(cell3, cell4):  
    if game_board[cell3[1]][cell3[0]] == 2 and (game_board[cell3[1]-1][cell3[0]-1] == 3 or game_board[cell3[1] +1][cell3[0]-1] == 3 or game_board[cell3[1]-1][cell3[0]+1] == 3 or game_board[cell3[1] +1][cell3[0]+1] == 3 or game_board[cell3[1]][cell3[0] - 2] == 3 or game_board[cell3[1]][cell3[0] + 2] == 3):
        game_board[cell4[1]][cell4[0]] = 1
        game_board[cell3[1]][cell3[0]] = 2
             
    elif game_board[cell3[1]][cell3[0]] == 3 and (game_board[cell3[1]-1][cell3[0]-1] == 2 or game_board[cell3[1] +1][cell3[0]-1] == 2 or game_board[cell3[1]-1][cell3[0]+1] == 2 or game_board[cell3[1] +1][cell3[0]+1] == 2 or game_board[cell3[1]][cell3[0] - 2] == 2 or game_board[cell3[1]][cell3[0] + 2] == 2):
           game_board[cell4[1]][cell4[0]] = 1
           game_board[cell3[1]][cell3[0]] = 3
           
    else:
        return True   
    
                             
        
        


def winning_way(cell2, cell3):
    
    if game_board[cell2[1]][cell2[0]] == 2 and game_board[cell3[1]][cell3[0]] == 4:
        game_board[cell3[1]][cell3[0]] = 2
        game_board[cell2[1]][cell2[0]] = 1
        
        
        
    elif game_board[cell2[1]][cell2[0]] == 3 and game_board[cell3[1]][cell3[0]] == 5:
        game_board[cell3[1]][cell3[0]] = 3
        game_board[cell2[1]][cell2[0]] = 1
        
        
    else:
        game_board[cell2[1]][cell2[0]] = game_board[cell2[1]][cell2[0]]
        game_board[cell3[1]][cell3[0]] = game_board[cell3[1]][cell3[0]]  
        
        


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
                        print(cell_x, cell_y)
                        if selected_cell is None:
                            selected_cell = (cell_x, cell_y)
                        elif destination_cell is None:
                            destination_cell = (cell_x, cell_y)

        if selected_cell is not None and destination_cell is not None:
            if(valid_move(selected_cell, destination_cell, player_turn)):
                game_board[destination_cell[1]][destination_cell[0]] = game_board[selected_cell[1]][selected_cell[0]]
                game_board[selected_cell[1]][selected_cell[0]] = 1
                selected_cell = None
                destination_cell = None
                player_turn = change_turn(player_turn)
            else:
                selected_cell = None
                destination_cell = None
        screen.fill((100, 100, 100))
        draw_board(screen, OFFSET_X, OFFSET_Y)
        if selected_cell is not None:
            pygame.draw.circle(screen, (0, 0, 0), (OFFSET_X + (selected_cell[0]*CELL_SIZE//2) + CELL_SIZE//2, OFFSET_Y + selected_cell[1]*CELL_SIZE + CELL_SIZE//2), CELL_SIZE//2, 2)
        pygame.display.flip()  
