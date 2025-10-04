import pygame
from src.block import *
from src.camera import * 
class Player():
    def __init__(self):
        # Recuadro del grid donde se encuentra el jugador
        self.gridPosition =  (0,0,0)
        
        # Visualización isométrica de la posición del jugador
        self.isoPosition =  (0,0,0)

        self.layout = pygame.sprite.LayeredUpdates()  

        self.grid = set()
        self.camera = Camera()

    def update_player_grid_position(self):

        self.gridPosition  =  self.camera.iso_to_grid(self.isoPosition)

    def add_block(self, img):
        #Actualiza la posicion del jugador en el grid
        self.update_player_grid_position()
        #Si no hay bloques en grid entonces los agrega
        if self.gridPosition  not in self.grid:
            self.grid.add( self.gridPosition)
            #Crea un bloque y lo agrega al set de Sprites Layout
            self.layout.add(Block(self.gridPosition, img), layer= sum(self.gridPosition))

    def update_draw_blocks_position(self):
        self.layout.update(self.camera)
        






