import pygame 
from src.player import *

HEIGHT = 800
WIDTH = 800
FPS = 60



def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("Game")
    TILE_IMG_RAW = pygame.image.load("assets/img/unit1.png").convert_alpha()
    TILE_IMG = pygame.transform.scale(TILE_IMG_RAW, (80, 80)) 
    player = Player()
    
    running = True

    while running:
        mx, my = pygame.mouse.get_pos() #Adqueire la posicion del jugador
        player.isoPosition = (mx,my,0)
        player.update_player_grid_position()
        events = pygame.event.get() 
        for e in events:
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1: #Si el jugador presiona click derecho, se agrega bloque
                player.add_block(TILE_IMG)

        player.camera.handle_input(events) #Actualiza la posicion de la camara
        player.update_blocks_position() #Actualiza la posicion de los bloques dado la posicion de la camara

        screen.fill((15, 15, 15))
        player.layout.draw(screen) #dibuja los bloque en la caudricula
        

        pygame.display.flip()
        clock.tick(FPS)
        


if __name__ == "__main__":
    main()
