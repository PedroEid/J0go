import pygame
import sys
from pygame.locals import *
from random import randrange
#criando classe bebe
class Bebe (pygame.sprite.Sprite):
    def __init__(self, imbebe, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imbebe)
        self.image=pygame.transform.scale(self.image,(200,200))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
class Mamadeira (pygame.sprite.Sprite):
    def __init__(self, immadeira, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(immadeira)
        self.image=pygame.transform.scale(self.image,(1,1))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
#criando tela
pygame.init()
tela = pygame.display.set_mode([800,600])
pygame.display.set_caption("Bem vindo ao jogo")
fundo = pygame.image.load("fundi1.jpg").convert()
fundo=pygame.transform.scale(fundo,(800,600))

#informacoes classes

pygame.display.set_caption('Baby Fight')
m_normal=Bebe('mamadeira.png',randrange(100),randrange(600))
bebe=Bebe('bbbravo.jpg',randrange(100),randrange(600))

#grupos

bebe_group = pygame.sprite.Group()
bebe_group.add(bebe)
mamadeira_group = pygame.sprite.Group()
mamadeira_group.add(m_normal)
sair = False
while sair!= True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True     
    tela.blit(fundo, (0,0))
    bebe_group.draw(tela)
    mamadeira_group.draw(tela)
    pygame.display.update()
        
pygame.display.quit()
    
    