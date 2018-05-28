import pygame
import sys
from pygame.locals import *
from random import randrange
import pygame.mixer


# Cores.
white = (255,255,255)
gray = (125,125,125)
green = (0,50,0)
black=(0,0,0)
red = (255,0,0)
purple =(150,150,255)
blue=(20,20,255)
azul=(0,200,250)

FPS = 60
grav=20
tela_y=500
tela_x=900
tela = pygame.display.set_mode([tela_x,tela_y])
tela.fill(black)
#fundo = pygame.image.load("ceu.png").convert()
#fundo = pygame.transform.scale(fundo,(tela_x,tela_y))

pygame.mixer.pre_init()
pygame.init()


relogio = pygame.time.Clock()
choro = pygame.mixer.Sound('choro2.ogg')
musica = pygame.mixer.Sound('music.ogg')


# Criando classe bebe
class Bebe (pygame.sprite.Sprite):
    def __init__(self, imbebe, pos_x, pos_y,tela,vida,cortex1,cortex2):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imbebe)       
        self.image = pygame.transform.scale(self.image,(180,150))
        self.image=pygame.transform.chop(self.image, (132, 120, cortex1,30 ))
        self.image=pygame.transform.chop(self.image, (0, 0, cortex2, 15))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.vida=vida


        
    def health(self):
        pygame.draw.rect(self.image,white,[0,0,100,3])
        if self.vida>0:
            pygame.draw.rect(self.image, red, [0,0,self.vida,3])
        
    
#criando classe de plataforma
class Imagens(pygame.sprite.Sprite):    
    def __init__(self,pos_x,pos_y, imagem,tamx, tamy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagem)       
        self.image = pygame.transform.scale(self.image,(120,100))
        self.image=pygame.transform.chop(self.image, (0, 65,0 ,35 ))
        self.image=pygame.transform.chop(self.image, (0, 0, 0, 40))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        
class Parede(pygame.sprite.Sprite):    
    def __init__(self,pos_x,pos_y, width, height,cor):
        pygame.sprite.Sprite.__init__(self)
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        # Draw the ellipse
        pygame.draw.ellipse(self.image, cor, [10, 10, width, height])
        self.image.fill(cor)
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
        self.image = pygame.transform.scale(self.image,(40,40))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.movendo = False
        self.passos = 0  # DEBUG
        self.pre_vy=self.vy 
        self.pre_x=self.rect.x-10 
        self.pre_y=self.rect.y
        self.pre_vx=self.vx

    def atira(self):
        self.movendo = True
    def parar_atirar(self):
        self.movendo=False
    def move(self):
        if self.movendo:
            self.vy += self.g/FPS
            self.rect.x += self.vx
            self.rect.y += self.vy
    def pre_move(self,tela):
        lista=[]
        self.pre_vy=self.vy 
        self.pre_x=self.rect.x+10
        self.pre_y=self.rect.y+25
        self.pre_vx=self.vx
        lista.append([self.pre_x,self.pre_y])    
        for i in range(20):
            self.pre_vy+= self.g/FPS        
            self.pre_x+=self.pre_vx
            self.pre_y+= self.pre_vy
            lista.append([self.pre_x,self.pre_y])
            listapre=[lista[i],lista[i+1]]
            if i%2!=0:
                pygame.draw.aalines(tela,blue ,False,listapre)
                

font = pygame.font.SysFont("Algerian", (tela_x-850))
text = font.render("Bem Vindo ao Baby Fight", True, (green))
font1 = pygame.font.SysFont("Algerian", tela_x-872)
font2= pygame.font.SysFont("Algerian", tela_x-880)
font3=pygame.font.SysFont('Aharoni',tela_x-880)
text1 = font1.render("Jogar", True, (blue))
controles=font2.render("Controles",True,blue)
regras=font2.render("Regras",True,blue)
#Controles
controle0=font1.render("CONTROLES", True, (black))
controle1=font3.render("SETAS PARA CIMA & BAIXO = CONTROLA A INCLINAÇÃO DO TIRO", True, (green))
controle2=font3.render("SETAS PARA OS LADOS = CONTROLE DA DIREÇÃO DO TIRO", True, (green))
controle3=font3.render("TECLAS A, BARRA DE ESPAÇO & D = MOVIMENTO DO BEBE",True,(green))
controle4=font3.render('TECLAS W & S = VELOCIDADE DO TIRO',True,(green))
#Regras
regra0=font2.render("REGRAS",True,blue)
regra1=font3.render("NESSE JOGO O SEU OBJETIVO É ACABAR COM OS OUTROS BEBES,", True, (green))
regra2=font3.render("MAS NÃO FAÇA ISSO ELES SÃO APENAS BEBES", True, (green))
regra3=font3.render("CADA JOGADOR TEM 3 MOVIMENTOS OU UM TIRO",True,green)
regra4=font3.render("NÃO USE HACK, CASO CONTRÁRIO FICARA DE CASTIGO",True,green)
voltar=font2.render("VOLTAR",True,black)

                
    # Criando tela.

pygame.init()

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
paredeb=pygame.sprite.Group()
paredele=pygame.sprite.Group()
paredeld=pygame.sprite.Group()
lava=pygame.sprite.Group()
#costantes
#dimensoes do bebe
d_mao_mao = 50
d_mao_pe = 70
by_p=90
#localizacoa bebe:
x = tela_x-200
y = tela_y-400
ex = tela_x-800
ey = tela_y-400
px1=randrange(200,600)
py1=randrange(50,200)


px2=randrange(200,600)
py2=randrange(200,350)


px3=randrange(200,600)
py3=randrange(300,350)

#criando os bebes
b_1= Bebe('bebe bonitinho0.png',x,y-10,tela,80,70,40)
b_2= Bebe('bebe bonitinho(3).png',ex,ey-10,tela,80,70,40)
#criando as plataformas
p_1=Imagens(x,y+by_p,'nuvens(1).png',100,10)
p_2=Imagens(ex,ey+by_p,'nuvens(1).png',100,10)
p_baixo_direita=Parede(0,tela_y-10,10000,100,red)
p_aleatoria1=Imagens(px1,py1,'nuvens(1).png',100,10)
p_aleatoria3=Imagens(px3,py3,'nuvens(1).png',100,10)
p_aleatoria2=Imagens(px2,py2,'nuvens(1).png',100,10)

paredeladoe=Parede(x+2,y+by_p+20,0.1,2,black)
paredebaixo=Parede(x+20,y+by_p+25,80,0.01,black)
paredeladod=Parede(x+120,y+by_p+20,0.1,2,black)



paredeladoe0=Parede(ex+2,ey+by_p+20,0.1,2,black)
paredebaixo0=Parede(ex+20,ey+by_p+25,80,0.01,red)
paredeladod0=Parede(ex+120,ey+by_p+20,0.1,2,black)




paredeladoe1=Parede(px1+2,py1+20,0.01,0.001,black)
paredebaixo1=Parede(px1+20,py1+25,80,0.001,black)
paredeladod1=Parede(px1+120,py1+20,0.01,0.001,black)



paredeladoe2=Parede(px2+2,py2+20,0.01,0.001,black)
paredebaixo2=Parede(px2+20,py2+25,80,0.001,black)
paredeladod2=Parede(px2+120,py2+20,0.01,0.001,black)



paredeladoe3=Parede(px3+2,py3+20,0.01,0.001,black)
paredebaixo3=Parede(px3+20,py3+25,80,0.001,black)
paredeladod3=Parede(px3+120,py3+20,0.01,0.001,black)

paredeld.add(paredeladod)
paredele.add(paredeladoe)
paredeb.add(paredebaixo)
paredeld.add(paredeladod0)
paredele.add(paredeladoe0)
paredeb.add(paredebaixo0)
paredeld.add(paredeladod1)
paredele.add(paredeladoe1)
paredeb.add(paredebaixo1)
paredeld.add(paredeladod2)
paredele.add(paredeladoe2)
paredeb.add(paredebaixo2)
paredeld.add(paredeladod3)
paredele.add(paredeladoe3)
paredeb.add(paredebaixo3)
lava.add(p_baixo_direita)


plataforma_group.add(p_aleatoria2)
plataforma_group.add(p_aleatoria3)
plataforma_group.add(p_aleatoria1)
plataforma_group.add(p_1)
plataforma_group.add(p_2)
#criando mamadeiras
m_1= Mamadeira('mamadeira2.png',(x+d_mao_pe),(y+d_mao_mao),10,(-10),(grav))
m_2=Mamadeira('mamadeira2.png',(ex+d_mao_pe),(ey+d_mao_mao),8,(-10),(grav))

#adicionando nos grupos
bebe_1.add(b_1)
bebe_2.add(b_2)
mamadeira_1.add(m_1)

mamadeira_2.add(m_2)
#    ex=x
#    ey=y

#    adicionando musica de fundo
pygame.mixer.music.load('babyfight.mp3')
pygame.mixer.music.play(-1)

 
control=False
trocou_de_mao_1=False
trocou_de_mao_2=False
atirou2=False
atirou1=False
rules=False

sair=False
inicio=True
movimento_1=False
m_bebe=0
b=0

#Looping principal
vy_inicial2=m_2.vy
vy_inicial1=m_1.vy
vx_inicial2=m_2.vx
vx_inicial1=m_1.vx


velmax_x=False
velmin_x=False
pulo2=0
pulo1=0
g1=0
g2=0
morte=False
#timer=0
pygame.mixer.music.play(-1)
jump1=False
jump2=False
while not sair:
    m_2.move()
    m_1.move()
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
                sair = True

#TElA DE INICIO
        elif inicio:
            tela.fill(azul)
            tela.blit(text,(420 - text.get_width() // 2, 130 - text.get_height() // 2))
            jogar=tela.blit(text1,(420 - text1.get_width() // 2, 230 - text1.get_height() // 2))
            cont=tela.blit(controles,(416 - text1.get_width() // 2, 280 - text1.get_height() // 2))
            rule=tela.blit(regras,(430 - text1.get_width() // 2, 320 - text1.get_height() // 2))
            trocou_de_mao_1=False
            trocou_de_mao_2=False
            atirou2=False        
            movimento_1=False
            m_bebe=0
            b=0

            if event.type == pygame.MOUSEBUTTONDOWN:            
                mouse_posicao=pygame.mouse.get_pos()
                if jogar.collidepoint(mouse_posicao):
                    inicio=False
                    control=False
                    rules=False
                    musica.play(-1)
                elif cont.collidepoint(mouse_posicao):
                        inicio=False
                        control=True
                        rules=False
                elif rule.collidepoint(mouse_posicao):
                            inicio=False
                            control=False
                            rules=True
                            
                            
                            
                            
                            
#TELA DE CONTROLES 
                            
                            
                            
        elif control:
            tela.fill(gray)
            tela.blit(controle0,(420 - text1.get_width() // 2, 130 - text1.get_height() // 2))
            tela.blit(controle1,(420 - text1.get_width() // 2, 205 - text1.get_height() // 2))
            tela.blit(controle2,(420 - text1.get_width() // 2, 280 - text1.get_height() // 2))
            tela.blit(controle3,(420 - text1.get_width() // 2, 355 - text1.get_height() // 2))
            tela.blit(controle4,(420 - text1.get_width() // 2, 430 - text1.get_height() // 2))
            volt=tela.blit(voltar,(170 - text1.get_width() // 2, 430 - text1.get_height() // 2))
            if event.type == pygame.MOUSEBUTTONDOWN:            
                mouse_posicao=pygame.mouse.get_pos()
                if volt.collidepoint(mouse_posicao):
                        control=False
                        inicio=True
                        
                        
#TELA DE REGRAS
                        
                        
                        
        elif rules:
            tela.fill(gray)
            tela.blit(regra0,(420 - text.get_width() // 2, 130 - text.get_height() // 2))
            tela.blit(regra1,(420 - text1.get_width() // 2, 230 - text1.get_height() // 2))
            tela.blit(regra2,(470 - text1.get_width() // 2, 250 - text1.get_height() // 2))
            tela.blit(regra3,(450 - text1.get_width() // 2, 300 - text1.get_height() // 2))
            tela.blit(regra4,(420 - text1.get_width() // 2, 350 - text1.get_height() // 2))
            volt=tela.blit(voltar,(170 - text1.get_width() // 2, 430 - text1.get_height() // 2))
            if event.type == pygame.MOUSEBUTTONDOWN:            
                mouse_posicao=pygame.mouse.get_pos()
                if volt.collidepoint(mouse_posicao):
                    control=False
                    inicio=True
                        
                        
            
                        
#MOVIMENTO DOS PERSONAGENS                        
        elif not morte:
            velmax_x=False
            velmin_x=False           
            movimentou2=False
            movimentou1=False
            if not movimento_1:
                pode=True
                
                if event.type == pygame.KEYDOWN:  
                        
                        if event.key== pygame.K_RETURN:
                            m_2.atira()
                            atirou2=True
                            
    
                        if event.key==pygame.K_LEFT and not trocou_de_mao_2 and not atirou2:
                            m_2.rect.x-=d_mao_mao+20
                            b_2.image=pygame.transform.flip(b_2.image, True, False)
                            m_2.vx=-m_2.vx
                            trocou_de_mao_2=True
                            
                        if event.key==pygame.K_RIGHT and trocou_de_mao_2 and not atirou2:
                                m_2.rect.x+=d_mao_mao+20
                                m_2.vx=-m_2.vx
                                b_2.image=pygame.transform.flip(b_2.image, True, False)
                                trocou_de_mao_2=False
                        if event.key==pygame.K_UP and not atirou2:
                            m_2.vy-=tela_y-498
    
                        if event.key==pygame.K_DOWN and not atirou2:
                            m_2.vy+=tela_y-498

                        if event.key==pygame.K_w and not atirou2:
                            if m_2.vx!=16 and m_2.vx!=-16:
                                if trocou_de_mao_2:
                                    m_2.vx-=2
                                else:
                                    m_2.vx+=2
                            else:
                                velmax_x=True
                        if event.key==pygame.K_d and b_2.rect.x<(900-d_mao_mao-50) and not atirou2:
                                
                            
                                    b_2.rect.x+=50
                                    m_2.rect.x+=50
                                    m_bebe+=1
                                    movimentou2=True
                            
                                    

                                    
                                    
                        if event.key==pygame.K_s and not atirou2:
                            if m_2.vx!=0:
                                if trocou_de_mao_2:
                                    m_2.vx+=2
                                else:
                                    m_2.vx-=2
                            else:
                                velmin_x=True
                        if event.key==pygame.K_a and b_2.rect.x>0 and not atirou2:
                            b_2.rect.x-=50
                            m_2.rect.x-=50
                            m_bebe+=1
                            movimentou=True
                        if event.key==pygame.K_SPACE and not atirou2 and not jump2:
                           
                            pulo2=-10
                            m_bebe+=1
                            jump2=True


                        




            if movimento_1:
                if event.type == pygame.KEYDOWN:  
                    if event.key== pygame.K_RETURN:
                        m_1.atira()
                        atirou1=True                        
                    if event.key==pygame.K_LEFT and not trocou_de_mao_1 and not atirou1:
                        m_1.rect.x-=d_mao_mao+20
                        m_1.vx=-m_1.vx
                        b_1.image=pygame.transform.flip(b_1.image, True, False)
                        trocou_de_mao_1=True
                    if event.key==pygame.K_RIGHT and trocou_de_mao_1 and not atirou1:
                            m_1.rect.x+=d_mao_mao+20
                            m_1.vx=-m_1.vx
                            b_1.image=pygame.transform.flip(b_1.image, True, False)
                            trocou_de_mao_1=False
                    if event.key==pygame.K_w and not atirou1:
                        if m_1.vx!=16 and m_1.vx!=(-16):
                            if trocou_de_mao_1:
                                m_1.vx-=2
                            else:
                                m_1.vx+=2
                        else:
                            velmax_x=True
                    if event.key==pygame.K_s and not atirou1:
                        if m_1.vx!=0:
                            if trocou_de_mao_1:
                                m_1.vx+=2
                            else:
                                m_1.vx-=2
                        else:
                            velmin_x=True
    
                        
                    if event.key==pygame.K_UP and not atirou1:
                        m_1.vy-=tela_y-498
    
                    if event.key==pygame.K_DOWN and not atirou1:
                        m_1.vy+=tela_y-498
                    if event.key==pygame.K_d and b_1.rect.x<(900-d_mao_mao-50) and not atirou1:
                            b_1.rect.x+=50
                            m_1.rect.x+=50
                            m_bebe-=1
                            movimentou=True
                            
    
                    if event.key==pygame.K_a and b_1.rect.x>0 and not atirou1:
                        b_1.rect.x-=50
                        m_1.rect.x-=50
                        m_bebe-=1
                        movimentou=True
    
                    if event.key==pygame.K_SPACE and not atirou1 and not jump1:
                        
                        pulo1=-10
                        m_bebe-=1
                        jump1=True
#TROCA DE MOVIMENTOS
    if m_bebe<=0:
        movimento_1=False
        mamadeira=mamadeira_2
        

    if m_bebe>=3:
        movimento_1=True
        mamadeira=mamadeira_1
              
#GRAVIDADE DOS BEBES
                    

    b_2.rect.y+=pulo2
    if not atirou2:
        m_2.rect.y=b_2.rect.y+d_mao_mao-10    
    gravidadeb2_1=pygame.sprite.spritecollide(b_2,plataforma_group, False)    
    gravidadeb2_pb=pygame.sprite.spritecollide(b_2,paredeb, False)

    gravlava2=pygame.sprite.spritecollide(b_2,lava,False)        
    if gravidadeb2_pb:
            pulo2=0
            b_2.rect.y+=2
            m_2.rect.y+=2
    elif gravlava2:
        pulo2=0
        jump2=False
        if not morte:
            pulo2-=15
            b_2.vida-=10
            b_2.health()
            
    elif gravidadeb2_1:
        pulo2=0
        jump2=False
    else:
        g2=grav*1/FPS
        pulo2+=g2
         




    b_1.rect.y+=pulo1
    if not atirou1:
        m_1.rect.y=b_1.rect.y+d_mao_mao-10
        
        
        
        
        
        
    gravidadeb1_1=pygame.sprite.spritecollide(b_1,plataforma_group, False)    
    gravidadeb1_pb=pygame.sprite.spritecollide(b_1,paredeb, False)
    gravlava1=pygame.sprite.spritecollide(b_1,lava,False)       
    if gravidadeb1_pb:
        pulo1=0
        g1=grav*1/FPS
        b_1.rect.y+=2
    elif gravlava1:
        pulo1=0
        jump1=False
        if not morte:
            pulo1-=15
            b_1.vida-=10
            b_1.health()
            
    elif gravidadeb1_1 and not gravidadeb1_pb:
        pulo1=0
        jump1=False
    else:
        g1=grav*1/FPS
        pulo1+=g1
        
        
        
        
#COLISAO DOS BEBES COM AS MAMADEIRAS E PLATAFORMAS            
    colisao_b_m2= pygame.sprite.spritecollide(b_1,mamadeira_2, False)
    colisao_m_p2=pygame.sprite.spritecollide(m_2,plataforma_group, False)
    if colisao_b_m2 or colisao_m_p2 and atirou2 or m_2.rect.x>900 or m_2.rect.x<0 or m_2.rect.y<-500:
        m_2.rect.x=b_2.rect.x+d_mao_pe
        m_2.rect.y=b_2.rect.y+d_mao_mao-10
        m_2.parar_atirar()
        if trocou_de_mao_2:
            b_2.image=pygame.transform.flip(b_2.image, True, False)
        if colisao_b_m2:
            b_1.vida-=20
            b_1.health()
            if b_1.rect.x<=850 and b_1.rect.x>=50:
                if trocou_de_mao_2:
                    b_1.rect.x-=50
                    m_1.rect.x-=50
                elif not trocou_de_mao_2:
                    b_1.rect.x+=50
                    m_1.rect.x+=50
        m_2.vy=vy_inicial2
        m_2.vx=vx_inicial2
        m_bebe=3
        trocou_de_mao_2=False
        atirou2=False




       
    colisao_b_m1 = pygame.sprite.spritecollide(b_2,mamadeira_1, False)
    colisao_m_p1=pygame.sprite.spritecollide(m_1,plataforma_group, False)
    if colisao_b_m1 or colisao_m_p1 and atirou1 or m_1.rect.x>900 or m_1.rect.x<0 or m_1.rect.y<-500:
        m_1.rect.x=b_1.rect.x+d_mao_pe
        m_1.rect.y=b_1.rect.y+d_mao_mao-10
        m_1.parar_atirar()
        if trocou_de_mao_1:
            b_1.image=pygame.transform.flip(b_1.image, True, False)
        if colisao_b_m1:
            b_2.vida-=20
            b_2.health()
            if b_2.rect.x<=850 and b_2.rect.x>=50:
                if trocou_de_mao_1:
                    b_2.rect.x-=50
                    m_2.rect.x-=50
                elif not trocou_de_mao_1:
                    b_2.rect.x+=50
                    m_2.rect.x+=50
        m_1.vy=vy_inicial1
        m_1.vx=vx_inicial1
        m_bebe=0
        atirou1=False
        trocou_de_mao_1=False
        
#SISTEMA DE COLISAO COM PAREDES LATERAIS        
    colisao_pesquerda2=pygame.sprite.spritecollide(b_2,paredele,False)
    colisao_pdireita2=pygame.sprite.spritecollide(b_2,paredeld,False)
                        
                        
                        
    if colisao_pesquerda2:
        if movimentou2:
            b_2.rect.x-=50
            if not atirou2:
                m_2.rect.x-=50
        else:
            b_2.rect.x-=5
            if not atirou2:
                m_2.rect.x-=5
                
                
    if colisao_pdireita2:
        if movimentou2:
            b_2.rect.x+=50
            if not atirou2:
                m_2.rect.x+=50

                
                
                
        
    colisao_pesquerda1=pygame.sprite.spritecollide(b_1,paredele,False)
    colisao_pdireita1=pygame.sprite.spritecollide(b_1,paredeld,False)
    if colisao_pesquerda1:
        if movimentou1:
            b_1.rect.x-=50
            if not atirou1:
                m_1.rect.x-=50
        else:
            b_1.rect.x-=5
            if not atirou1:
                m_1.rect.x-=5
            
            
    if colisao_pdireita1:
        if movimentou1:
            b_1.rect.x+=50
            if not atirou1:
                m_1.rect.x+=50

        
#TELA DO JOGO


    if not inicio and not control and not rules:
        
#        tela.blit(fundo, (0, 0))
        tela.fill(white)
        bebe_1.draw(tela)
        bebe_2.draw(tela)
        lava.draw(tela)
        plataforma_group.draw(tela)
        paredeb.draw(tela)
        paredeld.draw(tela)
        paredele.draw(tela)
        mamadeira_1.draw(tela)
        mamadeira_2.draw(tela)
        m=0
        pygame.mixer.music.stop()
        
#        timer+=1/FPS
#        a=font3.render(str(timer), True, (black))
#        tela.blit(a,(100 - text1.get_width() // 2, 400 - text1.get_height() // 2))
        if velmax_x:
            max_x=font3.render("Velocidade maxima", True, (red))
            tela.blit(max_x,(350 - text.get_width() // 2, 500 - text.get_height() // 2))
        elif velmin_x:
            max_x=font3.render("Velocidade minima", True, (red))
            tela.blit(max_x,(350 - text.get_width() // 2, 500 - text.get_height() // 2))
        if not atirou2 and not atirou1:   
            for m in mamadeira:
                m.pre_move(tela)
        if  (b_2.vida<=0 or b_1.vida<=0) and not morte:
            if b_2.vida<=0:
                b_choro= Bebe('bebe bonitinho(2).png',b_2.rect.x,b_2.rect.y,tela,100,0,0)
                bebe_2.add(b_choro)
                bebe_2.remove(b_2)
                morte=True
            if b_1.vida<=0:
                b_choro= Bebe('bebe bonitinho(1).png',b_1.rect.x,b_1.rect.y,tela,100,0,0)
                bebe_1.add(b_choro)
                bebe_1.remove(b_1)
                morte=True
            musica.stop()
            choro.play()
            mamadeira_2.remove(m_2)
            mamadeira_1.remove(m_1)
            final=font1.render("Parabéns, você fez o bebe chorar, seu MONSTRO", True, (green))
            final_jogar=font3.render("Jogar de novo", True, (blue))
        if morte:
            tela.blit(final,(420 - text.get_width() // 2, 100 - text.get_height() // 2))
            jogar_de_novo=tela.blit(final_jogar,(170 - text1.get_width() // 2, 430 - text1.get_height() // 2))
            if event.type == pygame.MOUSEBUTTONDOWN:            
                mouse_posicao=pygame.mouse.get_pos()
            if jogar_de_novo.collidepoint(mouse_posicao):
                choro.stop()
                morte=False
                musica.stop()
                pygame.mixer.music.play(-1)
                inicio=True
                control=False
                bebe_2 = pygame.sprite.Group()
                bebe_1 = pygame.sprite.Group()
                b_1= Bebe('bebe bonitinho0.png',x,y-10,tela,80,40,40)
                b_2= Bebe('bebe bonitinho(3).png',ex,ey-10,tela,80,40,40)
                #criando mamadeiras
                m_1= Mamadeira('mamadeira2.png',(x+d_mao_pe),(y+d_mao_mao),10,(-10),(grav))
                m_2=Mamadeira('mamadeira2.png',(ex+d_mao_pe),(ey+d_mao_mao),8,(-10),(grav))
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
            tela.blit(vez,(450 - text1.get_width() // 2, 50 - text1.get_height() // 2))

            
        


                

#desenho tela de inicio

                


#desenho tela dos cpntroles
    

    pygame.display.update()
    relogio.tick(FPS)
    
choro.stop()
pygame.mixer.music.stop()
musica.stop()

pygame.display.quit()