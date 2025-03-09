import tkinter as tk
from tkinter import messagebox
import random

class JogoDaVelha:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha")
        self.root.resizable(False, False)
        
        self.jogador_atual = "X"
        self.tabuleiro = [""] * 9
        self.jogando = True
        
        self.botoes = []
        for i in range(3):
            for j in range(3):
                btn = tk.Button(root, text="", font=('Arial', 20, 'bold'), width=5, height=2,
                               command=lambda row=i, col=j: self.fazer_jogada(row, col))
                btn.grid(row=i, column=j, padx=2, pady=2)
                self.botoes.append(btn)
        
        self.status_label = tk.Label(root, text=f"Vez do jogador: {self.jogador_atual}", font=('Arial', 12))
        self.status_label.grid(row=3, column=0, columnspan=3, pady=10)
        
        self.reset_button = tk.Button(root, text="Reiniciar Jogo", font=('Arial', 12),
                                     command=self.reiniciar_jogo)
        self.reset_button.grid(row=4, column=0, columnspan=3, pady=5)
        
        self.modo_jogo_var = tk.StringVar(value="2 Jogadores")
        self.modo_jogo = tk.OptionMenu(root, self.modo_jogo_var, "2 Jogadores", "Contra Computador")
        self.modo_jogo.grid(row=5, column=0, columnspan=3, pady=5)
        
    def fazer_jogada(self, row, col):
        if not self.jogando:
            return
            
        indice = row * 3 + col
        
        if self.tabuleiro[indice] == "":
            self.tabuleiro[indice] = self.jogador_atual
            self.botoes[indice].config(text=self.jogador_atual, 
                                      fg="blue" if self.jogador_atual == "X" else "red")
            
            if self.verificar_vitoria():
                messagebox.showinfo("Fim de Jogo", f"Jogador {self.jogador_atual} venceu!")
                self.jogando = False
            elif "" not in self.tabuleiro:
                messagebox.showinfo("Fim de Jogo", "Empate!")
                self.jogando = False
            else:
                self.jogador_atual = "O" if self.jogador_atual == "X" else "X"
                self.status_label.config(text=f"Vez do jogador: {self.jogador_atual}")
                
                # Se for modo contra computador e for a vez do O
                if self.modo_jogo_var.get() == "Contra Computador" and self.jogador_atual == "O" and self.jogando:
                    self.root.after(500, self.jogada_computador)
    
    def jogada_computador(self):
        # Lista de posições vazias
        posicoes_vazias = [i for i, x in enumerate(self.tabuleiro) if x == ""]
        if posicoes_vazias:
            escolha = random.choice(posicoes_vazias)
            row, col = divmod(escolha, 3)
            self.fazer_jogada(row, col)
    
    def verificar_vitoria(self):
        # Linhas horizontais, verticais e diagonais
        linhas_vitoria = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontais
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # verticais
            [0, 4, 8], [2, 4, 6]              # diagonais
        ]
        
        for linha in linhas_vitoria:
            if (self.tabuleiro[linha[0]] == self.tabuleiro[linha[1]] == self.tabuleiro[linha[2]] != ""):
                # Destacar a linha vencedora
                for pos in linha:
                    self.botoes[pos].config(bg="light green")
                return True
        return False

    def reiniciar_jogo(self):
        self.jogador_atual = "X"
        self.tabuleiro = [""] * 9
        self.jogando = True
    
        for btn in self.botoes:
            btn.config(text="", bg="light gray", fg="black")
        
        self.status_label.config(text=f"Vez do jogador: {self.jogador_atual}")


if __name__ == "__main__":
    root = tk.Tk()
    app = JogoDaVelha(root)
    root.mainloop()
