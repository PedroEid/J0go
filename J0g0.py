import pygame

def jogo():
    pygame.init()
    tela = pygame.display.set_mode([400,400])
    pygame.display.set_caption("Bem vindo ao jogo")
    fps = pygame.time.Clock()
    mamadeira = pygame.image.load("mamadeira.jpg")
    fundo = pygame.image.load("fundi1.jpg")
    bebe = pygame.image.load("bbbravo.jpg")
    
    def bebep(x,y):
        tela.blit(bebe,(x,y))
        
    def municao(x,y):
        tela.blit(mamadeira,(x,y))

    def fundo1(x,y):
        tela.blit(fundo(x,y))
    
    sair = False
    while sair!= True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True 
        fps.tick(30)     
        pygame.display.update()
        
    pygame.quit()
    
    
    
jogo()