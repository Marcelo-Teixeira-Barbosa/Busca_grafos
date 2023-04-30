import pygame

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Set the dimensions of the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Create the Pygame window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set the caption of the window
pygame.display.set_caption("Pygame Buttons with Hover Effect Example")

# Define the font to use for the buttons
button_font = pygame.font.SysFont("Arial", 24)

# Define the dimensions and position of the upper half of the screen
upper_half_width = WINDOW_WIDTH
upper_half_height = (WINDOW_HEIGHT-350) // 2
upper_half_rect = pygame.Rect(0, 0, upper_half_width, upper_half_height)

# Define the dimensions and position of the lower half of the screen
lower_half_width = WINDOW_WIDTH
lower_half_height = WINDOW_HEIGHT // 2
lower_half_rect = pygame.Rect(0, upper_half_height, lower_half_width, lower_half_height)

# Define the dimensions and position of the buttons
button_width = 200
button_height = 50
button_padding = 20
button_x = (upper_half_width - (button_width * 3 + button_padding * 2)) // 2
button_y = (upper_half_height - button_height) // 2

# Create the buttons
button1_rect = pygame.Rect(button_x, button_y, button_width, button_height)
button2_rect = pygame.Rect(button_x + button_width + button_padding, button_y, button_width, button_height)
button3_rect = pygame.Rect(button_x + button_width * 2 + button_padding * 2, button_y, button_width, button_height)

# Define the text to display on the buttons
button1_text = button_font.render("Button 1", True, WHITE)
button2_text = button_font.render("Button 2", True, WHITE)
button3_text = button_font.render("Button 3", True, WHITE)

# Create the black rectangle
rectangle_rect = pygame.Rect(0, upper_half_height, lower_half_width, lower_half_height)

# Set the background color of the upper half of the screen
screen.fill(WHITE, upper_half_rect)

# Draw the buttons on the upper half of the screen
def draw_button(rect, text, color):
    pygame.draw.rect(screen, color, rect)
    screen.blit(text, rect.move(10, 10))

button_states = {
    tuple(button1_rect): False,
    tuple(button2_rect): False,
    tuple(button3_rect): False,
}

# Update the state of the buttons
def update_buttons():
    for rect, text in [(button1_rect, button1_text), (button2_rect, button2_text), (button3_rect, button3_text)]:
        if rect.collidepoint(pygame.mouse.get_pos()):
            button_states[tuple(rect)] = True
            draw_button(rect.move(2, 2), text, GRAY)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            button_states[tuple(rect)] = False
            draw_button(rect, text, BLACK)
    if not any(button_states.values()):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)



# Draw the black rectangle on the lower half of the screen
pygame.draw.rect(screen, BLACK, rectangle_rect)

# Update the display
pygame.display.flip()

# Run the game loop
running = True
while running:
    update_buttons()
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
