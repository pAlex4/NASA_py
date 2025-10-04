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
    def __init__(self, img=None, alpha=128):
        super().__init__((0, 0, 0), img)
        # Aplica transparencia si hay imagen
        if self.image:
            self.image.set_alpha(alpha)  # 0 = invisible, 255 = opaco

    def update_position_block(self, player_position, camera):
        self.pos = player_position
        x, y, z = camera.grid_to_iso(player_position)
        self.rect.midtop = (x, y)

    def update_block_image(self, image):
        self.image = image
        self.rect = self.image.get_rect(midtop=self.rect.midtop)  # ← re-sincroniza rect
