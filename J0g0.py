import pygame
import sys
from pygame.locals import *
from random import randrange
#criando classe bebe
class Bebe (pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem, pos_x, pos_y):
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

#criando tela
pygame.init()
tela = pygame.display.set_mode([800,600])
pygame.display.set_caption("Bem vindo ao jogo")
fundo = pygame.image.load("fundi1.jpg").convert()
bebe=Bebe('bbbravo.jpg',randrange(40),randrange(40))
bebe_group = pygame.sprite.Group()
sair = False
while sair!= True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False     
    tela.blit(fundo, (0, 0))
    bebe_group.draw(tela)
    pygame.display.update()
        
pygame.display.quit()
    
    