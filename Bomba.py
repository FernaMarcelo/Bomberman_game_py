import pygame
import os
import time

class bomba(pygame.sprite.Sprite):
    def __init__(self, tamanio, centro, posicion_x, posicion_y, all_bomba, all_sprites, all_rompibles, suelo):
        pygame.sprite.Sprite.__init__(self)
        
        self.bomba = pygame.image.load(os.path.join('Imagenes/Bomba/bomb.png')).convert_alpha()
        self.bomba = pygame.transform.scale(self.bomba, (tamanio, tamanio))
        self.explosion_1 = pygame.image.load(os.path.join('Imagenes/Bomba/exp1.png')).convert_alpha()
        self.explosion_1 = pygame.transform.scale(self.explosion_1, (tamanio, tamanio))
        self.explosion_2 = pygame.image.load(os.path.join('Imagenes/Bomba/exp2.png')).convert_alpha()
        self.explosion_2 = pygame.transform.scale(self.explosion_2, (tamanio, tamanio))
        self.explosion_3 = pygame.image.load(os.path.join('Imagenes/Bomba/exp3.png')).convert_alpha()
        self.explosion_3 = pygame.transform.scale(self.explosion_3, (tamanio, tamanio))

        self.imagenes = [self.bomba, self.explosion_1, self.explosion_2, self.explosion_3]

        self.imagen_actual = 0
        self.image = self.imagenes[self.imagen_actual]
        self.rect = self.image.get_rect()
        self.rect.center = centro

        self.tiempo_inicial = time.time()

        self.posicion_x = posicion_x
        self.posicion_y = posicion_y

        self.all_bomba = all_bomba
        self.all_sprites = all_sprites
        self.all_rompibles = all_rompibles
        self.suelo = suelo
        

    def update(self):
        tiempo_transcurrido = time.time() - self.tiempo_inicial
        if tiempo_transcurrido >= 3:
            self.imagen_actual += 1
            if(self.imagen_actual != len(self.imagenes) - 1):
                self.image = self.imagenes[self.imagen_actual]
            else:
                if(self.imagen_actual == len(self.imagenes) - 1):
                    colision = pygame.sprite.groupcollide(self.all_bomba, self.all_rompibles, False, False)
                    for (bomba, madera_alcanzada) in colision.items():
                        direcciones = [(self.posicion_y + 1, self.posicion_x),
                                       (self.posicion_y - 1, self.posicion_x),
                                       (self.posicion_y, self.posicion_x + 1),
                                       (self.posicion_y, self.posicion_x - 1)]
                        for madera in madera_alcanzada:
                            if (madera.posicion_y, madera.posicion_x) in direcciones:
                                self.suelo[madera.posicion_y][madera.posicion_x] = 0
                                madera.kill()
                    self.kill()