import pygame

# Initialize Pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Top Bar Dropdown Example')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (150, 150, 150)

# Font
font = pygame.font.SysFont(None, 24)

# Dropdown menu options
menu_options = ['Option 1', 'Option 2', 'Option 3']

# Bar and button dimensions
bar_height = 40
button_width = 100
button_height = 30
button_rect = pygame.Rect(10, 5, button_width, button_height)

# Dropdown state
dropdown_visible = False
dropdown_rects = []

running = True
while running:
    screen.fill(WHITE)

    # Draw top bar
    pygame.draw.rect(screen, DARK_GRAY, (0, 0, 600, bar_height))

    # Draw options button
    pygame.draw.rect(screen, GRAY, button_rect)
    button_text = font.render("Options", True, BLACK)
    screen.blit(button_text, (button_rect.x + 10, button_rect.y + 5))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                if button_rect.collidepoint(event.pos):
                    # Toggle dropdown visibility
                    dropdown_visible = not dropdown_visible
                elif dropdown_visible:
                    clicked_option = False
                    for i, rect in enumerate(dropdown_rects):
                        if rect.collidepoint(event.pos):
                            print(f'Selected: {menu_options[i]}')
                            dropdown_visible = False
                            clicked_option = True
                            break
                    if not clicked_option:
                        # Clicked outside dropdown, hide it
                        dropdown_visible = False

    # Draw dropdown menu below the button if visible
    if dropdown_visible:
        dropdown_rects = []
        x, y = button_rect.x, button_rect.y + button_rect.height
        width, height = button_width, 30
        for i, option in enumerate(menu_options):
            rect = pygame.Rect(x, y + i * height, width, height)
            dropdown_rects.append(rect)
            pygame.draw.rect(screen, GRAY, rect)
            option_text = font.render(option, True, BLACK)
            screen.blit(option_text, (x + 5, y + 5 + i * height))

    pygame.display.flip()

pygame.quit()
