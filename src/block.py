import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, pos, img=None):
        super().__init__()
        self.pos = pos
        if img is None:
            self.image = pygame.Surface((64, 32), pygame.SRCALPHA)
            self.image.fill((255, 255, 255, 0))
        else:
            self.image = img
        self.rect = self.image.get_rect(midtop=(0, 0))  # ← evita el AttributeError
        self._layer = sum(pos)

    def update(self, camera):
        x, y, z = camera.grid_to_iso(self.pos)
        self.rect.midtop = (x, y)


class Previsualization_Block(Block):
    def __init__(self, img=None, alpha=50):
        # si hay imagen, crea una copia para no modificar la original
        img_copy = img.copy() if img else None
        super().__init__((0, 0, 0), img_copy)

        # aplica transparencia solo a la copia local
        if self.image:
            self.image.set_alpha(alpha)

    def update_position_block(self, player_position, camera):
        self.pos = player_position
        x, y, z = camera.grid_to_iso(player_position)
        self.rect.midtop = (x, y)

    def update_block_image(self, image, alpha=50):
        # vuelve a crear copia independiente antes de cambiar alpha
        self.image = image.copy()
        self.image.set_alpha(alpha)
        self.rect = self.image.get_rect(midtop=self.rect.midtop)
