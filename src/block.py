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
        x, y = camera.grid_to_iso(self.pos[0], self.pos[1],0)
        self.rect.midtop = (x,y)  # usa el MISMO ancla que en grid_to_iso


