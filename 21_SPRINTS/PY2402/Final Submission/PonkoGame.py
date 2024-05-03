import pygame

created = "Created By: Lael, Michely, Jonatas, Vitor"

# Iniciar o Pygame
pygame.init()

# Cores
branco = (255, 255, 255)
vermelho = (255, 0, 0)
preto = (0, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
amarelo = (255, 255, 0)
cinza = (54, 61, 56)
cinza_claro = (91, 97, 93)

# Definições de tela
largura, altura = 800, 600  # Aumentando o tamanho da tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Ponko")

# Criar traves
rect1 = pygame.Rect(4, 170, 15, 60)
rect2 = pygame.Rect(780, 170, 15, 60)  # Ajustando a posição do segundo retângulo

# Movimentos
UP = (0, -5)  # Reduzindo a velocidade vertical
DOWN = (0, 5)  # Reduzindo a velocidade vertical

# Posição inicial da bola
ball_pos = [largura // 2, altura // 2]

# Velocidade inicial da bola
ball_speed = [5, 5]  # Reduzindo a velocidade

# Pontuação
score1 = 0
score2 = 0

# Fonte para pontuação
font = pygame.font.Font(None, 36)

# Loop
jogo_ativo = True
clock = pygame.time.Clock()  # Objeto de relógio para controlar a taxa de quadros
while jogo_ativo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo_ativo = False

    # Movimentar a bola
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Verificar colisão com as bordas da tela
    if ball_pos[0] <= 0:
        # Player 2 marcou ponto
        score2 += 1
        ball_pos = [largura // 2, altura // 2]  # Reposicionar a bola ao centro
        ball_speed[0] -= 1
        ball_speed[1] += 1
        ball_speed[0] = -ball_speed[0]  # Inverter a direção da bola

    elif ball_pos[0] >= largura:
        # Player 1 marcou ponto
        score1 += 1
        ball_pos = [largura // 2, altura // 2]  # Reposicionar a bola ao centro
        ball_speed[0] += 1
        ball_speed[1] -= 1
        ball_speed[0] = -ball_speed[0]  # Inverter a direção da bola


    if ball_pos[1] <= 0 or ball_pos[1] >= altura:
        ball_speed[1] = -ball_speed[1]

    # Verificar colisão com as raquetes
    if rect1.colliderect(pygame.Rect(ball_pos[0]-10, ball_pos[1]-10, 20, 20)):
        ball_speed[0] = -ball_speed[0]  # Inverter a direção da bola horizontalmente
    if rect2.colliderect(pygame.Rect(ball_pos[0]-10, ball_pos[1]-10, 20, 20)):
        ball_speed[0] = -ball_speed[0]  # Inverter a direção da bola horizontalmente

    # Movimentar as raquetes
    keys = pygame.key.get_pressed()
    if rect1!=(4, 10, 15, 60) and keys[pygame.K_w]:
        rect1.move_ip(UP)
    if rect1 != (4, 535, 15, 60) and keys[pygame.K_s]:
        rect1.move_ip(DOWN)
    if rect2!=(780, 15, 15, 60) and keys[pygame.K_UP]:
        rect2.move_ip(UP)
    if rect2!=(780, 525, 15, 60) and keys[pygame.K_DOWN]:
        rect2.move_ip(DOWN)


    # Limpar a tela
    tela.fill(cinza)

    # Desenhar bola
    pygame.draw.circle(tela, amarelo, ball_pos, 10, 10)

    # Desenhar retângulos
    pygame.draw.rect(tela, branco, rect1)
    pygame.draw.rect(tela, branco, rect2)

    # Desenhar pontuação
    score_text = font.render(f"{score1} - {score2}", True, preto)
    tela.blit(score_text, (largura // 2 - score_text.get_width() // 2, 20))

    # Créditos
    credit = font.render(f"{created}", True, cinza_claro)
    tela.blit(credit, (160, 550))
    # Atualizar tela
    pygame.display.flip()

    # Limitar a taxa de quadros
    clock.tick(60)  # Limitando a 60 quadros por segundo

# Encerrar o Pygame
pygame.quit()