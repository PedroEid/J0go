import pygame
import sys
from pygame.locals import *
from random import randrange

# Cores.
white = (255,255,255)
gray = (125,125,125)
black = (0,0,0)
red = (255,0,0)
purple =(150,150,255)
blue=(50,0,255)

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

#        self.health(tela)
        
    def health(self, tela):
        pygame.draw.rect(self.image,white,[0,0,100,5])
        if self.vida>0:
            pygame.draw.rect(self.image, red, [0,0,self.vida,5])
        
    
#criando classe de plataforma       
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
        
#criando classe de mamadeira    
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
    def parar_atirar(self):
        self.movendo=False
    def move(self):
        if self.movendo:
            self.vy += self.g/FPS
            self.rect.x += self.vx
            self.rect.y += self.vy
            self.passos += 1
            
        if self.passos == 90:
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
trocou_de_mao=False
atirou=False
inicio=True
#Looping principal
while not sair:
#    print('b')

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
                sair = True
        if inicio:
            font = pygame.font.SysFont("Algerian", 50)
            text = font.render("Bem Vindo ao Baby Fight", True, (black))
            font1 = pygame.font.SysFont("Algerian", 32)
            text1 = font1.render("Jogar", True, (blue))



            
        else:

            if event.type == pygame.KEYDOWN:                
                    if event.key== pygame.K_RETURN:
                        vy_inicial=m_2.vy
                        m_2.atira()
                        atirou=True
                    if event.key==pygame.K_LEFT and not trocou_de_mao and not atirou:
                        m_2.rect.x-=60
                        m_2.vx=-m_2.vx
                        trocou_de_mao=True
                        
                    if event.key==pygame.K_RIGHT and trocou_de_mao and not atirou:
                            m_2.rect.x+=60
                            m_2.vx=-m_2.vx
                            trocou_de_mao=False
                    if event.key==pygame.K_UP and not atirou:
                        m_2.vy-=2
                    if event.key==pygame.K_DOWN and not atirou:
                        m_2.vy+=2
                    if event.key==pygame.K_d:
                        b_2.rect.x+=20
                        m_2.rect.x+=20
                    if event.key==pygame.K_a:
                        b_2.rect.x-=20
                        m_2.rect.x-=20
                    if event.key==pygame.K_w:
                        b_2.rect.y-=20
                        m_2.rect.y-=20
    #                        a=False
                    
    #    gravidade=pygame.sprite.spritecollide(b_1,plataforma_group, True)
    #    if gravidade:
    #        b_2.rect.y+=2
    #        m_2.rect.y+=2
            

            
            
    colisao = pygame.sprite.spritecollide(b_1,mamadeira_2, False)
    colisao1=pygame.sprite.spritecollide(m_2,plataforma_group, False)
    if colisao1 or colisao:
        m_2.vy=vy_inicial
        m_2.rect.x=ex+d_mao_pe
        m_2.rect.y=ey+d_mao_mao
        m_2.parar_atirar()
        print("a")
        if colisao:
            b_1.vida-=20
            b_1.health(tela)
        atirou=False
    if not inicio:
        tela.fill(white)
        m_2.move()
        bebe_2.draw(tela)
        bebe_1.draw(tela)
        mamadeira_1.draw(tela)
        mamadeira_2.draw(tela)
        plataforma_group.draw(tela)

    else:
        tela.fill(purple)
        tela.blit(text,(420 - text.get_width() // 2, 130 - text.get_height() // 2))
        t=tela.blit(text1,(420 - text1.get_width() // 2, 330 - text1.get_height() // 2))
        if event.type == pygame.MOUSEBUTTONDOWN:            
            mouse_posicao=pygame.mouse.get_pos()
            if t.collidepoint(mouse_posicao):
                inicio=False
    pygame.display.update()
    relogio.tick(FPS)

pygame.display.quit()