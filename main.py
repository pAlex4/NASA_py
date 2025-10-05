import pygame 
from src.player import *
from src.topbar import *

# Constantes
HEIGHT = 720
WIDTH = 1280
FPS = 60

# Inicializacion de pygame
pygame.init()
font = pygame.font.SysFont(None, 24)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Titulo y carga de imagenes
pygame.display.set_caption("Game")
TILE_IMG_RAW = pygame.image.load("assets/img/unit1.png").convert_alpha()
TILE_IMG = pygame.transform.scale(TILE_IMG_RAW, (80, 80)) 
player = Player()

# Topbar
options_button = TopBarButton(10, 5, 120, 30, "Options",
                              ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5',
                               'Option 6', 'Option 7', 'Option 8', 'Option 9'], max_visible=5)
mode_button = TopBarButton(140, 5, 150, 30, "Mode", ['draw', 'delete'], cycle=True)
rotate_button = TopBarButton(300, 5, 150, 30, "Rotate", ['0°', '90°', '180°', '270°'], cycle=True)
extra_button = TopBarButton(460, 5, 150, 30, "Extra", ['A', 'B', 'C'], cycle=True)

label = TopBarLabel(620, 5, 70, 30, "Stats: 0")

top_bar = TopBar(700, 40, [options_button, mode_button, rotate_button, extra_button], label)


# Loop principal
running = True
while running:
    mx, my = pygame.mouse.get_pos() #Adqueire la posicion del jugador
    player.isoPosition = (mx,my,0)
    player.update_player_grid_position()

    # Manejo de eventos
    events = pygame.event.get() 
    for e in events:
        top_bar.handle_event(e)
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1: #Si el jugador presiona click derecho, se agrega bloque
            player.add_block(TILE_IMG)


    player.camera.handle_input(events) #Actualiza la posicion de la camara
    player.update_blocks_position() #Actualiza la posicion de los bloques dado la posicion de la camara

    screen.fill((15, 15, 15))
    
    player.layout.draw(screen) #dibuja los bloque en la caudricula
    screen.blit(player.previsualization_block.image, player.previsualization_block.rect)
    
    # draw topbar
    top_bar.draw(screen)
    
    pygame.display.flip()
    clock.tick(FPS)
    


