import pygame
from src.block import *
from src.camera import * 
class Player():
    def __init__(self):
        # Recuadro del grid donde se encuentra el jugador
        self.gridPosition =  [0,0,0]
        
        # Visualización isométrica de la posición del jugador
        self.isoPosition =  [0,0,0]

        self.layout = pygame.sprite.LayeredUpdates()  

        self.grid = {}
        self.camera = Camera()
        self.previsualization_block = Previsualization_Block()
    def update_player_grid_position(self):
        """Actualiza la posición del jugador en el grid y la altura de previsualización."""
        # Calcular la posición actual en el grid
        self.gridPosition = list(self.camera.iso_to_grid(self.isoPosition))

        x, y, z = self.gridPosition

        # Buscar la primera altura libre (z más alto + 1)
        while (x, y, z) in self.grid:
            z += 1

        # Actualizar posición del bloque de previsualización justo arriba
        self.previsualization_block.update_position_block((x, y, z), self.camera)


    def add_block(self, img, tipo="default"):
        x, y, z = self.gridPosition

        # Si no hay bloque en esta coordenada, crear uno
        if (x, y, z) not in self.grid:
         
            self.grid[(x, y, z)] = {"tipo": tipo, "img": img}
            self.layout.add(Block((x, y, z), img), layer=x + y + z)

        # Si ya hay bloque, apilar hacia arriba
        else:
            while (x, y, z) in self.grid:
                z += 1
            self.previsualization_block.update_position_block((x, y, z), self.camera )
            self.grid[(x, y, z)] = {"tipo": tipo, "img": img}
            self.previsualization_block.update_block_image(img)
            self.layout.add(Block((x, y, z), img), layer=x + y + z)


    def update_blocks_position(self):
        self.layout.update(self.camera)
        






