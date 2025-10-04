import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, pos, img):
        super().__init__()
        self.pos = pos
        self.image = img
        self.rect = self.image.get_rect()
        self._layer = sum(pos)  # para LayeredUpdates
        # no fijes rect aquí; se fijará en update()
    def update(self, camera):
        x, y, z = camera.grid_to_iso(self.pos)
        self.rect.midtop = (x,y)  # usa el MISMO ancla que en grid_to_iso

class Prev_Block_Visualization(Block):
    def __init__(self, img_hover):
        # inicia con una posición dummy (0,0,0)
        super().__init__((0, 0, 0), img_hover)
        self.image = img_hover
        self.rect = self.image.get_rect(midtop=(0, 0))

    def update(self, player_position, camera):
        # convierte las coords del mouse a coordenadas de grilla
        i, j, k = camera.iso_to_grid(player_position)
        self.pos = (i, j, 0)  # mantenemos compatibilidad con Block
        x, y = grid_to_iso(i, j, 0)
        self.rect.midtop = (x, y)