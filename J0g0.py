import pygame
import sys
from pygame.locals import *
from random import randrange

# Cores.
white = (255,255,255)
gray = (125,125,125)
green = (0,50,0)
black=(0,0,0)
red = (255,0,0)
purple =(150,150,255)
blue=(20,20,255)

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
    def gravidade(self,gravidade):
        if gravidade:
            self.rect.y+=10
        
    
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
tela_y=500
tela_x=900
tela = pygame.display.set_mode([tela_x,tela_y])
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
#dimensoes do bebe
d_mao_mao = 60
d_mao_pe = 70
by_p=90
#localizacoa bebe:
x = tela_x-200
y = tela_y-200
ex = tela_x-800
ey = tela_y-400
#criando os bebes
b_1= Bebe('bbbravo.jpg',x,y,tela,100)
b_2= Bebe('bbbravo.jpg',ex,ey,tela,100)
#criando as plataformas
p_1=Plataforma(x,y+by_p,100,10)
p_2=Plataforma(ex,ey+by_p,100,10)
p_baixo=Plataforma(0,tela_y-10,10000,100)
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
rules=False
pulou=False
#Looping principal
while not sair:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
                sair = True
        if inicio:
            font = pygame.font.SysFont("Algerian", (tela_x-850))
            text = font.render("Bem Vindo ao Baby Fight", True, (green))
            font1 = pygame.font.SysFont("Algerian", tela_x-872)
            font2= pygame.font.SysFont("Algerian", tela_x-880)
            text1 = font1.render("Jogar", True, (blue))
            regras=font2.render("Regras",True,blue)
        elif rules:
            font3=pygame.font.SysFont('Aharoni',tela_x-20)
            regra0=font1.render("REGRAS", True, (black))
            regra1=font3.render("SETAS PARA CIMA E BAIXO = CONTROLE DA ALTURA DO TIRO", True, (green))
            regra2=font3.render("SETAS PARA OS LADOS = CONTROLE DA DIREÇAO DO TIRO", True, (green))
            regra3=font3.render("TECLAS W,A,D = MOVIMENTO DO BEBE",True,green)
            voltar=font2.render("VOLTAR",True,black)


            
        else:

            if event.type == pygame.KEYDOWN:  
                    vy_inicial=m_2.vy
                    if event.key== pygame.K_RETURN:
                        m_2.atira()
                        atirou=True
                    if event.key==pygame.K_LEFT and not trocou_de_mao and not atirou:
                        m_2.rect.x-=d_mao_mao
                        m_2.vx=-m_2.vx
                        trocou_de_mao=d_mao_mao
                        
                    if event.key==pygame.K_RIGHT and trocou_de_mao and not atirou:
                            m_2.rect.x+=d_mao_mao
                            m_2.vx=-m_2.vx
                            trocou_de_mao=False
                    if event.key==pygame.K_UP and not atirou:
                        m_2.vy-=tela_y-498
                    if event.key==pygame.K_DOWN and not atirou:
                        m_2.vy+=tela_y-498
                    if event.key==pygame.K_d and b_2.rect.x<(900-d_mao_mao-50):
                        b_2.rect.x+=20
                        m_2.rect.x+=20
                    if event.key==pygame.K_a and b_2.rect.x>0:
                        b_2.rect.x-=20
                        m_2.rect.x-=20
                    if event.key==pygame.K_w and not pulou:
                        pulou=True
                        b_2.rect.y-=200
                        m_2.rect.y-=200
    #                        a=False
                   
    gravidade=pygame.sprite.spritecollide(b_2,plataforma_group, False)
    print(gravidade)
    if not gravidade:
        b_2.rect.y+=5
        m_2.rect.y+=5
    else:
        pulou=False

            
    m_2.move()        
    colisao = pygame.sprite.spritecollide(b_1,mamadeira_2, False)
    colisao1=pygame.sprite.spritecollide(m_2,plataforma_group, False)
    if colisao1 or colisao:
        m_2.vy=vy_inicial
        m_2.rect.x=b_2.rect.x+d_mao_pe
        m_2.rect.y=b_2.rect.y+d_mao_mao
        m_2.parar_atirar()
        if colisao:
            b_1.vida-=20
            b_1.health(tela)
            if b_1.vida==0:
                bebe_1.remove(b_1)
                mamadeira_1.remove(m_1)
        atirou=False
    if not inicio and not rules:
        tela.fill(white)
        bebe_2.draw(tela)
        bebe_1.draw(tela)
        mamadeira_1.draw(tela)
        mamadeira_2.draw(tela)
        plataforma_group.draw(tela)

    elif inicio:
        tela.fill(purple)
        tela.blit(text,(420 - text.get_width() // 2, 130 - text.get_height() // 2))
        jogar=tela.blit(text1,(420 - text1.get_width() // 2, 230 - text1.get_height() // 2))
        rule=tela.blit(regras,(432 - text1.get_width() // 2, 290 - text1.get_height() // 2))
        if event.type == pygame.MOUSEBUTTONDOWN:            
            mouse_posicao=pygame.mouse.get_pos()
            if jogar.collidepoint(mouse_posicao):
                inicio=False
                volt=False
            elif rule.collidepoint(mouse_posicao):
                inicio=False
                rules=True
    elif rules:
        tela.fill(gray)
        tela.blit(regra0,(420 - text.get_width() // 2, 130 - text.get_height() // 2))
        tela.blit(regra1,(420 - text1.get_width() // 2, 230 - text1.get_height() // 2))
        tela.blit(regra2,(420 - text1.get_width() // 2, 330 - text1.get_height() // 2))
        tela.blit(regra3,(420 - text1.get_width() // 2, 430 - text1.get_height() // 2))
        volt=tela.blit(voltar,(170 - text1.get_width() // 2, 430 - text1.get_height() // 2))
        if event.type == pygame.MOUSEBUTTONDOWN:            
            mouse_posicao=pygame.mouse.get_pos()
            if volt.collidepoint(mouse_posicao):
                rules=False
                inicio=True
    pygame.display.update()
    relogio.tick(FPS)

pygame.display.quit()