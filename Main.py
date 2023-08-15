# Librerias necesarias
import requests
import time
import pygame
import os
import random
import sys
from Escenario import irrompible, rompible
from Jugador import jugador
import socket
import threading

SERVER_IP = '127.0.0.1'  # Reemplaza con la dirección IP del servidor Linux
SERVER_PORT = 65000
# Configuración del socket del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect((SERVER_IP, SERVER_PORT))
except socket.error as message:
    print("Fallo la conecxion")
    print(message)
    sys.exit()
msg   = client_socket.recv(256)
idjug = msg.decode('utf-8').split("\n")
print("ASIGNADO:", idjug[0])
#***************************************************************************************
    
# Constantes
bloques_tamanio = 40
suelo = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
         [-1, 3, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1],
         [-1, 0, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],
         [-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1],
         [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],
         [-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1],
         [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],
         [-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1],
         [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],
         [-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1],
         [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],
         [-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1],
         [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],
         [-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 4, -1],
         [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

# Cosas de la ventana
ancho_ventana = 760
alto_ventana = 600
ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Bomberman")

#Reloj
clock = pygame.time.Clock()
fps = 30


# Grupos de sprites
all_rompibles = pygame.sprite.Group()
all_irrompibles = pygame.sprite.Group()
all_jugador1 = pygame.sprite.Group()
all_jugador2 = pygame.sprite.Group()
all_bombas = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

print("3")
game_over = False

for f in range(len(suelo)):
    for c in range(len(suelo[f])):
        if suelo[f][c] == -1:
            all_irrompibles.add(irrompible(c, f, bloques_tamanio))
        elif suelo[f][c] == 1:
            azar = random.randint(1, 4)
            if azar == 1 or azar == 3:
                madera = rompible(c, f, bloques_tamanio)
                all_rompibles.add(madera)
                suelo[f][c] = 1
            else:
                suelo[f][c] = 0
        elif suelo[f][c] == 3:
            jugador1 = jugador(c, f, all_bombas, all_sprites, all_rompibles, bloques_tamanio, suelo, all_jugador1)
            all_jugador1.add(jugador1)
            suelo[f][c] = 0
        elif suelo[f][c] == 4:
            jugador2 = jugador(c, f, all_bombas, all_sprites, all_rompibles, bloques_tamanio, suelo, all_jugador2)
            all_jugador2.add(jugador2)
            suelo[f][c] = 0


all_sprites.add(all_irrompibles)
all_sprites.add(all_rompibles)
all_sprites.add(all_jugador1)
all_sprites.add(all_jugador2)
print("4")
while(game_over == False):
    # Eventitos que van sucediendo
    for evento in pygame.event.get():
        # Evento por si apretan la X de la ventana
        if evento.type == pygame.QUIT:
            game_over = True
    ventana.fill((255, 192, 203))

    # Se guarda la tecla que se vaya a presionar
    tecla = pygame.key.get_pressed()
    out=(" ").encode('utf-8')
    #*****************************************************
    # Inicia un hilo para enviar mensajes a otros clientes
    if tecla[pygame.K_w]:
        out = ("w").encode('utf-8')
    elif tecla[pygame.K_s]:
        out = ("s").encode('utf-8')
    elif tecla[pygame.K_d]:
        out = ("d").encode('utf-8')
    elif tecla[pygame.K_a]:
        out = ("a").encode('utf-8')
    elif tecla[pygame.K_SPACE]:
        out = ("S").encode('utf-8')
    client_socket.send(out)
    #*****************************************************
    # Inicia un hilo para recibir mensajes del servidor
    msg = client_socket.recv(256)
    lst = msg.decode('utf-8').split(";")
    print(lst[1],lst[0])
    jugador1.update(lst[1])
    jugador2.update(lst[0])
    #*****************************************************
    all_bombas.update()
    # Dibujos
    all_sprites.draw(ventana)
    # Se renderiza el juego desde acá
    pygame.display.flip()
    # Limita el juego a 60 FPS
    clock.tick(fps) 
pygame.quit()
