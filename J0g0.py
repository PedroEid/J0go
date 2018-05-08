import pygame
import sys
from pygame.locals import *
from random import randrange

# Cores.
white = (255,255,255)
gray = (125,125,125)
black = (0,0,0)
red = (255,0,0)

FPS = 30

# Criando classe bebe
class Bebe (pygame.sprite.Sprite):
    def __init__(self, imbebe, pos_x, pos_y,tela):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imbebe)
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        
        
    def draw(self, tela):
        print('a')
        tela.blit(self.image, self.rect)
        
    
        
        

class Mamadeira (pygame.sprite.Sprite):
    def __init__(self, immadeira, pos_x, pos_y,vel_x,vel_y,g):
        pygame.sprite.Sprite.__init__(self)
        self.vx = vel_x
        self.vy = vel_y
        self.g = g
        self.image = pygame.image.load(immadeira)
        self.image = pygame.transform.scale(self.image,(20,20))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.movendo = False
        self.passos = 0  # DEBUG
        
        
    def atira(self):
        
        self.movendo = True

    def move(self):
        if self.movendo:
            self.vy += self.g/FPS
            self.rect.x += self.vx
            self.rect.y += self.vy
            self.passos += 1
            
        if self.passos == 10:
            self.movendo = False
        
    # Criando tela.

pygame.init()

tela = pygame.display.set_mode([1000,700])
pygame.display.set_caption("Bem vindo ao jogo")

bebe=[]
m_normal=[]
bebe_group = pygame.sprite.Group()
mamadeira_group = pygame.sprite.Group()
plataforma=[]
plataforma_group=pygame.sprite.Group
ex = 0
ey = 0
d_mao_mao = 55
d_mao_pe = 70
for i in range(randrange(2,4)):
    x = randrange(700)
    y = randrange(400)
    while (x - ex) < 70:
        x = randrange(700)
    while (y - ey) < 70:
        y = randrange(500)
    bebe += [Bebe('bbbravo.jpg',x,y,tela)]
#    plataforma+=[pygame.draw.rect(tela, black, [x,y,100,10])]
    bebe_group.add(bebe[i])
    m_normal+= [Mamadeira('mamadeira.png',(x+d_mao_pe),(y+d_mao_mao),10,(-10),(10))]
    mamadeira_group.add(m_normal[i])
#    plataforma_group.add(plataforma[i])
    sua_m=m_normal[i]
    ex=x
    ey=y
#plataforma_group.add(pygame.draw.rect(tela, black, [1000,600,-1000,10]))
#criando grupos
#Relogio
relogio = pygame.time.Clock()
sair = False
while not sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True 
        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_RETURN:
                print('BANG!')
                sua_m.atira()
            if event.key==pygame.K_LEFT and sua_m.rect.x==(x+d_mao_pe):
                sua_m.rect.x-=60
                sua_m.vx=-sua_m.vx
            if event.key==pygame.K_RIGHT and sua_m.rect.x==(x+d_mao_pe-60):
                   sua_m.rect.x+=60
                   sua_m.vx=-sua_m.vx

    sua_m.move()

    tela.fill(white)
#    plataforma_group.draw(tela)
    bebe_group.draw(tela)
    bebe_group.draw(tela)
    mamadeira_group.draw(tela)
    pygame.display.update()
    relogio.tick(FPS)

pygame.display.quit()
    
    