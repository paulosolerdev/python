# Programa de Gerenciamento de Tarefas
import json
from datetime import datetime, timedelta
import os
import time
from typing import List, Dict
import colorama
from colorama import Fore, Style

# Inicializar colorama para cores no terminal
try:
    colorama.init()
    USE_COLORS = True
except Exception as e:
    print(f"Warning: Colorama não pôde ser inicializado: {e}")
    USE_COLORS = False

# Arquivo para armazenar as tarefas
ARQUIVO_TAREFAS = 'tarefas.json'
ARQUIVO_CONFIG = 'config.json'

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = self.carregar_tarefas()
        self.config = self.carregar_config()
        
    def __del__(self):
        if USE_COLORS:
            colorama.deinit()
    
    def color(self, color_code: str, text: str) -> str:
        """Helper method para aplicar cores de forma segura"""
        if USE_COLORS:
            return f"{color_code}{text}{Style.RESET_ALL}"
        return text
    
    def carregar_config(self) -> dict:
        try:
            with open(ARQUIVO_CONFIG, 'r') as arquivo:
                return json.load(arquivo)
        except FileNotFoundError:
            return {
                'categorias': ['Pessoal', 'Trabalho', 'Estudos', 'Saúde', 'Outros'],
                'lembretes': True,
                'tema': 'claro'
            }
    
    def salvar_config(self):
        with open(ARQUIVO_CONFIG, 'w') as arquivo:
            json.dump(self.config, arquivo)
    
    def carregar_tarefas(self) -> List[Dict]:
        try:
            with open(ARQUIVO_TAREFAS, 'r') as arquivo:
                return json.load(arquivo)
        except FileNotFoundError:
            return []
    
    def salvar_tarefas(self):
        with open(ARQUIVO_TAREFAS, 'w') as arquivo:
            json.dump(self.tarefas, arquivo)
    
    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def exibir_cabecalho(self):
        self.limpar_tela()
        print(self.color(Fore.CYAN, "╔════════════════════════════════════════════════════════════════╗"))
        print(self.color(Fore.CYAN, "║" + " " * 20 + "Gerenciador de Tarefas Pro" + " " * 20 + "║"))
        print(self.color(Fore.CYAN, "╚════════════════════════════════════════════════════════════════╝\n"))
    
    def exibir_menu(self):
        self.exibir_cabecalho()
        print(f"{Fore.YELLOW}Menu Principal:{Style.RESET_ALL}")
        print("1. 📝 Adicionar Tarefa")
        print("2. 👀 Visualizar Tarefas")
        print("3. ❌ Remover Tarefa")
        print("4. ✅ Marcar Tarefa como Concluída")
        print("5. 📊 Estatísticas")
        print("6. ⚙️  Configurações")
        print("7. 🚪 Sair")
        print("\n" + "=" * 60)
    
    def adicionar_tarefa(self):
        self.exibir_cabecalho()
        print(f"{Fore.YELLOW}Adicionar Nova Tarefa{Style.RESET_ALL}")
        
        titulo = input("📌 Título da tarefa: ")
        descricao = input("📄 Descrição: ")
        
        print("\nCategorias disponíveis:")
        for i, categoria in enumerate(self.config['categorias'], 1):
            print(f"{i}. {categoria}")
        
        try:
            cat_index = int(input("\nEscolha a categoria (número): ")) - 1
            categoria = self.config['categorias'][cat_index]
        except (ValueError, IndexError):
            print(f"{Fore.RED}Categoria inválida. Usando 'Outros'.{Style.RESET_ALL}")
            categoria = 'Outros'
        
        prioridade = input("🎯 Prioridade (alta, média, baixa): ").lower()
        data_vencimento = input("📅 Data de vencimento (dd/mm/aaaa): ")
        
        try:
            data = datetime.strptime(data_vencimento, '%d/%m/%Y')
        except ValueError:
            print(f"{Fore.RED}Data inválida. A tarefa não foi adicionada.{Style.RESET_ALL}")
            return
        
        nova_tarefa = {
            'id': len(self.tarefas) + 1,
            'titulo': titulo,
            'descricao': descricao,
            'categoria': categoria,
            'prioridade': prioridade,
            'data_vencimento': data_vencimento,
            'data_criacao': datetime.now().strftime('%d/%m/%Y %H:%M'),
            'concluida': False,
            'subtasks': []
        }
        
        self.tarefas.append(nova_tarefa)
        self.salvar_tarefas()
        print(f"\n{Fore.GREEN}✓ Tarefa adicionada com sucesso!{Style.RESET_ALL}")
        time.sleep(2)
    
    def visualizar_tarefas(self):
        self.exibir_cabecalho()
        print(f"{Fore.YELLOW}Suas Tarefas:{Style.RESET_ALL}")
        
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada.")
            return
        
        # Agrupar tarefas por categoria
        tarefas_por_categoria = {}
        for tarefa in self.tarefas:
            if tarefa['categoria'] not in tarefas_por_categoria:
                tarefas_por_categoria[tarefa['categoria']] = []
            tarefas_por_categoria[tarefa['categoria']].append(tarefa)
        
        for categoria, tarefas in tarefas_por_categoria.items():
            print(f"\n{Fore.CYAN}=== {categoria} ==={Style.RESET_ALL}")
            for tarefa in tarefas:
                status = "✓" if tarefa['concluida'] else "✗"
                cor_status = Fore.GREEN if tarefa['concluida'] else Fore.RED
                
                print(f"\n{cor_status}{status}{Style.RESET_ALL} {tarefa['titulo']}")
                print(f"   📝 {tarefa['descricao']}")
                print(f"   🎯 Prioridade: {tarefa['prioridade']}")
                print(f"   📅 Vencimento: {tarefa['data_vencimento']}")
                if tarefa['subtasks']:
                    print("   📋 Subtarefas:")
                    for subtask in tarefa['subtasks']:
                        print(f"      - {subtask}")
        
        input("\nPressione Enter para continuar...")
    
    def remover_tarefa(self):
        self.exibir_cabecalho()
        print(f"{Fore.YELLOW}Remover Tarefa{Style.RESET_ALL}")
        
        if not self.tarefas:
            print("Nenhuma tarefa para remover.")
            return
        
        for i, tarefa in enumerate(self.tarefas, 1):
            print(f"{i}. {tarefa['titulo']}")
        
        try:
            indice = int(input("\nDigite o número da tarefa que deseja remover: ")) - 1
            tarefa_removida = self.tarefas.pop(indice)
            self.salvar_tarefas()
            print(f"\n{Fore.GREEN}✓ Tarefa '{tarefa_removida['titulo']}' removida com sucesso!{Style.RESET_ALL}")
        except (IndexError, ValueError):
            print(f"{Fore.RED}Índice inválido. Tente novamente.{Style.RESET_ALL}")
        
        time.sleep(2)
    
    def marcar_tarefa_concluida(self):
        self.exibir_cabecalho()
        print(f"{Fore.YELLOW}Marcar Tarefa como Concluída{Style.RESET_ALL}")
        
        if not self.tarefas:
            print("Nenhuma tarefa para marcar como concluída.")
            return
        
        for i, tarefa in enumerate(self.tarefas, 1):
            if not tarefa['concluida']:
                print(f"{i}. {tarefa['titulo']}")
        
        try:
            indice = int(input("\nDigite o número da tarefa que deseja marcar como concluída: ")) - 1
            self.tarefas[indice]['concluida'] = True
            self.salvar_tarefas()
            print(f"\n{Fore.GREEN}✓ Tarefa '{self.tarefas[indice]['titulo']}' marcada como concluída!{Style.RESET_ALL}")
        except (IndexError, ValueError):
            print(f"{Fore.RED}Índice inválido. Tente novamente.{Style.RESET_ALL}")
        
        time.sleep(2)
    
    def exibir_estatisticas(self):
        self.exibir_cabecalho()
        print(f"{Fore.YELLOW}Estatísticas{Style.RESET_ALL}")
        
        total_tarefas = len(self.tarefas)
        tarefas_concluidas = sum(1 for t in self.tarefas if t['concluida'])
        tarefas_pendentes = total_tarefas - tarefas_concluidas
        
        print(f"\n📊 Total de Tarefas: {total_tarefas}")
        print(f"✅ Concluídas: {tarefas_concluidas}")
        print(f"⏳ Pendentes: {tarefas_pendentes}")
        
        if total_tarefas > 0:
            percentual = (tarefas_concluidas / total_tarefas) * 100
            print(f"📈 Progresso: {percentual:.1f}%")
        
        # Estatísticas por categoria
        print("\n📑 Tarefas por Categoria:")
        for categoria in self.config['categorias']:
            total = sum(1 for t in self.tarefas if t['categoria'] == categoria)
            concluidas = sum(1 for t in self.tarefas if t['categoria'] == categoria and t['concluida'])
            print(f"\n{categoria}:")
            print(f"  Total: {total}")
            print(f"  Concluídas: {concluidas}")
            if total > 0:
                print(f"  Progresso: {(concluidas/total)*100:.1f}%")
        
        input("\nPressione Enter para continuar...")
    
    def configuracoes(self):
        while True:
            self.exibir_cabecalho()
            print(f"{Fore.YELLOW}Configurações{Style.RESET_ALL}")
            print("1. Gerenciar Categorias")
            print("2. Ativar/Desativar Lembretes")
            print("3. Alterar Tema")
            print("4. Voltar")
            
            opcao = input("\nEscolha uma opção: ")
            
            if opcao == '1':
                self.gerenciar_categorias()
            elif opcao == '2':
                self.config['lembretes'] = not self.config['lembretes']
                self.salvar_config()
                print(f"\n{Fore.GREEN}✓ Lembretes {'ativados' if self.config['lembretes'] else 'desativados'}!{Style.RESET_ALL}")
                time.sleep(2)
            elif opcao == '3':
                self.config['tema'] = 'escuro' if self.config['tema'] == 'claro' else 'claro'
                self.salvar_config()
                print(f"\n{Fore.GREEN}✓ Tema alterado para {self.config['tema']}!{Style.RESET_ALL}")
                time.sleep(2)
            elif opcao == '4':
                break
    
    def gerenciar_categorias(self):
        self.exibir_cabecalho()
        print(f"{Fore.YELLOW}Gerenciar Categorias{Style.RESET_ALL}")
        
        print("\nCategorias atuais:")
        for i, categoria in enumerate(self.config['categorias'], 1):
            print(f"{i}. {categoria}")
        
        print("\nOpções:")
        print("1. Adicionar Categoria")
        print("2. Remover Categoria")
        print("3. Voltar")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == '1':
            nova_categoria = input("\nDigite o nome da nova categoria: ")
            if nova_categoria not in self.config['categorias']:
                self.config['categorias'].append(nova_categoria)
                self.salvar_config()
                print(f"\n{Fore.GREEN}✓ Categoria '{nova_categoria}' adicionada!{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Esta categoria já existe!{Style.RESET_ALL}")
        
        elif opcao == '2':
            try:
                indice = int(input("\nDigite o número da categoria que deseja remover: ")) - 1
                categoria_removida = self.config['categorias'].pop(indice)
                self.salvar_config()
                print(f"\n{Fore.GREEN}✓ Categoria '{categoria_removida}' removida!{Style.RESET_ALL}")
            except (IndexError, ValueError):
                print(f"{Fore.RED}Índice inválido!{Style.RESET_ALL}")
        
        time.sleep(2)
    
    def verificar_lembretes(self):
        if not self.config['lembretes']:
            return
        
        hoje = datetime.now()
        for tarefa in self.tarefas:
            if not tarefa['concluida']:
                try:
                    data_vencimento = datetime.strptime(tarefa['data_vencimento'], '%d/%m/%Y')
                    dias_restantes = (data_vencimento - hoje).days
                    
                    if 0 <= dias_restantes <= 3:
                        print(f"\n{Fore.YELLOW}⚠️ Lembrete: A tarefa '{tarefa['titulo']}' vence em {dias_restantes} dias!{Style.RESET_ALL}")
                except ValueError:
                    continue
    
    def main(self):
        while True:
            self.exibir_menu()
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1':
                self.adicionar_tarefa()
            elif opcao == '2':
                self.visualizar_tarefas()
            elif opcao == '3':
                self.remover_tarefa()
            elif opcao == '4':
                self.marcar_tarefa_concluida()
            elif opcao == '5':
                self.exibir_estatisticas()
            elif opcao == '6':
                self.configuracoes()
            elif opcao == '7':
                print(f"\n{Fore.GREEN}Obrigado por usar o Gerenciador de Tarefas Pro! Até logo!{Style.RESET_ALL}")
                break
            else:
                print(f"{Fore.RED}Opção inválida. Tente novamente.{Style.RESET_ALL}")
                time.sleep(2)
            
            self.verificar_lembretes()

if __name__ == "__main__":
    gerenciador = GerenciadorTarefas()
    gerenciador.main()
