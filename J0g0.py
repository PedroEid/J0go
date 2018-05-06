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
        self.vy+=1/2*self.g
        self.rect.y+=self.vy 
    #criando tela
pygame.init()
tela = pygame.display.set_mode([800,600])
pygame.display.set_caption("Bem vindo ao jogo")
bebe=[]
bebe_group = pygame.sprite.Group()
mamadeira_group=pygame.sprite.Group()
ex=0
ey=0
for i in range(randrange(2,4)):
    x=randrange(700)
    y=randrange(400)
    while (x-ex)<70:
        x=randrange(700)
    while (y-ey)<70:
        y=randrange(500)
    bebe+=[Bebe('bbbravo.jpg',x,y)]
    bebe_group.add(bebe[i])
    pygame.draw.rect(tela, gray, [x-30,y-30,100,10])
    m_normal=Mamadeira('mamadeira.png',(x+70),(y+55),10,(-50),(8))
    ex=x
    ey=y
#criando grupos
    mamadeira_group.add(m_normal)
#Relogio
relogio=pygame.time.Clock()
sair = False
while sair!= True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True 
        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_BACKSPACE:
                m_normal.move()
            if event.key==pygame.K_LEFT and m_normal.rect.x==(x+70):
                m_normal.rect.x-=60
                m_normal.vx=-m_normal.vx
            if event.key==pygame.K_RIGHT and m_normal.rect.x==(x+70-60):
                    m_normal.rect.x+=60
                    m_normal.vx=-m_normal.vx
    tela.fill(white)
    bebe_group.draw(tela)
    mamadeira_group.draw(tela)
    pygame.display.update()
    relogio.tick(10)
pygame.display.quit()
    
    