import pygame

# Initialize Pygame
pygame.init()

# Set up some constants
W, H = 600, 600
CELL_SIZE = 40

# Your pre-existing game board
game_board = [
    [0, 0, 2, 1, 1, 3, 0, 0],
    [0, 2, 1, 1, 1, 3, 0, 0],
    [0, 2, 1, 1, 1, 1, 3, 0],
    [2, 1, 1, 1, 1, 1, 3, 0],
    [5, 2, 1, 1, 1, 1, 3, 4],
    [2, 1, 1, 1, 1, 1, 3, 0],
    [0, 2, 1, 1, 1, 1, 3, 0],
    [0, 2, 1, 1, 1, 3, 0, 0],
    [0, 0, 2, 1, 1, 3, 0, 0],
]

# Calculate the size of the game board
BOARD_WIDTH = len(game_board[0]) * CELL_SIZE
BOARD_HEIGHT = len(game_board) * CELL_SIZE

# Calculate the offset needed to center the game board
OFFSET_X = (W - BOARD_WIDTH) // 2
OFFSET_Y = (H - BOARD_HEIGHT) // 2

# Create the screen
screen = pygame.display.set_mode((W, H))

# Function to draw the game board
def draw_board():
    for y, row in enumerate(game_board):
        for x, cell in enumerate(row):
            if cell >= 1:
                rect = pygame.Rect(OFFSET_X + x*CELL_SIZE + (CELL_SIZE//2)*(y%2), OFFSET_Y + y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, (255, 255, 255), rect)
                pygame.draw.rect(screen, (0, 0, 0), rect, 1)
            if cell == 2:
                pygame.draw.circle(screen, (0, 0, 255), (OFFSET_X + x*CELL_SIZE + CELL_SIZE//2 + (CELL_SIZE//2)*(y%2), OFFSET_Y + y*CELL_SIZE + CELL_SIZE//2), CELL_SIZE//4)
            if cell == 3:
                pygame.draw.circle(screen, (255, 0, 0), (OFFSET_X + x*CELL_SIZE + CELL_SIZE//2 + (CELL_SIZE//2)*(y%2), OFFSET_Y + y*CELL_SIZE + CELL_SIZE//2), CELL_SIZE//4)
            if cell == 4:
                pygame.draw.polygon(screen, (0, 0, 255), [(OFFSET_X + x*CELL_SIZE + CELL_SIZE//2 + (CELL_SIZE//2)*(y%2) - CELL_SIZE//4, OFFSET_Y + y*CELL_SIZE + CELL_SIZE//2 - CELL_SIZE//4), (OFFSET_X + x*CELL_SIZE + CELL_SIZE//2 + (CELL_SIZE//2)*(y%2) + CELL_SIZE//4, OFFSET_Y + y*CELL_SIZE + CELL_SIZE//2 - CELL_SIZE//4), (OFFSET_X + x*CELL_SIZE + CELL_SIZE//2 + (CELL_SIZE//2)*(y%2) + CELL_SIZE//4, OFFSET_Y + y*CELL_SIZE + CELL_SIZE//2 + CELL_SIZE//4), (OFFSET_X + x*CELL_SIZE + CELL_SIZE//2 + (CELL_SIZE//2)*(y%2) - CELL_SIZE//4, OFFSET_Y + y*CELL_SIZE + CELL_SIZE//2 + CELL_SIZE//4)])
            if cell == 5:
                pygame.draw.polygon(screen, (255, 0, 0), [(OFFSET_X + x*CELL_SIZE + CELL_SIZE//2 + (CELL_SIZE//2)*(y%2) - CELL_SIZE//4, OFFSET_Y + y*CELL_SIZE + CELL_SIZE//2 - CELL_SIZE//4), (OFFSET_X + x*CELL_SIZE + CELL_SIZE//2 + (CELL_SIZE//2)*(y%2) + CELL_SIZE//4, OFFSET_Y + y*CELL_SIZE + CELL_SIZE//2 - CELL_SIZE//4), (OFFSET_X + x*CELL_SIZE + CELL_SIZE//2 + (CELL_SIZE//2)*(y%2) + CELL_SIZE//4, OFFSET_Y + y*CELL_SIZE + CELL_SIZE//2 + CELL_SIZE//4), (OFFSET_X + x*CELL_SIZE + CELL_SIZE//2 + (CELL_SIZE//2)*(y%2) - CELL_SIZE//4, OFFSET_Y + y*CELL_SIZE + CELL_SIZE//2 + CELL_SIZE//4)])

# Game loop
running = True
selected_cell = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            cell_y = (mouse_y - OFFSET_Y) // CELL_SIZE
            cell_x = (mouse_x - OFFSET_X - (CELL_SIZE//2)*(cell_y%2)) // CELL_SIZE
            if 0 <= cell_x < len(game_board[0]) and 0 <= cell_y < len(game_board):
                if game_board[cell_y][cell_x] >= 1:
                    selected_cell = (cell_x, cell_y)

    screen.fill((100, 100, 100))
    draw_board()
    if selected_cell is not None:
        pygame.draw.circle(screen, (0, 0, 0), (OFFSET_X + selected_cell[0]*CELL_SIZE + CELL_SIZE//2 + (CELL_SIZE//2)*(selected_cell[1]%2), OFFSET_Y + selected_cell[1]*CELL_SIZE + CELL_SIZE//2), CELL_SIZE//2, 2)
    pygame.display.flip()

pygame.quit()