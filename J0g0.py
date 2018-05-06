import pygame
import sys
from pygame.locals import *
from random import randrange
#cores
white=(255,255,255)
gray=(125,125,125)
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
    def __init__(self, immadeira, pos_x, pos_y,vel_x,vel_y,g):
        self.vx=vel_x
        self.vy=vel_y
        self.g=g
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(immadeira)
        self.image=pygame.transform.scale(self.image,(20,20))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    def move(self):
        self.rect.x+=self.vx
        self.rect.y+=self.vy+ 1/2*self.g
    #criando tela
pygame.init()
tela = pygame.display.set_mode([800,600])
pygame.display.set_caption("Bem vindo ao jogo")
bebe=[]
bebe_group = pygame.sprite.Group()
mamadeira_group=pygame.sprite.Group()
for i in range(randrange(2,4)):
    z=randrange(700)
    bebe+=[Bebe('bbbravo.jpg',z,300)]
    bebe_group.add(bebe[i])
    m_normal=Mamadeira('mamadeira.png',(z+81),355,10,(-10),(8))
#criando grupos
    mamadeira_group.add(m_normal)
#Relogio
relogio=pygame.time.Clock()
sair = False
while sair!= True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sair = True 
        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_BACKSPACE:
                m_normal.move()    
    tela.fill(white)
    bebe_group.draw(tela)
    mamadeira_group.draw(tela)
    pygame.display.update()
    relogio.tick(10)
pygame.display.quit()
    
    