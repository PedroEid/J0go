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

tela = pygame.display.set_mode([1000,700])
tela.fill(white)

# Criando classe bebe
class Bebe (pygame.sprite.Sprite):
    def __init__(self, imbebe, pos_x, pos_y,tela,vida):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imbebe)
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.vida=vida
        self.health(tela)
        
    def health(self, tela):
        tela.blit(self.image, self.rect)
        pygame.draw.rect(self.image, red, [0,0,self.vida,10])
        
    
##        
class Plataforma(pygame.sprite.Sprite):    
    def __init__(self,pos_x,pos_y, width, height):
        pygame.sprite.Sprite.__init__(self)
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        # Draw the ellipse
        pygame.draw.ellipse(self.image, black, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        
    
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
            
        if self.passos == 30:
            self.movendo = False
        
    # Criando tela.

pygame.init()

tela = pygame.display.set_mode([900,500])
pygame.display.set_caption("Bem vindo ao jogo")

#bebe=[]
#m_normal=[]
bebe_1 = pygame.sprite.Group()
mamadeira_1 = pygame.sprite.Group()
mamadeira_2 = pygame.sprite.Group()
bebe_2 = pygame.sprite.Group()
#plataforma=[]
plataforma_group=pygame.sprite.Group()
#costantes

d_mao_mao = 55
d_mao_pe = 70
by_p=90
#localizacoa bebe:
x = 700
y = 300
ex = 100
ey = 100
#criando os bebes
b_1= Bebe('bbbravo.jpg',x,y,tela,100)
b_2= Bebe('bbbravo.jpg',ex,ey,tela,100)
#criando as plataformas
p_1=Plataforma(x,y+by_p,100,10)
p_2=Plataforma(ex,ey+by_p,100,10)
p_baixo=Plataforma(0,490,10000,10)
#criando mamadeiras
m_1= Mamadeira('mamadeira.png',(x+d_mao_pe),(y+d_mao_mao),5,(-10),(10))
m_2=Mamadeira('mamadeira.png',(ex+d_mao_pe),(ey+d_mao_mao),8,(-10),(10))

#adicionando nos grupos
bebe_1.add(b_1)
bebe_2.add(b_2)
mamadeira_1.add(m_1)
plataforma_group.add(p_baixo)
plataforma_group.add(p_1)
plataforma_group.add(p_2)
mamadeira_2.add(m_2)
#    ex=x
#    ey=y






#Relogio
relogio = pygame.time.Clock()
sair = False
#Looping principal
while not sair:
#    print('b')
    for event in pygame.event.get():
        colisao = pygame.sprite.spritecollide(b_1,mamadeira_2, True)
        
        #saida do jogo
        if event.type == pygame.QUIT:
            sair = True 
            
        #botoes
        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_RETURN:
                print('BANG!')
                m_2.atira()
                z=True
        

            if event.key==pygame.K_LEFT and m_2.rect.x==(ex+d_mao_pe):
                m_2.rect.x-=60
                m_2.vx=-m_2.vx
            if event.key==pygame.K_RIGHT and m_2.rect.x==(ex+d_mao_pe-60):
                   m_2.rect.x+=60
                   m_2.vx=-m_2.vx


    m_2.move()
    tela.fill(white)

    bebe_2.draw(tela)
    bebe_1.draw(tela)
    mamadeira_1.draw(tela)
    mamadeira_2.draw(tela)
    plataforma_group.draw(tela)
    pygame.display.update()
    relogio.tick(FPS)

pygame.display.quit()