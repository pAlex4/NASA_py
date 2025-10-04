import pygame

pygame.init()

# Screen setup
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Top Bar with Dropdown, Cycle, and Rotate Buttons')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (150, 150, 150)

font = pygame.font.SysFont(None, 24)

class TopBarButton:
    def __init__(self, x, y, width, height, text, options=None, cycle=False):
        """
        cycle=True means each click cycles through the options instead of showing dropdown.
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.options = options or []
        self.dropdown_visible = False
        self.dropdown_rects = []
        self.selected_option = None
        self.cycle = cycle
        if self.cycle and self.options:
            self.selected_option = self.options[0]

    def draw(self, surface):
        pygame.draw.rect(surface, GRAY, self.rect)
        display_text = self.text
        if self.cycle and self.selected_option is not None:
            display_text += f": {self.selected_option}"
        text_surf = font.render(display_text, True, BLACK)
        surface.blit(text_surf, (self.rect.x + 10, self.rect.y + 5))

        if self.dropdown_visible and not self.cycle:
            self.dropdown_rects = []
            x, y = self.rect.x, self.rect.y + self.rect.height
            width, height = self.rect.width, 30
            for i, option in enumerate(self.options):
                rect = pygame.Rect(x, y + i * height, width, height)
                self.dropdown_rects.append(rect)
                pygame.draw.rect(surface, GRAY, rect)
                option_text = font.render(option, True, BLACK)
                surface.blit(option_text, (x + 5, y + 5 + i * height))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
            if self.rect.collidepoint(event.pos):
                if self.cycle:
                    # Cycle through options
                    if self.options:
                        current_index = self.options.index(self.selected_option)
                        next_index = (current_index + 1) % len(self.options)
                        self.selected_option = self.options[next_index]
                        print(f'{self.text} changed to: {self.selected_option}')
                else:
                    # Toggle dropdown visibility
                    self.dropdown_visible = not self.dropdown_visible
                return True
            elif self.dropdown_visible and not self.cycle:
                for i, rect in enumerate(self.dropdown_rects):
                    if rect.collidepoint(event.pos):
                        self.selected_option = self.options[i]
                        print(f'Selected: {self.selected_option}')
                        self.dropdown_visible = False
                        return True
                # Click outside dropdown closes it
                self.dropdown_visible = False
        return False

class TopBar:
    def __init__(self, width, height, buttons):
        self.rect = pygame.Rect(0, 0, width, height)
        self.buttons = buttons

    def draw(self, surface):
        pygame.draw.rect(surface, DARK_GRAY, self.rect)
        for button in self.buttons:
            button.draw(surface)

    def handle_event(self, event):
        for button in self.buttons:
            if button.handle_event(event):
                break

options_button = TopBarButton(10, 5, 100, 30, "Options", ['Option 1', 'Option 2', 'Option 3'])
mode_button = TopBarButton(120, 5, 150, 30, "Mode", ['draw', 'delete'], cycle=True)
rotate_button = TopBarButton(280, 5, 150, 30, "Rotate", ['0°', '90°', '180°', '270°'], cycle=True)

top_bar = TopBar(600, 40, [options_button, mode_button, rotate_button])

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        top_bar.handle_event(event)

    top_bar.draw(screen)

    pygame.display.flip()

pygame.quit()
