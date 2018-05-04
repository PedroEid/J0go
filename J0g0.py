import pygame
import sys
from pygame.locals import *
from random import randrange
#criando classe bebe
class Bebe (pygame.sprite.Sprite):
    def __init__(self, imbebe, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
#        imbebe=pygame.transform.scale(imbebe,(40,40))
        self.image = pygame.image.load(imbebe)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

#criando tela
pygame.init()
tela = pygame.display.set_mode([800,600])
pygame.display.set_caption("Bem vindo ao jogo")
fundo = pygame.image.load("fundi1.jpg").convert()
fundo=pygame.transform.scale(fundo,(800,600))

bebe=Bebe('bbbravo.jpg',randrange(700),randrange(500))
bebe_group = pygame.sprite.Group()
bebe_group.add(bebe)
sair = False
while sair!= True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False     
    tela.blit(fundo, (0,0))
    bebe_group.draw(tela)
    pygame.display.update()
        
pygame.display.quit()
    
    