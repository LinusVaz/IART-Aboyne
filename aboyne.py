# main.py
import pygame
from board import game_board
from logic import game_loop

# Initialize Pygame
pygame.init()

W, H = 600, 600
CELL_SIZE = 40

# Calculate the size of the game board
BOARD_WIDTH = len(game_board[0]) * CELL_SIZE // 2
BOARD_HEIGHT = len(game_board) * CELL_SIZE 

# Calculate the offset needed to center the game board
OFFSET_X = (W - BOARD_WIDTH) // 2
OFFSET_Y = (H - BOARD_HEIGHT) // 2

# Create the screen
screen = pygame.display.set_mode((W, H))

# Start the game loop
game_loop(screen, OFFSET_X, OFFSET_Y)

pygame.quit()