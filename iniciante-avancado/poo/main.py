"""
Programa principal que integra diferentes funcionalidades
demonstradas nos arquivos do projeto
"""

from datetime import datetime
import random
import sys
import os

class GerenciadorVendas:
    def __init__(self):
        self.vendas = []
        self.comissao = 0.06
        self.salario_fixo = 500.00

    def registrar_venda(self, valor):
        self.vendas.append(valor)
        return self.calcular_comissao(valor)

    def calcular_comissao(self, valor_venda):
        return valor_venda * self.comissao

    def calcular_faturamento(self):
        total_comissoes = sum(self.calcular_comissao(v) for v in self.vendas)
        return self.salario_fixo + total_comissoes

class GerenciadorPedidos:
    def __init__(self):
        self.pedidos = []
        
    def novo_pedido(self):
        pedido = []
        while True:
            produto = input('Digite o nome do produto: ')
            preco = float(input('Digite o preço: '))
            pedido.append([produto, preco])
            
            if input('Cadastrar mais algum item? (S/N): ').lower() != 's':
                break
                
        self.pedidos.append(pedido)
        return pedido

    def calcular_total(self, pedido):
        return sum(item[1] for item in pedido)

class PizzariaSistema:
    def __init__(self):
        self.precos = {
            'S': 15,
            'M': 20,
            'L': 25
        }
        self.adicional_pepperoni = {
            'S': 2,
            'L': 3,
            'M': 3
        }
        self.adicional_queijo = 1

    def calcular_preco(self, tamanho, pepperoni, queijo_extra):
        if tamanho not in self.precos:
            return 0
            
        total = self.precos[tamanho]
        
        if pepperoni == 'Y':
            total += self.adicional_pepperoni[tamanho]
            
        if queijo_extra == 'Y':
            total += self.adicional_queijo
            
        return total

def main():
    # Instanciando as classes
    vendas = GerenciadorVendas()
    pedidos = GerenciadorPedidos()
    pizzaria = PizzariaSistema()
    
    # Menu principal
    while True:
        print("\n=== Sistema Integrado ===")
        print("1. Registrar Venda")
        print("2. Novo Pedido")
        print("3. Pedido de Pizza")
        print("4. Informações do Sistema")
        print("5. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == '1':
            valor = float(input("Digite o valor da venda: "))
            comissao = vendas.registrar_venda(valor)
            print(f"Comissão calculada: R${comissao:.2f}")
            
        elif opcao == '2':
            pedido = pedidos.novo_pedido()
            total = pedidos.calcular_total(pedido)
            print(f"\nTotal do pedido: R${total:.2f}")
            
        elif opcao == '3':
            tamanho = input('Tamanho da pizza (S/M/L): ').upper()
            pepperoni = input('Adicionar pepperoni? (Y/N): ').upper()
            queijo = input('Queijo extra? (Y/N): ').upper()
            
            total = pizzaria.calcular_preco(tamanho, pepperoni, queijo)
            print(f"\nTotal da pizza: R${total:.2f}")
            
        elif opcao == '4':
            print(f"\nSistema Operacional: {sys.platform.title()}")
            print(f"Versão Python: {sys.version.split()[0]}")
            print(f"Diretório atual: {os.getcwd()}")
            print(f"Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            
        elif opcao == '5':
            print("\nEncerrando o programa...")
            break
            
        else:
            print("\nOpção inválida!")

if __name__ == "__main__":
    main()
