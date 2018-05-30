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
fundo = pygame.image.load("ceu novo.png").convert()
fundo = pygame.transform.scale(fundo,(tela_x,tela_y))

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
class Plataformas(pygame.sprite.Sprite):    
    def __init__(self,pos_x,pos_y, imagem):
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
        
        
        
class Cookie(pygame.sprite.Sprite):    
    def __init__(self,pos_x,pos_y, imagem):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagem)       
        self.image = pygame.transform.scale(self.image,(20,20))
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
        self.image=pygame.transform.chop(self.image, (30, 26, 30,30 ))
        self.image=pygame.transform.chop(self.image, (0, 0, 0,15 ))
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
        self.pre_x=self.rect.x+20
        self.pre_y=self.rect.y+5
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
                

font = pygame.font.SysFont("Boo.Fixed Sys", (tela_x-850))
text = font.render("Bem Vindo ao Baby Fight", True, (green))
font1 = pygame.font.SysFont("segoe ui", tela_x-872)
font2= pygame.font.SysFont("segoe ui", tela_x-880)
font3=pygame.font.SysFont('segoe ui',tela_x-880)
text1 = font1.render("JOGAR", True, (blue))
controles=font2.render("CONTROLES",True,blue)
regras=font2.render("REGRAS",True,blue)
#Controles
controle0=font.render("CONTROLES", True, (black))
controle1=font3.render("SETAS PARA CIMA & BAIXO = CONTROLA A INCLINAÇÃO DO TIRO", True, (green))
controle2=font3.render("SETAS PARA OS LADOS = CONTROLE DA DIREÇÃO DO TIRO", True, (green))
controle3=font3.render("TECLAS A, BARRA DE ESPAÇO & D = MOVIMENTO DO BEBE",True,(green))
controle4=font3.render('TECLAS W & S = VELOCIDADE DO TIRO',True,(green))
#Regras
regra0=font.render("REGRAS",True,black)
regra1=font3.render("NESSE JOGO O SEU OBJETIVO É ACABAR COM OS OUTROS BEBES,", True, (green))
regra2=font3.render("MAS NÃO FAÇA ISSO ELES SÃO APENAS BEBES", True, (green))
regra3=font3.render("CADA JOGADOR TEM 3 MOVIMENTOS OU UM TIRO",True,green)
regra4=font3.render("NÃO USE HACK, CASO CONTRÁRIO FICARA DE CASTIGO",True,green)
voltar=font2.render("VOLTAR",True,black)

                
#CRIANDO TELA

pygame.init()

tela = pygame.display.set_mode([tela_x,tela_y])
pygame.display.set_caption("Bem vindo ao jogo")


#CRIANDO GRUPOS


cookie= pygame.sprite.Group()
bebe_1 = pygame.sprite.Group()
mamadeira_1 = pygame.sprite.Group()
mamadeira_2 = pygame.sprite.Group()
bebe_2 = pygame.sprite.Group()

plataforma_group=pygame.sprite.Group()
paredeb=pygame.sprite.Group()
paredebebe=pygame.sprite.Group()
lava=pygame.sprite.Group()



#CONSTANTES E VARIAVIES
    #DIMENSOES DOS BEBES
    
    
mamadeira_bebe_y = 60
mamadeira_bebe_x = 70
plataforma_bebe_y=90

    #FALSE/TRUE
control=False
trocou_de_mao_1=False
trocou_de_mao_2=False
atirou2=False
atirou1=False
rules=False
sair=False
inicio=True
movimento_1=False
velmax_x=False
velmin_x=False
morte=False
jump2=False
jump1=False

    #MOVIMENTO DOS BEBES
m_bebe=0


    #GRAVIDADE
pulo2=0
pulo1=0
g1=0
g2=0

#timer=0





    #LOCALIZACOES DOS BEBES:



x = tela_x-220
y = tela_y-400
ex = tela_x-800
ey = tela_y-400


    #LOCALIZACOES DAS PLATAFORMAS
    
    
px1=randrange(200,600)
py1=randrange(50,200)


px2=randrange(200,600)
py2=randrange(200,350)


px3=randrange(200,600)
py3=randrange(300,350)

#CRIANDO
    #BEBES


b_1= Bebe('bebe bonitinho0.png',x,y-10,tela,80,70,40)
b_2= Bebe('bebe bonitinho(3).png',ex,ey-10,tela,80,70,40)

    #MAMADEIRAS

m_1= Mamadeira('mamadeira2.png',(x+mamadeira_bebe_x),(y+mamadeira_bebe_y),10,(-10),(grav))
m_2=Mamadeira('mamadeira2.png',(ex+mamadeira_bebe_x),(ey+mamadeira_bebe_y),8,(-10),(grav))

    #PLATAFORMAS


p_1=Plataformas(x,y+plataforma_bebe_y,'nuvens(1).png')
p_2=Plataformas(ex,ey+plataforma_bebe_y,'nuvens(1).png')
p_aleatoria1=Plataformas(px1,py1,'nuvens(1).png')
p_aleatoria3=Plataformas(px3,py3,'nuvens(1).png')
p_aleatoria2=Plataformas(px2,py2,'nuvens(1).png')


    #LAVA
p_baixo_direita=Parede(0,tela_y-10,10000,100,red)



    #PAREDES

 


        #BEBES
paredebebe1=Parede(x+10,y+plataforma_bebe_y-10,65,15,red)
paredebebe2=Parede(ex+10,ey+plataforma_bebe_y-10,65,15,red)


        #PLATAFORMAS   
paredebaixo=Parede(x+15,y+plataforma_bebe_y,90,5,black)
paredebaixo0=Parede(ex+15,ey+plataforma_bebe_y,90,5,black)
paredebaixo1=Parede(px1+15,py1+2,90,5,black)
paredebaixo2=Parede(px2+15,py2+2,90,5,black)
paredebaixo3=Parede(px3+15,py3+2,90,5,black)




#ADICIONANDO AOS GRUPOS


    #PAREDE
paredeb.add(paredebaixo)
paredeb.add(paredebaixo0)
paredeb.add(paredebaixo1)
paredeb.add(paredebaixo2)
paredeb.add(paredebaixo3)


    #LAVA
    
lava.add(p_baixo_direita)

    #PLATAFORMA
    
plataforma_group.add(p_aleatoria2)
plataforma_group.add(p_aleatoria3)
plataforma_group.add(p_aleatoria1)
plataforma_group.add(p_1)
plataforma_group.add(p_2)

    #BEBES
    
bebe_1.add(b_1)
bebe_2.add(b_2)


    #MAMADEIRAS
    
    
mamadeira_1.add(m_1)
mamadeira_2.add(m_2)


#MUSICA DE FUNDO


pygame.mixer.music.load('babyfight.mp3')
pygame.mixer.music.play(-1)

 
#VELOCIDADE INICIAL DA MAMADEIRA


vy_inicial2=m_2.vy
vy_inicial1=m_1.vy
vx_inicial2=m_2.vx
vx_inicial1=m_1.vx

#LOOPING PRICIPAL
while not sair:
    # MOVIMENTO DA MAMADEIRA
    
    m_2.move()
    m_1.move()
    
    #APARECIMENTO DO COOKIE
    
    aparece=randrange(0,600)
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
                sair = True

        #TElA DE INICIO
        elif inicio:
            tela.fill(azul)
            tela.blit(text,(420 - text.get_width() // 2, 130 - text.get_height() // 2))
            jogar=tela.blit(text1,(425 - text1.get_width() // 2, 230 - text1.get_height() // 2))
            cont=tela.blit(controles,(416 - text1.get_width() // 2, 280 - text1.get_height() // 2))
            rule=tela.blit(regras,(435 - text1.get_width() // 2, 310 - text1.get_height() // 2))
            trocou_de_mao_1=False
            trocou_de_mao_2=False
            atirou2=False        
            movimento_1=False
            m_bebe=0


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
            tela.blit(controle0,(350 - text1.get_width() // 2, 100 - text1.get_height() // 2))
            tela.blit(controle1,(350 - text1.get_width() // 2, 205 - text1.get_height() // 2))
            tela.blit(controle2,(350 - text1.get_width() // 2, 280 - text1.get_height() // 2))
            tela.blit(controle3,(350 - text1.get_width() // 2, 355 - text1.get_height() // 2))
            tela.blit(controle4,(350 - text1.get_width() // 2, 430 - text1.get_height() // 2))
            volt=tela.blit(voltar,(170 - text1.get_width() // 2, 430 - text1.get_height() // 2))
            if event.type == pygame.MOUSEBUTTONDOWN:            
                mouse_posicao=pygame.mouse.get_pos()
                if volt.collidepoint(mouse_posicao):
                        control=False
                        inicio=True
                        
                        
        #TELA DE REGRAS
                        
                        
                        
        elif rules:
            tela.fill(gray)
            tela.blit(regra0,(525 - text.get_width() // 2, 130 - text.get_height() // 2))
            tela.blit(regra1,(350 - text1.get_width() // 2, 230 - text1.get_height() // 2))
            tela.blit(regra2,(350 - text1.get_width() // 2, 250 - text1.get_height() // 2))
            tela.blit(regra3,(350 - text1.get_width() // 2, 300 - text1.get_height() // 2))
            tela.blit(regra4,(350 - text1.get_width() // 2, 350 - text1.get_height() // 2))
            volt=tela.blit(voltar,(170 - text1.get_width() // 2, 430 - text1.get_height() // 2))
            if event.type == pygame.MOUSEBUTTONDOWN:            
                mouse_posicao=pygame.mouse.get_pos()
                if volt.collidepoint(mouse_posicao):
                    control=False
                    inicio=True
                        
                        
            
                        
                               
        elif not morte:
            velmax_x=False
            velmin_x=False           
            movimentou2=False
            movimentou1=False
            
            
            #MOVIMENTO DOS PERSONAGENS 
            if not movimento_1:
                pode=True
                
                if event.type == pygame.KEYDOWN:  
                        
                        if event.key== pygame.K_RETURN:
                            m_2.atira()
                            atirou2=True
                            
    
                        if event.key==pygame.K_LEFT and not trocou_de_mao_2 and not atirou2:
                            m_2.rect.x-=mamadeira_bebe_y+20
                            b_2.image=pygame.transform.flip(b_2.image, True, False)
                            m_2.vx=-m_2.vx
                            trocou_de_mao_2=True
                            
                        if event.key==pygame.K_RIGHT and trocou_de_mao_2 and not atirou2:
                                m_2.rect.x+=mamadeira_bebe_y+20
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
                        if event.key==pygame.K_d and b_2.rect.x<(781) and not atirou2:
                                
                            
                                    b_2.rect.x+=50
                                    m_2.rect.x+=50
                                    paredebebe2.rect.x=b_2.rect.x+10
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
                            paredebebe2.rect.x=b_2.rect.x+10
                            m_bebe+=1
                            movimentou2=True
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
                        m_1.rect.x-=mamadeira_bebe_y+20
                        m_1.vx=-m_1.vx
                        b_1.image=pygame.transform.flip(b_1.image, True, False)
                        trocou_de_mao_1=True
                    if event.key==pygame.K_RIGHT and trocou_de_mao_1 and not atirou1:
                            m_1.rect.x+=mamadeira_bebe_y+20
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
                    if event.key==pygame.K_d and b_1.rect.x<(781) and not atirou1:
                            b_1.rect.x+=50
                            m_1.rect.x+=50
                            paredebebe1.rect.x=b_1.rect.x+10
                            m_bebe-=1
                            movimentou1=True
                            
    
                    if event.key==pygame.K_a and b_1.rect.x>0 and not atirou1:
                        b_1.rect.x-=50
                        m_1.rect.x-=50
                        paredebebe1.rect.x=b_1.rect.x+10
                        m_bebe-=1
                        movimentou1=True
    
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
    paredebebe2.rect.y=b_2.rect.y+90
    if not atirou2:
        m_2.rect.y=b_2.rect.y+mamadeira_bebe_y 
        
        
        
    gravidadeb2_1=pygame.sprite.spritecollide(paredebebe2,paredeb, False)    
    gravlava2=pygame.sprite.spritecollide(b_2,lava,False)        
    if gravlava2:
        pulo2=0
        jump2=False
        if not morte:
            pulo2-=15
            b_2.vida-=10
            b_2.health()
            
    elif gravidadeb2_1 and pulo2>=0:
        pulo2=0
        jump2=False
    else:
        g2=grav*1/FPS
        pulo2+=g2
         




    b_1.rect.y+=pulo1
    paredebebe1.rect.y=b_1.rect.y+90
    if not atirou1:
        m_1.rect.y=b_1.rect.y+mamadeira_bebe_y
        
        
        
        
        
        
    gravidadeb1_1=pygame.sprite.spritecollide(paredebebe1,paredeb, False)    
    gravlava1=pygame.sprite.spritecollide(b_1,lava,False)       
    if gravlava1:
        pulo1=0
        jump1=False
        if not morte:
            pulo1-=15
            b_1.vida-=10
            b_1.health()
            
    elif gravidadeb1_1 and pulo1>=0:
        pulo1=0
        jump1=False
    else:
        g1=grav*1/FPS
        pulo1+=g1
        
        
        
        
#COLISAO DAS MAMADEIRAS COM OS BEBES E PLATAFORMAS            
    colisao_b_m2= pygame.sprite.spritecollide(b_1,mamadeira_2, False)
    colisao_m_p2=pygame.sprite.spritecollide(m_2,plataforma_group, False)
    if colisao_b_m2 or colisao_m_p2 and atirou2 or m_2.rect.x>900 or m_2.rect.x<0 or m_2.rect.y<-500:
        m_2.rect.x=b_2.rect.x+mamadeira_bebe_x
        m_2.rect.y=b_2.rect.y+mamadeira_bebe_y
        m_2.parar_atirar()
        if trocou_de_mao_2:
            b_2.image=pygame.transform.flip(b_2.image, True, False)
        if colisao_b_m2:
            b_1.vida-=20
            b_1.health()
            if b_1.rect.x<(781) and b_1.rect.x>0:
                if trocou_de_mao_2:
                    b_1.rect.x-=50
                    m_1.rect.x-=50
                    paredebebe1.rect.x=b_1.rect.x+10
                elif not trocou_de_mao_2:
                    b_1.rect.x+=50
                    m_1.rect.x+=50
                    paredebebe1.rect.x=b_1.rect.x+10
        m_2.vy=vy_inicial2
        m_2.vx=vx_inicial2
        m_bebe=3
        trocou_de_mao_2=False
        atirou2=False




       
    colisao_b_m1 = pygame.sprite.spritecollide(b_2,mamadeira_1, False)
    colisao_m_p1=pygame.sprite.spritecollide(m_1,plataforma_group, False)
    if colisao_b_m1 or colisao_m_p1 and atirou1 or m_1.rect.x>900 or m_1.rect.x<0 or m_1.rect.y<-500:
        m_1.rect.x=b_1.rect.x+mamadeira_bebe_x
        m_1.rect.y=b_1.rect.y+mamadeira_bebe_y
        m_1.parar_atirar()
        if trocou_de_mao_1:
            b_1.image=pygame.transform.flip(b_1.image, True, False)
        if colisao_b_m1:
            b_2.vida-=20
            b_2.health()
            if b_2.rect.x<(781) and b_2.rect.x>0:
                if trocou_de_mao_1:
                    b_2.rect.x-=50
                    m_2.rect.x-=50
                    paredebebe2.rect.x=b_2.rect.x+10
                elif not trocou_de_mao_1:
                    b_2.rect.x+=50
                    m_2.rect.x+=50
                    paredebebe2.rect.x=b_2.rect.x+10
        m_1.vy=vy_inicial1
        m_1.vx=vx_inicial1
        m_bebe=0
        atirou1=False
        trocou_de_mao_1=False
        
        
        
#COLISAO COOKIE E BEBES

        
    comer2=pygame.sprite.spritecollide(b_2,cookie,True)
    comer1=pygame.sprite.spritecollide(b_1,cookie,True)
    if comer2:
        b_2.vida+=40
        b_2.health()
    if comer1:
        b_1.vida+=40
        b_1.health()
        
        
#SISTEMA DE COLISAO COM PAREDES LATERAIS        


                
                
                
        

        
#TELA DO JOGO


    if not inicio and not control and not rules:
        lava.draw(tela)
        tela.blit(fundo, (0, 0))
        if aparece==5:
            #CRIACAO DOS COOKIES
            ck=Cookie(randrange(0,800),randrange(0,450),'índice.png')
            cookie.add(ck)

#        tela.fill(white)
        bebe_1.draw(tela)
        bebe_2.draw(tela)
        plataforma_group.draw(tela)
        mamadeira_1.draw(tela)
        mamadeira_2.draw(tela)
        cookie.draw(tela)
        m=0
        pygame.mixer.music.stop()
        
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
            final=font1.render("Parabéns, você fez o bebe chorar, seu MONSTRO", True, (black))
            final_jogar=font3.render("Jogar de novo", True, (blue))
        if morte:
            tela.blit(final,(400 - text.get_width() // 2, 20 - text.get_height() // 2))
            jogar_de_novo=tela.blit(final_jogar,(170 - text1.get_width() // 2, 430 - text1.get_height() // 2))
            if event.type == pygame.MOUSEBUTTONDOWN:            
                mouse_posicao=pygame.mouse.get_pos()
            if jogar_de_novo.collidepoint(mouse_posicao):
                cookie= pygame.sprite.Group()
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
                #Recriando mamadeiras
                m_1= Mamadeira('mamadeira2.png',(x+mamadeira_bebe_x),(y+mamadeira_bebe_y),10,(-10),(grav))
                m_2=Mamadeira('mamadeira2.png',(ex+mamadeira_bebe_x),(ey+mamadeira_bebe_y),8,(-10),(grav))
                
                paredebebe1=Parede(x+10,y+plataforma_bebe_y,70,5,red)
                paredebebe2=Parede(ex+10,ey+plataforma_bebe_y,70,5,red)
                #adicionando nos grupos
                bebe_1.add(b_1)
                bebe_2.add(b_2)
                mamadeira_1.add(m_1)
                mamadeira_2.add(m_2)
        elif m_bebe<=0 or m_bebe>=3:
            if m_bebe<=0:
                vez=font3.render("Vez da Valentina", True, (black))
            else:
                vez=font3.render("Vez do Enzo", True, (black))
            tela.blit(vez,(450 - text1.get_width() // 2, 50 - text1.get_height() // 2))
        
            
        


                

#desenho tela de inicio

                


#desenho tela dos cpntroles
    

    pygame.display.update()
    relogio.tick(FPS)
    
choro.stop()
pygame.mixer.music.stop()
musica.stop()

pygame.display.quit()