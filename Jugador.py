import pygame
import os
from Bomba import bomba

class jugador(pygame.sprite.Sprite):
    def __init__(self, c, f, all_bomba, all_sprites, all_rompibles, tamanio, suelo):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('Imagenes', 'Lucy', 'Abajo', '1.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (tamanio, tamanio))
        self.rect = self.image.get_rect()
        self.rect.x =  c * tamanio
        self.rect.y = f * tamanio

        self.posicion_x = c
        self.posicion_y = f

        self.all_sprites = all_sprites
        self.all_bomba = all_bomba
        self.tamanio = tamanio
        
        self.suelo = suelo

        self.all_bomba = all_bomba
        self.all_sprites = all_sprites
        self.all_rompibles = all_rompibles

    def update(self, tecla):
        if tecla == "w":
            if self.suelo[self.posicion_y-1][self.posicion_x] == 0:
                self.posicion_y -= 1
                self.rect.y -= self.tamanio

        elif tecla == "s":
            if self.suelo[self.posicion_y+1][self.posicion_x] == 0:
                self.posicion_y += 1
                self.rect.y += self.tamanio

        elif tecla == "d":
            if self.suelo[self.posicion_y][self.posicion_x+1] == 0:
                self.posicion_x += 1
                self.rect.x += self.tamanio

        elif tecla == "a":
            if self.suelo[self.posicion_y][self.posicion_x-1] == 0:
                self.posicion_x -= 1
                self.rect.x -= self.tamanio

        elif tecla == "S":
            self.SoltarBomba()

    def SoltarBomba(self):
        nueva_bomba = bomba(self.tamanio + 10, self.rect.center, self.posicion_x, self.posicion_y, self.all_bomba, self.all_sprites, self.all_rompibles, self.suelo)
        self.all_bomba.add(nueva_bomba)
        self.all_sprites.add(nueva_bomba)
        
