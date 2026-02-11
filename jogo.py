import random

def jogar_adivinhacao():
    print("*********************************")
    print("Bem-vindo ao jogo de Adivinhação!")
    print("*********************************")
    
    print("Qual é o nível da dificuldade?")
    print("(1) fácil, (2) médio, (3) difícil")

    while True:
        nivel_str = input("Define o nível: ")
        if nivel_str.isdigit(): # Pequena validação para não travar se digitar letra
            nivel = int(nivel_str)
            if nivel == 1:
                total_de_tentativas = 20
                break
            elif nivel == 2:
                total_de_tentativas = 10
                break
            elif nivel == 3:
                total_de_tentativas = 5
                break
        print("Entrada inválida, tente novamente (1, 2 ou 3).")

    numero_secreto = random.randint(1, 100)
    acertou = False
    pontos = 1000 # Começando com uma pontuação maior para o jogo durar

    for rodada in range(1, total_de_tentativas + 1):
        print(f"\n--- Tentativa {rodada} de {total_de_tentativas} ---")
        chute = int(input("Digite um número entre 1 e 100: "))

        if chute == numero_secreto:
            print(f"Você acertou e fez {pontos} pontos!")
            acertou = True
            break 
        else:
            # Só perde pontos se errar
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            
            if chute > numero_secreto:
                print("O número secreto é menor!")
            else:
                print("O número secreto é maior!")

    if not acertou:
        print(f"\nQue pena! O número era {numero_secreto}. Sua pontuação final: 0")

    print("\nFim do jogo.")
    input("Pressione ENTER para sair...")

jogar_adivinhacao()