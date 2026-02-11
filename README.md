Markdown
# 🎮 Jogo de Adivinhação

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

Um jogo interativo de lógica onde o desafio é descobrir o número secreto entre 1 e 100. O projeto conta com duas versões: uma para **Terminal (Python)** e outra com **Interface Web (HTML/JS)**.

## ⚙️ Como Funciona
O computador escolhe um número aleatório. O objetivo do jogador é adivinhar esse número com o menor número de tentativas possível, gerenciando sua pontuação.

### 🏆 Sistema de Pontuação
O jogador inicia com **1000 pontos**. A cada erro, a diferença entre o chute e o número real é subtraída do total:
> `pontos = pontos - abs(numero_secreto - chute)`

---

## 🚀 Versões do Projeto

### 1. Versão Terminal (Python)
Focada em lógica pura e estruturada.
* **Requisitos:** Python 3.x instalado.
* **Como rodar:**
  ```bash
  python jogo.py
2. Versão Web (Front-end)
Interface moderna e responsiva para jogar no navegador.

Tecnologias: HTML5, CSS3 e JavaScript (Vanilla).

Como rodar: Basta abrir o arquivo index.html em qualquer navegador ou acessar pelo GitHub Pages.

🕹️ Funcionalidades
Níveis de Dificuldade:

🟢 Fácil: 20 tentativas.

🟡 Médio: 10 tentativas.

🔴 Difícil: 5 tentativas.

Dicas Dinâmicas: O jogo informa se o número secreto é maior ou menor que o palpite atual.

Validação de Dados: Impede entradas inválidas ou campos vazios.

🛠️ Conceitos Praticados
[x] Geração de números aleatórios.

[x] Estruturas de repetição (for, while).

[x] Manipulação de DOM (na versão Web).

[x] Lógica matemática com funções absolutas.

Desenvolvido como projeto de estudos para lógica de programação. 🚀


---