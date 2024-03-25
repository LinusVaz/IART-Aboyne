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
                if cell != 0:    
                    if valid_move(piece, (x, y), player_turn):
                        moves += 1
    return moves

def is_enemy(cell, player_turn):
    if player_turn == 1 and game_board[cell[1]][cell[0]] == 3:
        return True
    if player_turn == 2 and game_board[cell[1]][cell[0]] == 2:
        return True
    return False


def is_adjacent(cell1, cell2):
    if cell1[1] == cell2[1] and (cell1[0] == cell2[0] + 2 or cell1[0] == cell2[0] - 2):
        return True
    if cell1[0] == cell2[0] + 1 and (cell1[1] == cell2[1] + 1 or cell1[1] == cell2[1] - 1):
        return True
    if cell1[0] == cell2[0] - 1 and (cell1[1] == cell2[1] + 1 or cell1[1] == cell2[1] - 1):
        return True

def is_jump(cell1, cell2, player_turn):
    if cell1[1] == cell2[1]:
        if cell1[0] < cell2[0]:
            for i in range(cell1[0]+2, cell2[0], 2):
                if game_board[cell1[1]][i] != player_turn+1:
                    return False
            return True
        if cell1[0] > cell2[0]:
            for i in range(cell2[0]+2, cell1[0], 2):
                if game_board[cell1[1]][i] != player_turn+1:
                    return False
            return True
        
    # Calculate the differences
    diff_x = abs(cell2[0] - cell1[0])
    diff_y = abs(cell2[1] - cell1[1])

    # Check if the cells are on the same 45-degree diagonal
    if diff_x == diff_y:
        for i in range(1, diff_x):
            if cell1[0] < cell2[0] and cell1[1] < cell2[1]:  # Diagonal down-right
                if game_board[cell1[1]+i][cell1[0]+i] != player_turn+1:
                    return False
            elif cell1[0] < cell2[0] and cell1[1] > cell2[1]:  # Diagonal up-right
                if game_board[cell1[1]-i][cell1[0]+i] != player_turn+1:
                    return False
            elif cell1[0] > cell2[0] and cell1[1] < cell2[1]:  # Diagonal down-left
                if game_board[cell1[1]+i][cell1[0]-i] != player_turn+1:
                    return False
            else:  # Diagonal up-left
                if game_board[cell1[1]-i][cell1[0]-i] != player_turn+1:
                    return False
        return True
    else:
        # The cells are not on the same 45-degree diagonal
        return False
        



def valid_move(selected_cell, destination_cell, player_turn):
    if(game_board[selected_cell[1]][selected_cell[0]] == player_turn+1):
        if(not blocked_cell(selected_cell)):
            if(is_adjacent(selected_cell, destination_cell)):
                if(game_board[destination_cell[1]][destination_cell[0]] == 1 or winning_way(selected_cell,destination_cell)):
                    return True
            else:
                if(is_jump(selected_cell, destination_cell, player_turn)):
                    if(game_board[destination_cell[1]][destination_cell[0]] == 1 or is_enemy(destination_cell, player_turn) or winning_way(selected_cell,destination_cell)):
                        return True
            
def blocked_cell(cell3):      #check if adjacent cells have enemy pieces
    if game_board[cell3[1]][cell3[0]] == 2:
        if cell3[1] > 0 and cell3[0] > 0:
            if game_board[cell3[1]-1][cell3[0]-1] == 3:
                return True
        if cell3[1] > 0 and cell3[0] < len(game_board[0])-1:
            if game_board[cell3[1]-1][cell3[0]+1] == 3:
                return True
        if cell3[1] < len(game_board)-1 and cell3[0] > 0:
            if game_board[cell3[1]+1][cell3[0]-1] == 3:
                return True
        if cell3[1] < len(game_board)-1 and cell3[0] < len(game_board[0])-1:
            if game_board[cell3[1]+1][cell3[0]+1] == 3:
                return True
    if game_board[cell3[1]][cell3[0]] == 3:
        if cell3[1] > 0 and cell3[0] > 0:
            if game_board[cell3[1]-1][cell3[0]-1] == 2:
                return True
        if cell3[1] > 0 and cell3[0] < len(game_board[0])-1:
            if game_board[cell3[1]-1][cell3[0]+1] == 2:
                return True
        if cell3[1] < len(game_board)-1 and cell3[0] > 0:
            if game_board[cell3[1]+1][cell3[0]-1] == 2:
                return True
        if cell3[1] < len(game_board)-1 and cell3[0] < len(game_board[0])-1:
            if game_board[cell3[1]+1][cell3[0]+1] == 2:
                return True
    
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
                if check_goal(destination_cell, player_turn):
                    running = False
                    break
                player_turn = change_turn(player_turn) 
                game_board[destination_cell[1]][destination_cell[0]] = game_board[selected_cell[1]][selected_cell[0]]
                game_board[selected_cell[1]][selected_cell[0]] = 1   
                print("Player", player_turn, "turn") 
                print("Valid moves: ", valid_moves(player_turn, get_pieces(player_turn)))  
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
