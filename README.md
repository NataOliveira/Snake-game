# 🐍 Snake Game

Um jogo da cobrinha clássico desenvolvido em Python utilizando a biblioteca **Pygame**.

## 📋 Sobre o projeto

Reimplementação do clássico jogo Snake, com sistema de pontuação, aumento progressivo de velocidade e efeitos sonoros. O jogador controla uma cobra que cresce a cada comida consumida, devendo evitar colidir com o próprio corpo.

## 🎮 Funcionalidades

- Movimentação da cobra nas 4 direções (cima, baixo, esquerda, direita)
- Bloqueio de movimento reverso (não é possível virar 180° instantaneamente)
- Cobra "atravessa" as bordas da tela (wrap-around), reaparecendo do lado oposto
- Sistema de pontuação exibido em tempo real
- Aumento progressivo de velocidade a cada comida consumida
- Crescimento do corpo da cobra proporcional à pontuação
- Detecção de colisão com o próprio corpo (Game Over)
- Tela de "Game Over" com opção de reiniciar a partida
- Música de fundo em loop e efeito sonoro ao coletar comida

## 🕹️ Controles

| Tecla | Ação |
|-------|------|
| `↑` | Mover para cima |
| `↓` | Mover para baixo |
| `←` | Mover para esquerda |
| `→` | Mover para direita |
| `R` | Reiniciar o jogo (após Game Over) |

## 🛠️ Tecnologias utilizadas

- **Python 3**
- **Pygame** — renderização gráfica, captura de eventos e áudio

## 📦 Pré-requisitos

- Python 3.8 ou superior
- Pygame instalado:

```bash
pip install pygame
```

## 📁 Estrutura de arquivos necessária

O projeto depende de dois arquivos de áudio que devem estar na mesma pasta do script:

```
📂 snake-game/
 ├── snake.py
 ├── take.mp3      # efeito sonoro ao comer
 └── music.wav      # música de fundo (loop)
```

> ⚠️ Sem esses arquivos, o jogo não iniciará, pois `pygame.mixer` tentará carregá-los na inicialização.

## ▶️ Como executar

```bash
python snake.py
```

## 🚧 Melhorias futuras (ideias)

- Extrair "número mágicos" (tamanho da tela, tamanho dos blocos, cores) para constantes no topo do arquivo
- Separar a lógica em funções/classes menores para facilitar manutenção
- Adicionar menu inicial e tela de recorde (highscore)
- Tratar o caso de arquivos de áudio ausentes sem quebrar o jogo

## 📄 Licença

Este projeto é livre para fins de estudo e aprendizado.
