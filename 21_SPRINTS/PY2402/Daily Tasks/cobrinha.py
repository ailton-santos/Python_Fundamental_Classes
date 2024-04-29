import pygame

#Inicializar módulo
pygame.init()

#Criando uma janela
tela = pygame.display.set_mode((1250,650))

#Definir Frame
clock = pygame.time.Clock()

#Colocando um quadrado
quadrado = pygame.Rect(100, 100, 50, 50)

#Loop
executando = True
while executando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executando = False
        #Tecla pressionada
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                quadrado.move_ip([0, 20])
            if event.key == pygame.K_UP:
                quadrado.move_ip([0, -20])
            if event.key == pygame.K_LEFT:
                quadrado.move_ip([-20, 0])
            if event.key == pygame.K_RIGHT:
                quadrado.move_ip([20, 0])
    #Elemento da Tela
    pygame.draw.rect(tela, (255, 0, 0), quadrado)
    #Configurar Frame
    clock.tick(27)
    pygame.display.update()
pygame.quit()