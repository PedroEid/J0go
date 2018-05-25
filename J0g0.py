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

pygame.mixer.pre_init()
pygame.init()

choro = pygame.mixer.Sound('choro2.ogg')
musica = pygame.mixer.Sound('music.ogg')


# Criando classe bebe
class Bebe (pygame.sprite.Sprite):
    def __init__(self, imbebe, pos_x, pos_y,tela,vida,cortex1,cortex2):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imbebe)       
        self.image = pygame.transform.scale(self.image,(180,150))
        self.image=pygame.transform.chop(self.image, (140, 120, cortex1,30 ))
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
class Plataforma(pygame.sprite.Sprite):    
    def __init__(self,pos_x,pos_y, width, height,cor):
        pygame.sprite.Sprite.__init__(self)
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        # Draw the ellipse
        pygame.draw.ellipse(self.image, cor, [0, 0, width, height])
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
        self.pre_y=self.rect.y+15
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
b_1= Bebe('bebe bonitinho0.png',x,y-10,tela,80,40,40)
b_2= Bebe('bebe bonitinho(3).png',ex,ey-10,tela,80,40,40)
#criando as plataformas
p_1=Plataforma(x,y+by_p,100,10,black)

paredeladod=Plataforma(x-1,y+by_p+5,0.01,0.01,black)
paredebaixo=Plataforma(x+10,y+by_p+10,80,0.01,black)
paredeladoe=Plataforma(x+100,y+by_p+5,0.01,0.01,black)

p_2=Plataforma(ex,ey+by_p,100,10,black)

paredeladod0=Plataforma(ex-1,ey+by_p+5,0.01,0.01,black)
paredebaixo0=Plataforma(ex+10,ey+by_p+10,80,0.01,red)
paredeladoe0=Plataforma(ex+100,ey+by_p+5,0.01,0.01,black)


p_baixo_direita=Plataforma(0,tela_y-10,10000,100,black)
p_aleatoria1=Plataforma(px1,py1,100,10,black)

paredeladod1=Plataforma(px1-1,py1+5,0.01,0.01,black)
paredebaixo1=Plataforma(px1+10,py1+10,80,0.01,black)
paredeladoe1=Plataforma(px1+100,py1+5,0.01,0.01,black)

p_aleatoria2=Plataforma(px2,py2,100,10,black)

paredeladod2=Plataforma(px2-1,py2+5,0.01,0.01,black)
paredebaixo2=Plataforma(px2+10,py2+10,80,0.01,black)
paredeladoe2=Plataforma(px2+100,py2+5,0.01,0.01,black)

p_aleatoria3=Plataforma(px3,py3,100,10,black)

paredeladod3=Plataforma(px3-1,py3+5,0.01,0.01,black)
paredebaixo3=Plataforma(px3+10,py3+10,80,0.01,black)
paredeladoe3=Plataforma(px3+100,py3+5,0.01,0.01,black)

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


plataforma_group.add(p_aleatoria2)
plataforma_group.add(p_aleatoria3)
plataforma_group.add(p_aleatoria1)
plataforma_group.add(p_baixo_direita)
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
control=False
trocou_de_mao_1=False
trocou_de_mao_2=False
atirou=False
rules=False

sair=False
inicio=True
movimento_1=False
m_bebe=0
b=0
vx_inicial=m_2.vx
#Looping principal
vy_inicial2=m_2.vy
vy_inicial1=m_1.vy
velmax_x=False
velmin_x=False
pulo2=0
pulo1=0
g1=0
g2=0
morte=False
#timer=0
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
            atirou=False        
            movimento_1=False
            m_bebe=0
            b=0
            vx_inicial=m_2.vx
            if event.type == pygame.MOUSEBUTTONDOWN:            
                mouse_posicao=pygame.mouse.get_pos()
                if jogar.collidepoint(mouse_posicao):
                    inicio=False
                    control=False
                    rules=False
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
            if not movimento_1:
                
#                if timer>10:
#                    m_bebe=3
                if event.type == pygame.KEYDOWN:  
                        
                        if event.key== pygame.K_RETURN:
                            m_2.atira()
                            atirou=True
                            
    
                        if event.key==pygame.K_LEFT and not trocou_de_mao_2 and not atirou:
                            m_2.rect.x-=d_mao_mao+20
                            b_2.image=pygame.transform.flip(b_2.image, True, False)
                            m_2.vx=-m_2.vx
                            trocou_de_mao_2=True
                            
                        if event.key==pygame.K_RIGHT and trocou_de_mao_2 and not atirou:
                                m_2.rect.x+=d_mao_mao+20
                                m_2.vx=-m_2.vx
                                b_2.image=pygame.transform.flip(b_2.image, True, False)
                                trocou_de_mao_2=False
                        if event.key==pygame.K_UP and not atirou:
                            m_2.vy-=tela_y-498
    
                        if event.key==pygame.K_DOWN and not atirou:
                            m_2.vy+=tela_y-498

                        if event.key==pygame.K_w and not atirou:
                            if m_2.vx!=16 and m_2.vx!=-16:
                                if trocou_de_mao_2:
                                    m_2.vx-=2
                                else:
                                    m_2.vx+=2
                            else:
                                velmax_x=True
                        if event.key==pygame.K_d and b_2.rect.x<(900-d_mao_mao-50) and not atirou:
                            b_2.rect.x+=50
                            m_2.rect.x+=50
                            m_bebe+=1
                        if event.key==pygame.K_s and not atirou:
                            if m_2.vx!=0:
                                if trocou_de_mao_2:
                                    m_2.vx+=2
                                else:
                                    m_2.vx-=2
                            else:
                                velmin_x=True
                        if event.key==pygame.K_a and b_2.rect.x>0 and not atirou:
                            b_2.rect.x-=50
                            m_2.rect.x-=50
                            m_bebe+=1
                        
                        if event.key==pygame.K_SPACE and not atirou:
                           
                            pulo2=-10
                            m_bebe+=1
                        vy_inicial2=m_2.vy
                        




            if movimento_1:
#                timer+=1/FPS
#                if timer>10:
#                    m_bebe=3
                for i in range(5*FPS):
                    pass
                if event.type == pygame.KEYDOWN:  
                    vy_inicial1=m_1.vy
                    if event.key== pygame.K_RETURN:
                        m_1.atira()
                        atirou=True                        
                    if event.key==pygame.K_LEFT and not trocou_de_mao_1 and not atirou:
                        m_1.rect.x-=d_mao_mao+20
                        m_1.vx=-m_1.vx
                        b_1.image=pygame.transform.flip(b_1.image, True, False)
                        trocou_de_mao_1=True
                    if event.key==pygame.K_RIGHT and trocou_de_mao_1 and not atirou:
                            m_1.rect.x+=d_mao_mao+20
                            m_1.vx=-m_1.vx
                            b_1.image=pygame.transform.flip(b_1.image, True, False)
                            trocou_de_mao_1=False
                    if event.key==pygame.K_w and not atirou:
                        if m_1.vx!=16 and m_1.vx!=(-16):
                            if trocou_de_mao_1:
                                m_1.vx-=2
                            else:
                                m_1.vx+=2
                        else:
                            velmax_x=True
                    if event.key==pygame.K_s and not atirou:
                        if m_1.vx!=0:
                            if trocou_de_mao_1:
                                m_1.vx+=2
                            else:
                                m_1.vx-=2
                        else:
                            velmin_x=True
    
                        
                    if event.key==pygame.K_UP and not atirou:
                        m_1.vy-=tela_y-498
    
                    if event.key==pygame.K_DOWN and not atirou:
                        m_1.vy+=tela_y-498
                    if event.key==pygame.K_d and b_1.rect.x<(900-d_mao_mao-50) and not atirou:
                        b_1.rect.x+=50
                        m_1.rect.x+=50
                        m_bebe-=1
    
                    if event.key==pygame.K_a and b_1.rect.x>0 and not atirou:
                        b_1.rect.x-=50
                        m_1.rect.x-=50
                        m_bebe-=1
    
                    if event.key==pygame.K_SPACE and not atirou:
                        
                        pulo1=-10
                        m_bebe-=1
                         
                    vy_inicial1=m_1.vy
              
#GRAVIDADE DOS BEBES
    if not atirou:
        b_2.rect.y+=pulo2
        m_2.rect.y=b_2.rect.y+d_mao_mao-10
        
    gravidadeb2_1=pygame.sprite.spritecollide(b_2,plataforma_group, False)    
    gravidadeb2_pb=pygame.sprite.spritecollide(b_2,paredeb, False)
    gravidedeb2_ple=pygame.sprite.spritecollide(b_2,paredele,False)
    gravidadeb2_pld=pygame.sprite.spritecollide(b_2,paredeld,False)
    if not gravidadeb2_1 and not gravidadeb2_pb:
        g2=grav*1/FPS
        pulo2+=g2
    elif gravidadeb2_pb:
        pulo2=0
        b_2.rect.y+=2
        m_2.rect.y+=2
    elif gravidedeb2_ple:
        pulo2=0
        b_2.rect.x+=2
        m_2.rect.x+=2
    elif gravidadeb2_pld:
        pulo2=0
        b_2.rect.x-=2
        m_2.rect.x-=2
    else:
        pulo2=0
        g2=0

        
        



    if not atirou:
        b_1.rect.y+=pulo1
        m_1.rect.y=b_1.rect.y+d_mao_mao-10
        
        
        
        
        
        
    gravidadeb1_1=pygame.sprite.spritecollide(b_1,plataforma_group, False)    
    gravidadeb1_pb=pygame.sprite.spritecollide(b_1,paredeb, False)
    gravidedeb1_ple=pygame.sprite.spritecollide(b_1,paredele,False)
    gravidadeb1_pld=pygame.sprite.spritecollide(b_1,paredeld,False)
    if not gravidadeb1_1 and not gravidadeb1_pb:
        g1=grav*1/FPS
        pulo1+=g1
    elif gravidadeb1_pb:
        pulo1=0
        b_1.rect.y+=2
        m_1.rect.y+=2
    elif gravidedeb1_ple:
        pulo1=0
        b_1.rect.x+=2
        m_1.rect.x+=2
    elif gravidadeb1_pld:
        pulo1=0
        b_1.rect.x-=2
        m_1.rect.x-=2
    else:
        pulo1=0
        
        
        
        
        
#COLISAO DOS BEBES COM AS MAMADEIRAS E PLATAFORMAS            
    colisao_b_m2= pygame.sprite.spritecollide(b_1,mamadeira_2, False)
    colisao_m_p2=pygame.sprite.spritecollide(m_2,plataforma_group, False)
    if colisao_b_m2 or colisao_m_p2 or m_2.rect.x>900 or m_2.rect.x<0 or m_2.rect.y<-500:
        m_2.vy=vy_inicial2
        m_2.rect.x=b_2.rect.x+d_mao_pe
        m_2.rect.y=b_2.rect.y+d_mao_mao-10
        m_2.parar_atirar()
        m_bebe=3
        if trocou_de_mao_2:
            b_2.image=pygame.transform.flip(b_2.image, True, False)
        if colisao_b_m2:
            b_1.vida-=20
            b_1.health()
            if b_1.rect.x<800 and b_1.rect.x>50:
                if trocou_de_mao_2:
                    b_1.rect.x-=50
                    m_1.rect.x-=50
                elif not trocou_de_mao_2:
                    b_1.rect.x+=50
                    m_1.rect.x+=50
                if b_1.vida==0:
                    bebe_1.remove(b_1)
                    mamadeira_1.remove(m_1)
        trocou_de_mao_2=False
        movimento_1=True
        atirou=False
        m_2.vx=vx_inicial




       
    colisao_b_m1 = pygame.sprite.spritecollide(b_2,mamadeira_1, False)
    colisao_m_p1=pygame.sprite.spritecollide(m_1,plataforma_group, False)
    if colisao_b_m1 or colisao_m_p1 or m_1.rect.x>900 or m_1.rect.x<0 or m_1.rect.y<-500:
        m_1.vy=vy_inicial1
        m_1.rect.x=b_1.rect.x+d_mao_pe
        m_1.rect.y=b_1.rect.y+d_mao_mao-10
        m_1.parar_atirar()
        m_bebe=0
        if trocou_de_mao_1:
            b_1.image=pygame.transform.flip(b_1.image, True, False)
        if colisao_b_m1:
            b_2.vida-=20
            b_2.health()
            if b_2.rect.x<800 and b_2.rect.x>50:
                if trocou_de_mao_1:
                    b_2.rect.x-=50
                    m_2.rect.x-=50
                elif not trocou_de_mao_1:
                    b_2.rect.x+=50
                    m_2.rect.x+=50
        movimento_1=False
        atirou=False
        trocou_de_mao_1=False
        m_1.vx=vx_inicial
        
        
        
        
        
#TELA DO JOGO
    if m_bebe<=0:
        movimento_1=False
        mamadeira=mamadeira_2
        
#        timer=0
    if m_bebe>=3:
        movimento_1=True
        mamadeira=mamadeira_1
#        timer=0
    if not inicio and not control and not rules:
        tela.fill(white)
        bebe_1.draw(tela)
        bebe_2.draw(tela)
        plataforma_group.draw(tela)
        paredeb.draw(tela)
        paredeld.draw(tela)
        paredele.draw(tela)
        mamadeira_1.draw(tela)
        mamadeira_2.draw(tela)
        m=0
#        timer+=1/FPS
#        a=font3.render(str(timer), True, (black))
#        tela.blit(a,(100 - text1.get_width() // 2, 400 - text1.get_height() // 2))
        if velmax_x:
            max_x=font3.render("Velocidade maxima", True, (red))
            tela.blit(max_x,(350 - text.get_width() // 2, 500 - text.get_height() // 2))
        elif velmin_x:
            max_x=font3.render("Velocidade minima", True, (red))
            tela.blit(max_x,(350 - text.get_width() // 2, 500 - text.get_height() // 2))
        if not atirou:   
            for m in mamadeira:
                m.pre_move(tela)
        if b_2.vida<=0 or b_1.vida<=0:
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
            tela.blit(final,(420 - text.get_width() // 2, 100 - text.get_height() // 2))
            jogar_de_novo=tela.blit(final_jogar,(170 - text1.get_width() // 2, 430 - text1.get_height() // 2))
            if event.type == pygame.MOUSEBUTTONDOWN:            
                mouse_posicao=pygame.mouse.get_pos()
            if jogar_de_novo.collidepoint(mouse_posicao):
                choro.stop()
                morte=False
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
        pygame.mixer.music.stop()
        musica.play(-1)
        


                

#desenho tela de inicio

                


#desenho tela dos cpntroles
    

    pygame.display.update()
    relogio.tick(FPS)
    
choro.stop()
pygame.mixer.music.stop()
musica.stop()

pygame.display.quit()