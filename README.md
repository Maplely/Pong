# Pong

Jogo Pong clássico para dois jogadores, desenvolvido em Python com Pygame.

## Funcionalidades

- Partida local para dois jogadores no mesmo teclado
- Movimento da bola com colisão no teto, no chão e nas raquetes
- Raquetes limitadas aos limites da tela
- Movimento independente de FPS usando `dt` (delta time)
- Bola retorna ao centro quando sai pelas laterais

## Controles

| Jogador | Subir | Descer |
|---------|-------|--------|
| Jogador 1 | `W` | `S` |
| Jogador 2 | `Seta para cima` | `Seta para baixo` |

## Requisitos

- Python 3.10+
- Pygame

## Como executar

1. Clone ou baixe o projeto e entre na pasta:

   ```bash
   cd Pong
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Execute o jogo:

   ```bash
   python pong.py
   ```

## Estrutura do projeto

```text
Pong/
├── .gitignore
├── README.md
├── pong.py
└── requirements.txt
```

## Próximas melhorias

- Placar
- Ângulo de rebate conforme o ponto de contato na raquete
- Saque com direção aleatória
- Sons e condição de vitória/reinício
