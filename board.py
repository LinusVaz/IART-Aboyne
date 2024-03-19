import pygame

# Set up some constants
W, H = 600, 600
CELL_SIZE = 40

# Your pre-existing game board

game_board = [
    [0, 0, 0, 0, 2, 0, 1, 0, 1, 0, 1, 0, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 3, 0, 0, 0, 0],
    [0, 0, 2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 3, 0, 0, 0],
    [0, 2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 3, 0, 0],
    [5, 0, 2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 3, 0, 4, 0], #
    [0, 2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 3, 0, 0],
    [0, 0, 2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 3, 0, 0, 0],
    [0, 0, 0, 2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 1, 0, 1, 0, 1, 0, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


# Function to draw the game board
def draw_board(screen, OFFSET_X, OFFSET_Y):
    for y, row in enumerate(game_board):
        for x, cell in enumerate(row):
            if cell >= 1:
                rect = pygame.Rect(OFFSET_X + x*(CELL_SIZE//2), OFFSET_Y + y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, (255, 255, 255), rect)
                pygame.draw.rect(screen, (0, 0, 0), rect, 1)
            if cell == 2:
                pygame.draw.circle(screen, (0, 0, 255), (OFFSET_X + x*(CELL_SIZE//2) + CELL_SIZE//2, OFFSET_Y + y*CELL_SIZE + CELL_SIZE//2), CELL_SIZE//4)
            if cell == 3:
                pygame.draw.circle(screen, (255, 0, 0), (OFFSET_X + x*(CELL_SIZE//2) + CELL_SIZE//2, OFFSET_Y + y*CELL_SIZE + CELL_SIZE//2), CELL_SIZE//4)
            if cell == 4:
                pygame.draw.rect(screen, (0, 0, 255), (OFFSET_X + x*(CELL_SIZE//2) + CELL_SIZE//4, OFFSET_Y + y*CELL_SIZE + CELL_SIZE//4, CELL_SIZE//2, CELL_SIZE//2))
            if cell == 5:
                pygame.draw.rect(screen, (255, 0, 0), (OFFSET_X + x*(CELL_SIZE//2) + CELL_SIZE//4, OFFSET_Y + y*CELL_SIZE + CELL_SIZE//4, CELL_SIZE//2, CELL_SIZE//2))

