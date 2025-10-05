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
        self.previsualization_block = Previsualization_Block()

    def update_player_grid_position(self):
    #Actualiza la posicion del jugador en el grid
        self.gridPosition  =  self.camera.iso_to_grid(self.isoPosition)
        self.previsualization_block.update_position_block(self.gridPosition, self.camera )

    def add_block(self, img):

        #Si no hay bloques en grid entonces los agrega
        if self.gridPosition  not in self.grid:
            self.grid.add( self.gridPosition)
            #Crea un bloque y lo agrega al set de Sprites Layout
            self.previsualization_block.update_block_image(img)
            self.layout.add(Block(self.gridPosition, img), layer= sum(self.gridPosition))
        else:
            x,y,z =self.gridPosition
            z += 1
            self.layout.add(Block((x,y,z), img), layer= sum(self.gridPosition))

    def update_blocks_position(self):
        self.layout.update(self.camera)
        






