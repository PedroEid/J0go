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


        
    def health(self):
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
        self.image = pygame.transform.scale(self.image,(30,30))
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
p_baixo_direita=Plataforma(0,tela_y-10,10000,100)
p_baixo_esquerda=Plataforma(0,1000+tela_y-10,(10000),100)
plataforma_group.add(p_baixo_direita)
plataforma_group.add(p_baixo_esquerda)
plataforma_group.add(p_1)
plataforma_group.add(p_2)
#criando mamadeiras
m_1= Mamadeira('mamadeira2.png',(x+d_mao_pe),(y+d_mao_mao-10),10,(-10),(10))
m_2=Mamadeira('mamadeira2.png',(ex+d_mao_pe),(ey+d_mao_mao-10),8,(-10),(10))

#adicionando nos grupos
bebe_1.add(b_1)
bebe_2.add(b_2)
mamadeira_1.add(m_1)

mamadeira_2.add(m_2)
#    ex=x
#    ey=y






#Relogio
relogio = pygame.time.Clock()
sair = False
inicio=True
rules=False
trocou_de_mao=False
atirou=False


movimento_1=False
m_bebe=0
b=0
vx_inicial=m_2.vx
#Looping principal
vy_inicial=m_2.vy
while not sair:
    m_2.move()
    m_1.move()  
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
            font3=pygame.font.SysFont('Aharoni',tela_x-880)
            regra0=font1.render("REGRAS", True, (black))
            regra1=font3.render("SETAS PARA CIMA E BAIXO = CONTROLE DA ALTURA DO TIRO", True, (green))
            regra2=font3.render("SETAS PARA OS LADOS = CONTROLE DA DIREÇAO DO TIRO", True, (green))
            regra3=font3.render("TECLAS W,A,D = MOVIMENTO DO BEBE",True,green)
            voltar=font2.render("VOLTAR",True,black)


        else:    
            if not movimento_1:
                
                if event.type == pygame.KEYDOWN:  
                        
                        if event.key== pygame.K_RETURN:
                            m_2.atira()
                            atirou=True
                            m_bebe=3
    
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
                            b_2.rect.x+=50
                            m_2.rect.x+=50
                            m_bebe+=1
                            
                        if event.key==pygame.K_a and b_2.rect.x>0:
                            b_2.rect.x-=50
                            m_2.rect.x-=50
                            m_bebe+=1
                        
                        if event.key==pygame.K_w:
                           
                            b_2.rect.y-=200
                            m_2.rect.y-=200
                            m_bebe+=1
                        vy_inicial2=m_2.vy
            if movimento_1:               
                if event.type == pygame.KEYDOWN:  
                    vy_inicial1=m_1.vy
                    if event.key== pygame.K_RETURN:
                        m_1.atira()
                        atirou=True
                        m_bebe=0
                    if event.key==pygame.K_LEFT and not trocou_de_mao and not atirou:
                        m_1.rect.x-=d_mao_mao
                        m_1.vx=-m_1.vx
                        trocou_de_mao=True
                    if event.key==pygame.K_RIGHT and trocou_de_mao and not atirou:
                            m_1.rect.x+=d_mao_mao
                            m_1.vx=-m_1.vx
                            trocou_de_mao=False

                        
                    if event.key==pygame.K_UP and not atirou:
                        m_1.vy-=tela_y-498

                    if event.key==pygame.K_DOWN and not atirou:
                        m_1.vy+=tela_y-498
                    if event.key==pygame.K_d and b_1.rect.x<(900-d_mao_mao-50):
                        b_1.rect.x+=50
                        m_1.rect.x+=50
                        m_bebe-=1

                    if event.key==pygame.K_a and b_1.rect.x>0:
                        b_1.rect.x-=50
                        m_1.rect.x-=50
                        m_bebe-=1

                    if event.key==pygame.K_w:
                        
                        b_1.rect.y-=200
                        m_1.rect.y-=200
                        m_bebe-=1
                    vy_inicial1=m_1.vy
    if m_bebe<=0:
        movimento_1=False
    if m_bebe>3:
        movimento_1=True                
#gravidade do bebe2                    
    gravidade2=pygame.sprite.spritecollide(b_2,plataforma_group, False)
    if not gravidade2:
        b_2.rect.y+=5
        m_2.rect.y+=5
        
        
        
        
#gravidade do bebe2        
    gravidade1=pygame.sprite.spritecollide(b_1,plataforma_group, False)
    
    if not gravidade1:
        b_1.rect.y+=5
        m_1.rect.y+=5
            
#colisao do bebe2            
    colisao_b_m2= pygame.sprite.spritecollide(b_1,mamadeira_2, False)
    colisao_m_p2=pygame.sprite.spritecollide(m_2,plataforma_group, False)
    if colisao_b_m2 or colisao_m_p2 or m_2.rect.x>900 or m_2.rect.x<0 or m_2.rect.y<-500:
        m_2.vy=vy_inicial2
        m_2.rect.x=b_2.rect.x+d_mao_pe
        m_2.rect.y=b_2.rect.y+d_mao_mao-10
        m_2.parar_atirar()
        if colisao_b_m2:
            b_1.vida-=20
            b_1.health()
            if b_1.vida==0:
                bebe_1.remove(b_1)
                mamadeira_1.remove(m_1)
        trocou_de_mao=False
        movimento_1=True
        atirou=False
        m_2.vx=vx_inicial
#colisao do bebe1       
    colisao_b_m1 = pygame.sprite.spritecollide(b_2,mamadeira_1, False)
    colisao_m_p1=pygame.sprite.spritecollide(m_1,plataforma_group, False)
    if colisao_b_m1 or colisao_m_p1 or m_1.rect.x>900 or m_1.rect.x<0 or m_1.rect.y<-500:
        m_1.vy=vy_inicial1
        m_1.rect.x=b_1.rect.x+d_mao_pe
        m_1.rect.y=b_1.rect.y+d_mao_mao-10
        m_1.parar_atirar()
        if colisao_b_m1:
            b_2.vida-=20
            b_2.health()
        trocou_de_mao=False
        movimento_1=False
        atirou=False

        m_1.vx=vx_inicial
        
#desenho do jogo

    if not inicio and not rules:
        tela.fill(white)
        bebe_1.draw(tela)
        bebe_2.draw(tela)
        plataforma_group.draw(tela)
        mamadeira_1.draw(tela)
        mamadeira_2.draw(tela)
        if b_2.vida<=0 or b_1.vida<=0:
            if b_2.vida<=0:
                bebe_2.remove(b_2)
            if b_1.vida<=0:
                bebe_1.remove(b_1)
            mamadeira_2.remove(m_2)
            mamadeira_1.remove(m_1)
            final=font1.render("Parabens, você fez o bebe chorar, seu monstro", True, (green))
            final_jogar=font3.render("Jogar de novo", True, (blue))
            tela.blit(final,(420 - text.get_width() // 2, 130 - text.get_height() // 2))
            jogar_de_novo=tela.blit(final_jogar,(170 - text1.get_width() // 2, 430 - text1.get_height() // 2))
            if event.type == pygame.MOUSEBUTTONDOWN:            
                mouse_posicao=pygame.mouse.get_pos()
            if jogar_de_novo.collidepoint(mouse_posicao):
                inicio=True
                rules=False
                bebe_2 = pygame.sprite.Group()
                bebe_1 = pygame.sprite.Group()
                b_1= Bebe('bbbravo.jpg',x,y,tela,100)
                b_2= Bebe('bbbravo.jpg',ex,ey,tela,100)
                #criando mamadeiras
                m_1= Mamadeira('mamadeira2.png',(x+d_mao_pe),(y+d_mao_mao-10),10,(-10),(10))
                m_2=Mamadeira('mamadeira2.png',(ex+d_mao_pe),(ey+d_mao_mao-10),8,(-10),(10))
                #adicionando nos grupos
                bebe_1.add(b_1)
                bebe_2.add(b_2)
                mamadeira_1.add(m_1)
                mamadeira_2.add(m_2)
        elif m_bebe<=0 or m_bebe>=3:
            if m_bebe<=0:
                vez=font3.render("Vez do player 1", True, (black))
            else:
                vez=font3.render("Vez do player 2", True, (black))
            tela.blit(vez,(450 - text1.get_width() // 2, 100 - text1.get_height() // 2))
        

                

#desenho tela de inicio
    elif inicio:
        tela.fill(purple)
        tela.blit(text,(420 - text.get_width() // 2, 130 - text.get_height() // 2))
        jogar=tela.blit(text1,(420 - text1.get_width() // 2, 230 - text1.get_height() // 2))
        rule=tela.blit(regras,(432 - text1.get_width() // 2, 290 - text1.get_height() // 2))
        trocou_de_mao=False
        atirou=False        
        movimento_1=False
        m_bebe=0
        b=0
        vx_inicial=m_2.vx
        if event.type == pygame.MOUSEBUTTONDOWN:            
            mouse_posicao=pygame.mouse.get_pos()
            if jogar.collidepoint(mouse_posicao):
                inicio=False
                rules=False
            elif rule.collidepoint(mouse_posicao):
                inicio=False
                rules=True


#desenho tela de regras
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