import pygame 
from src.player import *

HEIGHT = 800
WIDTH = 800
FPS = 60



def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    selected_tile = 1
    pygame.display.set_caption("Game")
    TILE_IMG_RAW = pygame.image.load("assets/img/unit1.png").convert_alpha()
    TILE_IMG = pygame.transform.scale(TILE_IMG_RAW, (80, 80)) 
    TILE_IMG_2 = pygame.transform.scale(TILE_IMG_RAW, (2*80, 2*80)) 
    TILE_IMG_3 = pygame.transform.scale(TILE_IMG_RAW, (3*80, 3*80)) 
    TILE_IMG_4 = pygame.transform.scale(TILE_IMG_RAW, (4*80, 4*80)) 
    sel ={1:TILE_IMG,2:TILE_IMG_2,3:TILE_IMG_3,4:TILE_IMG_4}
    player = Player()
    
    running = True
    numero = 1
    while running:
        mx, my = pygame.mouse.get_pos() #Adqueire la posicion del jugador
        player.isoPosition = (mx,my,0)
        player.update_player_grid_position()
        events = pygame.event.get() 
        for e in events:
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.KEYDOWN:
            # Revisar si es una tecla numérica
                if pygame.K_0 <= e.key <= pygame.K_9:
                    numero = e.key - pygame.K_0
                    if selected_tile != numero:
                        selected_tile = numero
                        print(selected_tile)
            elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1: #Si el jugador presiona click derecho, se agrega bloque
                

                player.add_block(sel[numero])

            

        player.camera.handle_input(events) #Actualiza la posicion de la camara
        player.update_blocks_position() #Actualiza la posicion de los bloques dado la posicion de la camara

        screen.fill((15, 15, 15))
        player.layout.draw(screen) #dibuja los bloque en la caudricula
        screen.blit(player.previsualization_block.image, player.previsualization_block.rect)

        pygame.display.flip()
        clock.tick(FPS)
        


if __name__ == "__main__":
    main()
