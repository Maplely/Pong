# Importa a biblioteca pygame
import pygame
# Inicia todos os modulos do pygame
pygame.init()

# Criação de variavel para ficar mais facil compreender o tamanho da tela
largura_t = 800
altura_t = 600

# Dados tecnicos
# Seta o quadro em branco pronto para receber conteudo 
screen = pygame.display.set_mode((largura_t, altura_t))
tela_rect = screen.get_rect()  # Guarda os limites da tela para usar no clamp_ip
clock = pygame.time.Clock()    # Controla o tempo entre frames (usado para gerar o dt)

# Dados do jogo

# Hitbox / dados lógicos da bola (o desenho acontece lá dentro do while)
bola = pygame.Rect(0, 0, 15, 15)

# Hitbox / dados lógicos das raquetes
raquete1 = pygame.Rect(0, 0, 10, 90)
raquete2 = pygame.Rect(0, 0, 10, 90)

# Aqui se encontra o controle da posição inicial dos objetos
bola.center = (largura_t // 2, altura_t // 2)
raquete2.midright = (largura_t - 30, altura_t // 2)
raquete1.midleft = (30, altura_t // 2)

# Posições exatas em float (o Rect só guarda inteiros, então guardamos os decimais aqui)
bola_x = float(bola.x)
bola_y = float(bola.y)
raquete1_y = float(raquete1.y)
raquete2_y = float(raquete2.y)

# Velocidades em PIXELS POR SEGUNDO
vel_x = 300.0
vel_y = 300.0
vel_raquete = 420.0

keep_alive = True

# Basicamente um keep alive que mantem o jogo aberto enquanto ele for true
while keep_alive:
    # Calcula o delta time (tempo em segundos desde o último frame) e limita a 60 FPS
    dt = clock.tick(60) / 1000.0

    # --- 1. EVENTOS ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_alive = False

    # --- 2. MOVIMENTO E REGRAS ---
    # Atualiza a posição exata (float) da bola multiplicando pelo dt
    bola_x += vel_x * dt
    bola_y += vel_y * dt
    bola.x = round(bola_x)
    bola.y = round(bola_y)

    # Jogador 1 (W e S)
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w]:
        raquete1_y -= vel_raquete * dt
    if teclas[pygame.K_s]:
        raquete1_y += vel_raquete * dt

    # Jogador 2 (Setas Cima e Baixo)
    if teclas[pygame.K_UP]:
        raquete2_y -= vel_raquete * dt
    if teclas[pygame.K_DOWN]:
        raquete2_y += vel_raquete * dt

    # Atualiza os Rects das raquetes com as posições arredondadas
    raquete1.y = round(raquete1_y)
    raquete2.y = round(raquete2_y)

    # Para a bola quicar no teto e no chão usamos top e bottom
    if bola.top <= 0 or bola.bottom >= altura_t:
        vel_y *= -1
        bola.clamp_ip(tela_rect)  # Garante que não fique presa na borda
        bola_y = float(bola.y)    # Sincroniza o float com a correção do Rect

    # Colisão com a raquete 1 (só rebate se estiver indo para a esquerda)
    if bola.colliderect(raquete1) and vel_x < 0:
        vel_x *= -1
        bola.left = raquete1.right  # Empurra a bola para fora da raquete
        bola_x = float(bola.x)      # Sincroniza o float com a nova posição

    # Colisão com a raquete 2 (só rebate se estiver indo para a direita)
    if bola.colliderect(raquete2) and vel_x > 0:
        vel_x *= -1
        bola.right = raquete2.left  # Empurra a bola para fora da raquete
        bola_x = float(bola.x)      # Sincroniza o float com a nova posição

    # Se passar pelas bordas laterais, volta a bola para o centro
    if bola.left <= 0 or bola.right >= largura_t:
        bola.center = (largura_t // 2, altura_t // 2)
        bola_x = float(bola.x)
        bola_y = float(bola.y)
        vel_x *= -1

    # Para as raquetes não voarem para fora da tela usamos clamp_ip
    raquete1.clamp_ip(tela_rect)
    raquete2.clamp_ip(tela_rect)
    raquete1_y = float(raquete1.y)  # Sincroniza caso o clamp_ip tenha barrado na borda
    raquete2_y = float(raquete2.y)

    # --- 3. RENDERIZAÇÃO ---
    # Como esta dentro do while ele printa preto na tela
    # sempre que uma animação ocorre não deixando rastros da anterior
    screen.fill((0, 0, 0))
    
    # Printa os objetos na tela
    pygame.draw.rect(screen, (255, 255, 255), raquete1)
    pygame.draw.rect(screen, (255, 255, 255), raquete2)
    pygame.draw.rect(screen, (255, 255, 255), bola)
    
    # Atualiza o monitor com tudo que foi desenhado neste frame
    pygame.display.flip()

# Encerra os módulos do pygame com segurança ao sair do loop
pygame.quit()