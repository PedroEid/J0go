import pygame
import sys
from pygame.locals import *
from random import randrange
#cores
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
#criando classe bebe
class Bebe (pygame.sprite.Sprite):
    def __init__(self, imbebe, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imbebe)
        self.image=pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
class Mamadeira (pygame.sprite.Sprite):
    def __init__(self, immadeira, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(immadeira)
        self.image=pygame.transform.scale(self.image,(20,20))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
#criando tela
pygame.init()
tela = pygame.display.set_mode([800,600])
pygame.display.set_caption("Bem vindo ao jogo")


bebe=Bebe('bbbravo.jpg',100,300)
m_normal=Mamadeira('mamadeira.png',181,355)
#criando grupos
bebe_group = pygame.sprite.Group()
mamadeira_group=pygame.sprite.Group()
bebe_group.add(bebe)
mamadeira_group.add(m_normal)
sair = False
while sair!= True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sair = True     
    tela.fill(white)
    bebe_group.draw(tela)
    mamadeira_group.draw(tela)
    pygame.display.update()
        
pygame.display.quit()
    
    