import pygame
import random
import os
import time
pygame.init()
Explosion = pygame.mixer.Sound('Imagenes/Bomba/Explocion.mp3')
Explosion.set_volume(0.2)
bloques_tamanio = (80, 80)
class Bomb(pygame.sprite.Sprite):
        # Construtor da classe.
        def __init__(self,bottom, centerx,i,j):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)

            self.image = pygame.image.load(os.path.join('Imagenes/Bomba/bomb.png')).convert_alpha()
            self.image = pygame.transform.scale(self.image,bloques_tamanio)
            self.rect = self.image.get_rect()
            self.types=[pygame.image.load(os.path.join('Imagenes/Bomba/bomb.png')).convert_alpha(),
                        pygame.image.load(os.path.join('Imagenes/Bomba/exp1.png')).convert_alpha(),
                        pygame.image.load(os.path.join('Imagenes/Bomba/exp2.png')).convert_alpha(),
                        pygame.image.load(os.path.join('Imagenes/Bomba/exp3.png')).convert_alpha()]
            self.rect.centerx = centerx
            self.rect.bottom = bottom
            self.tempo = 150
            self.expc=centerx
            self.expb=bottom

            self.i = i
            self.j = j

        def update(self):
            self.tempo -= 2 
            if self.tempo>30 and self.tempo<=40:
                self.image=pygame.image.load(os.path.join('Imagenes', 'Bomba', 'exp1.png')).convert_alpha()
                centerx=self.expc
                bottom=self.expb
                self.rect.centerx = centerx
                self.rect.bottom = bottom

            if self.tempo ==30:
               Explosion.play()

                
            if self.tempo<=30 and self.tempo>20:
                self.image=pygame.image.load(os.path.join('Imagenes', 'Bomba', 'exp2.png')).convert_alpha()
                centerx=self.expc
                bottom=self.expb
                self.rect.centerx = centerx
                self.rect.bottom = bottom

                
            if self.tempo<=20 and self.tempo>10:
                self.image=pygame.image.load(os.path.join('Imagenes', 'Bomba', 'exp3.png')).convert_alpha()
                centerx=self.expc
                bottom=self.expb
                self.rect.centerx = centerx
                self.rect.bottom = bottom 
        
            if self.tempo <= 5:
                
                centerx =self.expc
                bottom = self.expb
                self.rect.width *= 1 
                self.rect.height *= 1 
                self.rect.centerx = centerx
                self.rect.bottom = bottom
