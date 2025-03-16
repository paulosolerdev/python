#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def criar_tabuleiro():
    """Cria um tabuleiro vazio para o jogo da velha."""
    return [[' ' for _ in range(3)] for _ in range(3)]

def exibir_tabuleiro(tabuleiro):
    """Exibe o tabuleiro atual do jogo."""
    print("\n")
    for i in range(3):
        print(f" {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} ")
        if i < 2:
            print("-----------")
    print("\n")

def verificar_vitoria(tabuleiro, jogador):
    """Verifica se o jogador venceu."""
    # Verificar linhas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador:
            return True
    
    # Verificar colunas
    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == jogador:
            return True
    
    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    
    return False

def verificar_empate(tabuleiro):
    """Verifica se o jogo terminou em empate."""
    for linha in tabuleiro:
        for celula in linha:
            if celula == ' ':
                return False
    return True

def fazer_jogada(tabuleiro, jogador):
    """Permite que um jogador faça sua jogada."""
    while True:
        try:
            print(f"Jogador '{jogador}', é sua vez.")
            linha = int(input("Digite o número da linha (0, 1 ou 2): "))
            coluna = int(input("Digite o número da coluna (0, 1 ou 2): "))
            
            if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
                print("Posição inválida! As linhas e colunas devem ser 0, 1 ou 2.")
                continue
            
            if tabuleiro[linha][coluna] != ' ':
                print("Essa posição já está ocupada! Escolha outra.")
                continue
            
            tabuleiro[linha][coluna] = jogador
            return
        except ValueError:
            print("Entrada inválida! Digite apenas números.")
        except IndexError:
            print("Posição inválida! As linhas e colunas devem ser 0, 1 ou 2.")

def jogar_novamente():
    """Pergunta se os jogadores querem jogar novamente."""
    resposta = input("Deseja jogar novamente? (s/n): ").lower()
    return resposta == 's'

def jogo_da_velha():
    """Função principal que executa o jogo da velha."""
    print("=" * 30)
    print("    JOGO DA VELHA")
    print("=" * 30)
    print("\nInstruções:")
    print("- Cada jogador deve escolher uma posição no tabuleiro quando for sua vez")
    print("- As posições são definidas por linha (0, 1 ou 2) e coluna (0, 1 ou 2)")
    print("- O primeiro jogador a formar uma linha, coluna ou diagonal vence")
    print("- Se todas as posições forem preenchidas sem um vencedor, o jogo termina em empate")
    
    while True:
        # Inicializar o jogo
        tabuleiro = criar_tabuleiro()
        jogador_atual = 'X'
        jogo_terminado = False
        
        # Exibir tabuleiro inicial
        print("\nTabuleiro inicial:")
        exibir_tabuleiro(tabuleiro)
        
        # Loop principal do jogo
        while not jogo_terminado:
            # Jogador faz sua jogada
            fazer_jogada(tabuleiro, jogador_atual)
            
            # Exibir tabuleiro atualizado
            exibir_tabuleiro(tabuleiro)
            
            # Verificar se o jogador atual venceu
            if verificar_vitoria(tabuleiro, jogador_atual):
                print(f"Parabéns! Jogador '{jogador_atual}' venceu!")
                jogo_terminado = True
            # Verificar se houve empate
            elif verificar_empate(tabuleiro):
                print("O jogo terminou em empate!")
                jogo_terminado = True
            # Alternar para o próximo jogador
            else:
                jogador_atual = 'O' if jogador_atual == 'X' else 'X'
        
        # Perguntar se desejam jogar novamente
        if not jogar_novamente():
            print("Obrigado por jogar! Até a próxima!")
            break

if __name__ == "__main__":
    jogo_da_velha()
