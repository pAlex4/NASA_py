import pygame
import math
class Camera:
    def __init__(self):
        self.offset = pygame.Vector2(0, 0)
        self.speed = 16
        self.dragging = False
        self._dragStart = None
       
       #Varibles que dependen del bloque unitario
        self._anchor = (0, 0)
        #Longitud en pixeles del bloque unitario
        self._isoWidth = 80
        #Altura en pixeles del bloque unitario 
        self._isoHeight = 53
        self._baseOrigin =  (self._isoWidth//2, 120)
        self._eps = 1e-6

    def handle_input(self, events):
        keys = pygame.key.get_pressed()


        if keys[pygame.K_a] or keys[pygame.K_LEFT]:  self.offset.x += self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: self.offset.x -= self.speed
        if keys[pygame.K_w] or keys[pygame.K_UP]:    self.offset.y += self.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:  self.offset.y -= self.speed

        for e in events:  # drag con botón medio (opcional)
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 2:
                self.dragging, self._drag_start = True, pygame.Vector2(e.pos)
            elif e.type == pygame.MOUSEBUTTONUP and e.button == 2:
                self.dragging = False
            elif e.type == pygame.MOUSEMOTION and self.dragging:
                m = pygame.Vector2(e.pos)
                delta = m - self._drag_start
                self.offset += delta     # arrastras la vista
                self._drag_start = m

    #Transforma las coordenadas del grid cuadrado en vista isometrica      
    def grid_to_iso(self, pos):
        ox, oy = self._baseOrigin
        ax, ay = self._anchor
   
        x = ox + self.offset.x + (self._isoWidth//2)*(pos[0] - pos[1]) + ax
        y = oy + self.offset.y + (self._isoHeight //2)*(pos[0] + pos[1]) - pos[2]*self._isoHeight + ay
        z = pos[2]
        return x, y, z
    #Transforma las coordenadas de la vista isometrica a grid cuadrado     
    def iso_to_grid(self, pos):
        ox, oy = self._baseOrigin
        ax, ay = self._anchor
        X = pos[0] - ox - self.offset.x- ax
        Y = pos[1] - oy - self.offset.y - ay
        u = X / (self._isoWidth/2)
        v = Y / (self._isoHeight/2)
        i_f = 0.5*(u+v)
        j_f = 0.5*(v-u)
        i = math.floor(i_f + self._eps)
        j = math.floor(j_f + self._eps)
        k = pos[2]
        return i, j, k
