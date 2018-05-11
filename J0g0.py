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
    def _init_(self, imbebe, pos_x, pos_y,tela,vida):
        pygame.sprite.Sprite._init_(self)
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
    def _init_(self,pos_x,pos_y, width, height):
        pygame.sprite.Sprite._init_(self)
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        # Draw the ellipse
        pygame.draw.ellipse(self.image, black, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        
    
class Mamadeira (pygame.sprite.Sprite):
    def _init_(self, immadeira, pos_x, pos_y,vel_x,vel_y,g):
        pygame.sprite.Sprite._init_(self)
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

bebe=[]
m_normal=[]
bebe_group = pygame.sprite.Group()
mamadeira_group = pygame.sprite.Group()
plataforma=[]
plataforma_group=pygame.sprite.Group()
ex = 0
ey = 0
d_mao_mao = 55
d_mao_pe = 70

for i in range(randrange(2,4)):
    x = randrange(700)
    y = randrange(400)
    bebe += [Bebe('bbbravo.jpg',x,y,tela,100)]
    plataforma+=[Plataforma(x,y+90,100,10)]
    bebe_group.add(bebe[i])
    m_normal+= [Mamadeira('mamadeira.png',(x+d_mao_pe),(y+d_mao_mao),10,(-10),(10))]
    mamadeira_group.add(m_normal[i])
    plataforma_group.add(plataforma[i])
    sua_m=m_normal[i]
    ex=x
    ey=y
plataforma+=[Plataforma(0,450,10000,10)]
plataforma_group.add(plataforma[i+1])

#criando grupos
#Relogio
relogio = pygame.time.Clock()
sair = False
z=False
while not sair:
#    print('b')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True 
        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_RETURN:
                print('BANG!')
                sua_m.atira()
                z=True
#            colisao = pygame.sprite.spritecollide(sua_m,bebe_group, z)
#            print(colisao)

            if event.key==pygame.K_LEFT and sua_m.rect.x==(x+d_mao_pe):
                sua_m.rect.x-=60
                sua_m.vx=-sua_m.vx
            if event.key==pygame.K_RIGHT and sua_m.rect.x==(x+d_mao_pe-60):
                   sua_m.rect.x+=60
                   sua_m.vx=-sua_m.vx

    sua_m.move()
    tela.fill(white)

    bebe_group.draw(tela)
    mamadeira_group.draw(tela)
    plataforma_group.draw(tela)
    pygame.display.update()
    relogio.tick(FPS)

pygame.display.quit()