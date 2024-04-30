import pygame
import random

# Definição de Constantes
LARGURA_TELA = 800
ALTURA_TELA = 600
COR_PRETA = (0, 0, 0)
COR_BRANCA = (255, 255, 255)
COR_VERMELHA = (255, 0, 0)
VELOCIDADE = 10
TAMANHO_BLOCO = 20
POSICAO_INICIAL_CABECA = [LARGURA_TELA // 2, ALTURA_TELA // 2]
CORPO_INICIAL = [[POSICAO_INICIAL_CABECA[0], POSICAO_INICIAL_CABECA[1] - TAMANHO_BLOCO],
                 [POSICAO_INICIAL_CABECA[0], POSICAO_INICIAL_CABECA[1] - 2 * TAMANHO_BLOCO],
                 [POSICAO_INICIAL_CABECA[0], POSICAO_INICIAL_CABECA[1] - 3 * TAMANHO_BLOCO]]
DIRECAO_INICIAL = 'DIREITA'
DIRECOES_VALIDAS = {'ESQUERDA': [-TAMANHO_BLOCO, 0],
                    'DIREITA': [TAMANHO_BLOCO, 0],
                    'CIMA': [0, -TAMANHO_BLOCO],
                    'BAIXO': [0, TAMANHO_BLOCO]}
PONTOS = 0
FONTE = None

# Função para Inicialização do Pygame
def inicializar_pygame():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('Minhoca Simples')
    global FONTE
    FONTE = pygame.font.Font(None, 36)
    return tela

# Função para Desenhar na Tela
def desenhar_tela(tela, corpo_minhoca, comida, pontos):
    tela.fill(COR_PRETA)

    for bloco in corpo_minhoca:
        pygame.draw.rect(tela, COR_VERMELHA, pygame.Rect(bloco[0], bloco[1], TAMANHO_BLOCO, TAMANHO_BLOCO))

    pygame.draw.rect(tela, COR_BRANCA, pygame.Rect(comida[0], comida[1], TAMANHO_BLOCO, TAMANHO_BLOCO))

    texto_pontos = FONTE.render(f'Pontos: {pontos}', True, COR_BRANCA)
    tela.blit(texto_pontos, [0, 0])

    pygame.display.flip()

# Função para Gerar Comida
def gerar_comida():
    x = random.randrange(0, LARGURA_TELA - TAMANHO_BLOCO, TAMANHO_BLOCO)
    y = random.randrange(0, ALTURA_TELA - TAMANHO_BLOCO, TAMANHO_BLOCO)
    return [x, y]

# Função para Verificar Colisão
def verificar_colisao(corpo_minhoca, comida):
    for bloco in corpo_minhoca:
        if bloco == comida:
            return True
    return False

# Função para Atualizar Corpo da Minhoca
def atualizar_corpo_minhoca(corpo_minhoca, direcao):
    nova_cabeca = [corpo_minhoca[0][0] + DIRECOES_VALIDAS[direcao][0],
                   corpo_minhoca[0][1] + DIRECOES_VALIDAS[direcao][1]]
    corpo_minhoca.insert(0, nova_cabeca)
    corpo_minhoca.pop()
    return corpo_minhoca

# Função para Tratar Eventos do Jogo
def tratar_eventos(corpo_minhoca, direcao):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direcao != 'DIREITA':
                direcao = 'ESQUERDA'
            elif event.key == pygame.K_RIGHT and direcao != 'ESQUERDA':
                direcao = 'DIREITA'
            elif event.key == pygame.K_UP and direcao != 'BAIXO':
                direcao = 'CIMA'
            elif event.key == pygame.K_DOWN and direcao != 'CIMA':
                direcao = 'BAIXO'
    return direcao

def main():
    global PONTOS  # Declarando PONTOS como global
    tela = inicializar_pygame()
    clock = pygame.time.Clock()

    corpo_minhoca = CORPO_INICIAL.copy()
    comida = gerar_comida()
    direcao = DIRECAO_INICIAL

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        direcao = tratar_eventos(corpo_minhoca, direcao)
        corpo_minhoca = atualizar_corpo_minhoca(corpo_minhoca, direcao)

        if verificar_colisao(corpo_minhoca, comida):
            comida = gerar_comida()
            PONTOS += 1

        desenhar_tela(tela, corpo_minhoca, comida, PONTOS)
        clock.tick(VELOCIDADE)

if __name__ == "__main__":
    main()
