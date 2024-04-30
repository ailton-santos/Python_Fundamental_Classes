import pygame

#incializar módulo
pygame.init()

#criando uma janela
tela=pygame.display.set_mode((1300,650))

#Definir frama
clock=pygame.time.Clock()

#colocando um quadrado
quadrado=pygame.Rect(100,100,50,50)

#loop
executando=True
while executando:
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            executando=False
        #Tecla pressionada
        if evento.type==pygame.KEYDOWN:
            if evento.key==pygame.K_DOWN:
                quadrado.move_ip([0,20])
            if evento.key==pygame.K_UP:
                quadrado.move_ip([0,-20])
            if evento.key==pygame.K_LEFT:
                quadrado.move_ip([-20,0])
            if evento.key==pygame.K_RIGHT:
                quadrado.move_ip([20,0])
    #elemento da tela
    pygame.draw.rect(tela,(120,26,10),quadrado)
    #Configurar frame
    clock.tick(27)
    pygame.display.update()
pygame.quit()