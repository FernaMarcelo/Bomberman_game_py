import pygame
import os

class irrompible(pygame.sprite.Sprite):
    def __init__(self, c, f, tamanio):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('Imagenes', 'Escenario', 'crate_19.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (tamanio, tamanio))
        self.rect = self.image.get_rect()
        self.rect.x =  c * tamanio
        self.rect.y = f * tamanio


class rompible(pygame.sprite.Sprite):
    def __init__(self, c, f, tamanio):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('Imagenes', 'Escenario', 'crate_10.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (tamanio, tamanio))
        self.rect = self.image.get_rect()
        self.rect.x =  c * tamanio
        self.rect.y = f * tamanio
        self.posicion_x = c
        self.posicion_y = f