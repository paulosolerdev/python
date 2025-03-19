import random
import time
import os
import sys
from getpass import getpass

class TerminalHacker:
    def __init__(self):
        self.username = ""
        self.level = 1
        self.reputation = 0
        self.skills = {
            "encryption": 1,
            "networking": 1,
            "social_engineering": 1,
            "malware": 1
        }
        self.missions_completed = 0
        self.current_ip = "127.0.0.1"
        self.connected = False
        self.target_systems = [
            {"name": "LocalCorp Server", "difficulty": 1, "type": "corporate", "ip": "192.168.1.45"},
            {"name": "City Library Database", "difficulty": 2, "type": "public", "ip": "203.45.67.89"},
            {"name": "ShadowNet Node", "difficulty": 3, "type": "darkweb", "ip": "78.34.56.123"},
            {"name": "Government Firewall", "difficulty": 4, "type": "government", "ip": "45.67.89.210"},
            {"name": "MegaCorp Mainframe", "difficulty": 5, "type": "corporate", "ip": "156.78.90.231"}
        ]
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def type_text(self, text, delay=0.03):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
        
    def show_banner(self):
        self.clear_screen()
        banner = """
        ████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗         
        ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║         
           ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║         
           ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║         
           ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗    
           ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝    
                                                                              
        ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗                      
        ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗                     
        ███████║███████║██║     █████╔╝ █████╗  ██████╔╝                     
        ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗                     
        ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║                     
        ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                     
        """
        print(banner)
        print(f"Conectado como: {self.username} | Nível: {self.level} | Reputação: {self.reputation}")
        print(f"IP atual: {self.current_ip} | Status: {'Conectado' if self.connected else 'Desconectado'}")
        print("="*80)
        
    def login(self):
        self.clear_screen()
        print("\n\n")
        self.type_text("Iniciando sistema...", 0.05)
        time.sleep(0.5)
        self.type_text("Carregando módulos de segurança...", 0.05)
        time.sleep(0.5)
        self.type_text("Estabelecendo conexão segura...", 0.05)
        time.sleep(0.5)
        self.type_text("Conexão estabelecida.", 0.05)
        time.sleep(1)
        
        print("\n" + "="*50)
        print("TERMINAL HACKER - SISTEMA DE ACESSO SEGURO")
        print("="*50 + "\n")
        
        while True:
            self.username = input("Login: ")
            if self.username.strip():
                break
            else:
                print("Nome de usuário inválido. Tente novamente.")
        
        password = getpass("Senha: ")
        
        print("\nAutenticando", end="")
        for _ in range(5):
            print(".", end="", flush=True)
            time.sleep(0.3)
        print("\n")
        
        self.type_text("Acesso concedido. Bem-vindo ao Terminal Hacker, " + self.username + ".")
        time.sleep(1)
        
    def show_help(self):
        commands = {
            "help": "Mostra esta lista de comandos",
            "scan": "Escaneia redes em busca de alvos",
            "connect <ip>": "Conecta a um sistema remoto",
            "disconnect": "Desconecta do sistema atual",
            "crack": "Tenta quebrar a senha do sistema conectado",
            "status": "Mostra seu status atual",
            "skills": "Mostra suas habilidades",
            "upgrade <skill>": "Melhora uma habilidade",
            "missions": "Lista missões disponíveis",
            "accept <id>": "Aceita uma missão",
            "clear": "Limpa a tela",
            "exit": "Sai do jogo"
        }
        
        print("\n=== COMANDOS DISPONÍVEIS ===")
        for cmd, desc in commands.items():
            print(f"{cmd:20} - {desc}")
        print()
        
    def scan_network(self):
        print("\nEscaneando rede em busca de sistemas vulneráveis...")
        progress = 0
        while progress < 100:
            progress += random.randint(5, 15)
            progress = min(progress, 100)
            sys.stdout.write(f"\rProgresso: [{progress*'#':{100}s}] {progress}%")
            sys.stdout.flush()
            time.sleep(0.2)
        print("\n")
        
        available_targets = []
        for target in self.target_systems:
            if target["difficulty"] <= self.level + 1:
                available_targets.append(target)
        
        if not available_targets:
            print("Nenhum alvo encontrado na sua faixa de habilidade.")
            return
        
        print("Sistemas encontrados:")
        for i, target in enumerate(available_targets):
            print(f"{i+1}. {target['name']} ({target['ip']}) - Tipo: {target['type']}, Dificuldade: {target['difficulty']}")
        print()
        
    def connect(self, ip):
        target = None
        for t in self.target_systems:
            if t["ip"] == ip:
                target = t
                break
                
        if not target:
            print(f"Erro: IP {ip} não encontrado na rede.")
            return
            
        print(f"\nTentando conectar a {target['name']} ({ip})...")
        for i in range(5):
            dots = "." * (i % 4)
            sys.stdout.write(f"\rEstabelecendo conexão{dots:4}")
            sys.stdout.flush()
            time.sleep(0.3)
            
        success_chance = min(90, 40 + (self.skills["networking"] * 10) - (target["difficulty"] * 10))
        if random.randint(1, 100) <= success_chance:
            print(f"\nConexão estabelecida com {target['name']}!")
            self.connected = True
            self.current_ip = ip
        else:
            print(f"\nFalha na conexão. Firewall bloqueou o acesso.")
            self.connected = False
            
    def disconnect(self):
        if not self.connected:
            print("Você não está conectado a nenhum sistema.")
            return
            
        print("Desconectando", end="")
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.3)
        print()
        
        self.connected = False
        self.current_ip = "127.0.0.1"
        print("Desconectado com sucesso. Retornando ao seu sistema local.")
        
    def crack_password(self):
        if not self.connected:
            print("Você precisa estar conectado a um sistema para quebrar senhas.")
            return
            
        target = None
        for t in self.target_systems:
            if t["ip"] == self.current_ip:
                target = t
                break
                
        if not target:
            print("Erro: Sistema não reconhecido.")
            return
            
        print(f"\nIniciando ataque de força bruta em {target['name']}...")
        
        # Mini-jogo de quebra de senha
        password_length = target["difficulty"] + 2
        charset = "0123456789ABCDEF"
        password = ''.join(random.choice(charset) for _ in range(password_length))
        attempts = 3 + self.skills["encryption"]
        
        print(f"Senha detectada: {password_length} caracteres hexadecimais")
        print(f"Você tem {attempts} tentativas para quebrar a senha.")
        print("Dica: Para cada posição correta, você verá um [O]")
        print("      Para cada caractere correto na posição errada, você verá um [X]")
        
        for attempt in range(1, attempts + 1):
            guess = input(f"\nTentativa {attempt}/{attempts}: ").upper()
            
            if len(guess) != password_length:
                print(f"A senha deve ter {password_length} caracteres!")
                continue
                
            if guess == password:
                print("\nSENHA CORRETA! Acesso concedido ao sistema.")
                self.reputation += target["difficulty"] * 10
                self.missions_completed += 1
                
                # Chance de melhorar habilidades
                skill = random.choice(list(self.skills.keys()))
                if random.random() < 0.3:  # 30% de chance
                    self.skills[skill] += 1
                    print(f"Você melhorou sua habilidade de {skill.replace('_', ' ')} para nível {self.skills[skill]}!")
                
                # Subir de nível
                if self.missions_completed >= self.level * 2:
                    self.level += 1
                    print(f"\nPARABÉNS! Você subiu para o nível {self.level}!")
                
                return
            
            # Feedback para o jogador
            feedback = ""
            temp_password = list(password)
            temp_guess = list(guess)
            
            # Primeiro, marque os caracteres corretos na posição correta
            for i in range(password_length):
                if temp_guess[i] == temp_password[i]:
                    feedback += "[O]"
                    temp_password[i] = "_"
                    temp_guess[i] = "*"
                else:
                    feedback += "[ ]"
            
            # Depois, marque os caracteres corretos na posição errada
            for i in range(password_length):
                if temp_guess[i] != "*":
                    if temp_guess[i] in temp_password:
                        idx = temp_password.index(temp_guess[i])
                        temp_password[idx] = "_"
                        feedback = feedback[:i] + "[X]" + feedback[i+3:]
            
            print(f"Resultado: {feedback}")
            
        print("\nNúmero máximo de tentativas excedido. Acesso negado.")
        print(f"A senha correta era: {password}")
        
        # Chance de ser detectado
        if random.random() < 0.2:  # 20% de chance
            print("\nALERTA! Sua atividade foi detectada pelo sistema de segurança!")
            print("Desconectando para evitar rastreamento...")
            self.disconnect()
            
    def show_status(self):
        print(f"\n=== STATUS DO HACKER ===")
        print(f"Nome: {self.username}")
        print(f"Nível: {self.level}")
        print(f"Reputação: {self.reputation}")
        print(f"Missões completadas: {self.missions_completed}")
        print(f"IP atual: {self.current_ip}")
        print(f"Status: {'Conectado' if self.connected else 'Desconectado'}")
        
    def show_skills(self):
        print("\n=== HABILIDADES ===")
        for skill, level in self.skills.items():
            print(f"{skill.replace('_', ' ').title()}: {level}")
            
    def upgrade_skill(self, skill):
        if skill not in self.skills:
            print(f"Habilidade '{skill}' não encontrada.")
            print(f"Habilidades disponíveis: {', '.join(self.skills.keys())}")
            return
            
        cost = self.skills[skill] * 50
        if self.reputation < cost:
            print(f"Reputação insuficiente. Você precisa de {cost} pontos.")
            return
            
        self.reputation -= cost
        self.skills[skill] += 1
        print(f"Habilidade {skill.replace('_', ' ')} melhorada para o nível {self.skills[skill]}!")
        
    def show_missions(self):
        print("\n=== MISSÕES DISPONÍVEIS ===")
        missions = [
            {"id": 1, "name": "Roubo de dados", "target": "Empresa local", "reward": 50, "difficulty": 1},
            {"id": 2, "name": "Quebra de firewall", "target": "Banco de dados público", "reward": 100, "difficulty": 2},
            {"id": 3, "name": "Implantação de backdoor", "target": "Servidor corporativo", "reward": 150, "difficulty": 3},
            {"id": 4, "name": "Interceptação de comunicações", "target": "Rede governamental", "reward": 200, "difficulty": 4},
            {"id": 5, "name": "Ataque de negação de serviço", "target": "Megacorporação", "reward": 250, "difficulty": 5}
        ]
        
        available_missions = [m for m in missions if m["difficulty"] <= self.level + 1]
        
        if not available_missions:
            print("Nenhuma missão disponível para o seu nível atual.")
            return
            
        for mission in available_missions:
            print(f"ID: {mission['id']} - {mission['name']}")
            print(f"   Alvo: {mission['target']}")
            print(f"   Recompensa: {mission['reward']} pontos de reputação")
            print(f"   Dificuldade: {mission['difficulty']}")
            print()
            
    def accept_mission(self, mission_id):
        missions = [
            {"id": 1, "name": "Roubo de dados", "target": "Empresa local", "reward": 50, "difficulty": 1},
            {"id": 2, "name": "Quebra de firewall", "target": "Banco de dados público", "reward": 100, "difficulty": 2},
            {"id": 3, "name": "Implantação de backdoor", "target": "Servidor corporativo", "reward": 150, "difficulty": 3},
            {"id": 4, "name": "Interceptação de comunicações", "target": "Rede governamental", "reward": 200, "difficulty": 4},
            {"id": 5, "name": "Ataque de negação de serviço", "target": "Megacorporação", "reward": 250, "difficulty": 5}
        ]
        
        mission = None
        for m in missions:
            if m["id"] == mission_id:
                mission = m
                break
                
        if not mission:
            print(f"Missão com ID {mission_id} não encontrada.")
            return
            
        if mission["difficulty"] > self.level + 1:
            print("Esta missão é muito difícil para o seu nível atual.")
            return
            
        print(f"\nAceitando missão: {mission['name']}")
        print(f"Alvo: {mission['target']}")
        print("Para completar esta missão, você precisa se conectar ao sistema alvo e quebrar a senha.")
        
        # Sugerir um alvo para a missão
        suggested_target = None
        for target in self.target_systems:
            if target["difficulty"] == mission["difficulty"]:
                suggested_target = target
                break
                
        if suggested_target:
            print(f"Sistema sugerido para esta missão: {suggested_target['name']} ({suggested_target['ip']})")
        
    def run(self):
        self.login()
        
        while True:
            self.show_banner()
            command = input(f"{self.username}@terminal:~$ ").strip().lower()
            
            if command == "exit":
                print("Saindo do Terminal Hacker. Até a próxima missão!")
                break
                
            elif command == "help":
                self.show_help()
                
            elif command == "scan":
                self.scan_network()
                
            elif command.startswith("connect "):
                ip = command.split(" ")[1]
                self.connect(ip)
                
            elif command == "disconnect":
                self.disconnect()
                
            elif command == "crack":
                self.crack_password()
                
            elif command == "status":
                self.show_status()
                
            elif command == "skills":
                self.show_skills()
                
            elif command.startswith("upgrade "):
                skill = command.split(" ")[1]
                self.upgrade_skill(skill)
                
            elif command == "missions":
                self.show_missions()
                
            elif command.startswith("accept "):
                try:
                    mission_id = int(command.split(" ")[1])
                    self.accept_mission(mission_id)
                except ValueError:
                    print("ID de missão inválido. Use um número.")
                    
            elif command == "clear":
                self.clear_screen()
                
            else:
                print(f"Comando '{command}' não reconhecido. Digite 'help' para ver os comandos disponíveis.")
                
            input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    game = TerminalHacker()
    game.run()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Terminal Nexus: Advanced Hacker Simulation
Um jogo de simulação hacker em modo texto
"""

import os
import sys
import time
import json
import random
import argparse
from getpass import getpass

# Importações dos módulos do jogo
from core.terminal import Terminal
from core.player import Player
from core.network import Network
from core.security import SecuritySystem
from world.entities import WorldEntities
from world.missions import MissionSystem
from world.economy import EconomySystem
from world.reputation import ReputationSystem
from utils.ascii_art import AsciiArt
from utils.colors import Colors
from utils.helpers import clear_screen, type_text, load_json_data

class TerminalNexus:
    """Classe principal do jogo Terminal Nexus"""
    
    VERSION = "1.0.0"
    
    def __init__(self, debug=False):
        """Inicializa o jogo"""
        self.debug = debug
        self.running = True
        self.logged_in = False
        self.first_run = True
        
        # Carrega dados do jogo
        self.load_game_data()
        
        # Inicializa componentes do jogo
        self.terminal = Terminal()
        self.player = Player()
        self.network = Network(self.systems_data)
        self.security = SecuritySystem()
        self.world_entities = WorldEntities(self.entities_data)
        self.mission_system = MissionSystem(self.missions_data)
        self.economy = EconomySystem()
        self.reputation = ReputationSystem()
        
        # Arte ASCII e cores
        self.ascii = AsciiArt()
        self.colors = Colors()
        
        # Estado do jogo
        self.current_system = None
        self.connected_to = None
        self.mission_active = False
        self.current_mission = None
        self.game_time = 0  # Tempo de jogo em minutos virtuais
        self.real_time_start = time.time()
        
        # Histórico de comandos
        self.command_history = []
        self.history_index = 0
        
        # Configurações
        self.config = {
            "typing_speed": 0.03,
            "show_tips": True,
            "difficulty": "normal",
            "auto_save": True,
            "theme": "matrix"
        }
        
        # Registra comandos disponíveis
        self.register_commands()
    
    def load_game_data(self):
        """Carrega todos os dados do jogo a partir dos arquivos JSON"""
        try:
            self.systems_data = load_json_data("data/systems.json")
            self.missions_data = load_json_data("data/missions.json")
            self.tools_data = load_json_data("data/tools.json")
            self.story_data = load_json_data("data/story.json")
            self.entities_data = load_json_data("data/entities.json")
        except Exception as e:
            print(f"Erro ao carregar dados do jogo: {e}")
            sys.exit(1)
    
    def register_commands(self):
        """Registra todos os comandos disponíveis no jogo"""
        self.commands = {
            # Comandos básicos
            "help": self.cmd_help,
            "exit": self.cmd_exit,
            "clear": self.cmd_clear,
            "status": self.cmd_status,
            "time": self.cmd_time,
            "config": self.cmd_config,
            
            # Comandos de rede
            "scan": self.cmd_scan,
            "connect": self.cmd_connect,
            "disconnect": self.cmd_disconnect,
            "ping": self.cmd_ping,
            "trace": self.cmd_trace,
            "netstat": self.cmd_netstat,
            
            # Comandos de sistema
            "ls": self.cmd_ls,
            "cd": self.cmd_cd,
            "cat": self.cmd_cat,
            "mkdir": self.cmd_mkdir,
            "rm": self.cmd_rm,
            "cp": self.cmd_cp,
            "mv": self.cmd_mv,
            "find": self.cmd_find,
            "grep": self.cmd_grep,
            "chmod": self.cmd_chmod,
            "whoami": self.cmd_whoami,
            
            # Comandos de hacking
            "crack": self.cmd_crack,
            "brute": self.cmd_brute,
            "exploit": self.cmd_exploit,
            "inject": self.cmd_inject,
            "sniff": self.cmd_sniff,
            "ddos": self.cmd_ddos,
            "backdoor": self.cmd_backdoor,
            "rootkit": self.cmd_rootkit,
            "ransomware": self.cmd_ransomware,
            "decrypt": self.cmd_decrypt,
            
            # Comandos de missão
            "missions": self.cmd_missions,
            "accept": self.cmd_accept,
            "abort": self.cmd_abort,
            "complete": self.cmd_complete,
            
            # Comandos de economia e inventário
            "buy": self.cmd_buy,
            "sell": self.cmd_sell,
            "market": self.cmd_market,
            "inventory": self.cmd_inventory,
            "use": self.cmd_use,
            "upgrade": self.cmd_upgrade,
            
            # Comandos sociais
            "message": self.cmd_message,
            "contacts": self.cmd_contacts,
            "reputation": self.cmd_reputation,
            "forum": self.cmd_forum,
            
            # Comandos avançados
            "analyze": self.cmd_analyze,
            "vpn": self.cmd_vpn,
            "proxy": self.cmd_proxy,
            "firewall": self.cmd_firewall,
            "log": self.cmd_log,
            "wipe": self.cmd_wipe,
            "compile": self.cmd_compile,
            "decompile": self.cmd_decompile,
            "script": self.cmd_script,
            
            # Comandos de jogo
            "save": self.cmd_save,
            "load": self.cmd_load,
            "tutorial": self.cmd_tutorial,
            "achievements": self.cmd_achievements,
            "stats": self.cmd_stats
        }
    
    def show_intro(self):
        """Mostra a introdução do jogo"""
        clear_screen()
        self.ascii.display("logo")
        print(f"\n{self.colors.CYAN}Terminal Nexus: Advanced Hacker Simulation v{self.VERSION}{self.colors.RESET}")
        print(f"{self.colors.GRAY}Desenvolvido por CodeGPT Labs{self.colors.RESET}")
        print("\n" + "="*80)
        
        if self.first_run:
            type_text("Iniciando sistema...", delay=0.05)
            time.sleep(0.5)
            type_text("Carregando módulos de segurança...", delay=0.05)
            time.sleep(0.5)
            type_text("Estabelecendo conexão com a darknet...", delay=0.05)
            time.sleep(0.5)
            type_text("Conexão estabelecida.", delay=0.05)
            time.sleep(1)
            self.first_run = False
    
    def login(self):
        """Gerencia o processo de login do jogador"""
        if self.logged_in:
            return True
            
        print("\n" + "="*50)
        print(f"{self.colors.GREEN}TERMINAL NEXUS - SISTEMA DE ACESSO SEGURO{self.colors.RESET}")
        print("="*50 + "\n")
        
        # Verifica se existe um save
        save_exists = os.path.exists("save.dat")
        
        if save_exists:
            choice = input("Save encontrado. Deseja carregar? (s/n): ").lower()
            if choice == 's':
                if self.cmd_load(None):
                    return True
        
        # Novo jogo
        while True:
            username = input("Login: ")
            if username.strip():
                break
            else:
                print("Nome de usuário inválido. Tente novamente.")
        
        password = getpass("Senha: ")
        
        print("\nAutenticando", end="")
        for _ in range(5):
            print(".", end="", flush=True)
            time.sleep(0.3)
        print("\n")
        
        type_text(f"Acesso concedido. Bem-vindo ao Terminal Nexus, {username}.")
        time.sleep(1)
        
        # Configuração inicial do jogador
        self.player.username = username
        self.player.password = password  # Na vida real, nunca armazene senhas em texto puro!
        self.player.init_new_player()
        
        # Tutorial para novos jogadores
        self.show_tutorial()
        
        self.logged_in = True
        return True
    
    def show_tutorial(self):
        """Mostra o tutorial para novos jogadores"""
        clear_screen()
        print(f"\n{self.colors.YELLOW}=== TUTORIAL DO TERMINAL NEXUS ==={self.colors.RESET}")
        
        tutorial_text = [
            "Bem-vindo ao mundo de Terminal Nexus, um simulador hacker avançado.",
            "Aqui você poderá explorar sistemas, completar missões e construir sua reputação no submundo digital.",
            "",
            "Comandos básicos para começar:",
            "  help       - Mostra a lista de comandos disponíveis",
            "  scan       - Escaneia a rede em busca de sistemas vulneráveis",
            "  connect IP - Conecta a um sistema remoto",
            "  missions   - Mostra as missões disponíveis",
            "",
            "Dicas importantes:",
            "• Comece com sistemas de baixa segurança para ganhar experiência",
            "• Complete missões para ganhar dinheiro e reputação",
            "• Compre e atualize ferramentas para enfrentar desafios mais difíceis",
            "• Use VPNs e proxies para ocultar sua identidade em sistemas de alta segurança",
            "• Mantenha backups de seus dados importantes",
            "",
            "Lembre-se: no mundo digital, conhecimento é poder."
        ]
        
        for line in tutorial_text:
            if line:
                type_text(line, delay=0.02)
            else:
                print()
        
        input("\nPressione ENTER para começar sua jornada...")
    
    def update_game_time(self):
        """Atualiza o tempo de jogo"""
        real_time_elapsed = time.time() - self.real_time_start
        # 1 minuto real = 10 minutos no jogo
        self.game_time += int(real_time_elapsed * 10)
        self.real_time_start = time.time()
        
        # Eventos baseados no tempo
        if self.game_time % 60 == 0:  # A cada hora no jogo
            self.process_hourly_events()
    
    def process_hourly_events(self):
        """Processa eventos que ocorrem a cada hora no jogo"""
        # Chance de eventos aleatórios
        if random.random() < 0.2:  # 20% de chance
            self.trigger_random_event()
        
        # Atualização de sistemas
        self.network.update_systems()
        
        # Atualização de missões
        self.mission_system.update_missions()
    
    def trigger_random_event(self):
        """Dispara um evento aleatório no jogo"""
        events = [
            {"name": "Ataque de hackers", "message": "Um grupo de hackers está atacando a rede. Segurança aumentada em todos os sistemas."},
            {"name": "Falha de segurança", "message": "Uma falha de segurança foi descoberta em sistemas corporativos. Oportunidade para exploração."},
            {"name": "Blackout", "message": "Um blackout afetou parte da rede. Alguns sistemas estão temporariamente inacessíveis."},
            {"name": "Atualização de firewall", "message": "Grandes corporações atualizaram seus firewalls. Exploits antigos podem não funcionar."},
            {"name": "Vazamento de dados", "message": "Um vazamento de dados expôs informações sensíveis. Novas oportunidades no mercado negro."}
        ]
        
        event = random.choice(events)
        print(f"\n{self.colors.YELLOW}[EVENTO] {event['name']}: {event['message']}{self.colors.RESET}")
    
    def process_command(self, command_line):
        """Processa um comando inserido pelo usuário"""
        if not command_line.strip():
            return
            
        # Adiciona ao histórico
        self.command_history.append(command_line)
        if len(self.command_history) > 100:
            self.command_history.pop(0)
        self.history_index = len(self.command_history)
        
        # Divide o comando e argumentos
        parts = command_line.split()
        command = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else None
        
        # Executa o comando
        if command in self.commands:
            try:
                self.commands[command](args)
            except Exception as e:
                if self.debug:
                    print(f"{self.colors.RED}Erro ao executar comando: {e}{self.colors.RESET}")
                    import traceback
                    traceback.print_exc()
                else:
                    print(f"{self.colors.RED}Erro ao executar comando. Use 'help {command}' para mais informações.{self.colors.RESET}")
        else:
            print(f"{self.colors.RED}Comando '{command}' não reconhecido. Digite 'help' para ver os comandos disponíveis.{self.colors.RESET}")
    
    def run(self):
        """Loop principal do jogo"""
        self.show_intro()
        
        if not self.login():
            return
        
        while self.running:
            self.update_game_time()
            
            # Mostra o prompt
            if self.connected_to:
                system_name = self.network.get_system_name(self.connected_to)
                prompt = f"{self.colors.GREEN}{self.player.username}@{system_name}{self.colors.RESET}:{self.colors.BLUE}~{self.colors.RESET}$ "
            else:
                prompt = f"{self.colors.GREEN}{self.player.username}@localhost{self.colors.RESET}:{self.colors.BLUE}~{self.colors.RESET}$ "
            
            try:
                command = input(prompt)
                self.process_command(command)
            except KeyboardInterrupt:
                print("\nUse 'exit' para sair do jogo.")
            except EOFError:
                print("\nUse 'exit' para sair do jogo.")
    
    # Implementação dos comandos
    def cmd_help(self, args):
        """Mostra a ajuda do jogo"""
        if not args:
            categories = {
                "Básicos": ["help", "exit", "clear", "status", "time", "config"],
                "Rede": ["scan", "connect", "disconnect", "ping", "trace", "netstat"],
                "Sistema": ["ls", "cd", "cat", "mkdir", "rm", "cp", "mv", "find", "grep", "chmod", "whoami"],
                "Hacking": ["crack", "brute", "exploit", "inject", "sniff", "ddos", "backdoor", "rootkit", "ransomware", "decrypt"],
                "Missões": ["missions", "accept", "abort", "complete"],
                "Economia": ["buy", "sell", "market", "inventory", "use", "upgrade"],
                "Social": ["message", "contacts", "reputation", "forum"],
                "Avançados": ["analyze", "vpn", "proxy", "firewall", "log", "wipe", "compile", "decompile", "script"],
                "Jogo": ["save", "load", "tutorial", "achievements", "stats"]
            }
            
            print(f"\n{self.colors.YELLOW}=== COMANDOS DISPONÍVEIS ==={self.colors.RESET}")
            for category, cmds in categories.items():
                print(f"\n{self.colors.CYAN}{category}:{self.colors.RESET}")
                # Imprime em colunas
                col_width = 15
                num_cols = 5
                for i in range(0, len(cmds), num_cols):
                    row = cmds[i:i+num_cols]
                    print("  " + "".join(f"{cmd:<{col_width}}" for cmd in row))
            
            print(f"\nDigite '{self.colors.YELLOW}help <comando>{self.colors.RESET}' para informações detalhadas sobre um comando específico.")
        else:
            cmd = args[0].lower()
            if cmd in self.commands:
                doc = self.commands[cmd].__doc__ or "Sem documentação disponível."
                print(f"\n{self.colors.YELLOW}Ajuda: {cmd}{self.colors.RESET}")
                print(doc)
            else:
                print(f"{self.colors.RED}Comando '{cmd}' não encontrado.{self.colors.RESET}")
    
    def cmd_exit(self, args):
        """Sai do jogo"""
        if self.config["auto_save"]:
            print("Salvando jogo automaticamente...")
            self.cmd_save(None)
        
        confirm = input("Tem certeza que deseja sair? (s/n): ").lower()
        if confirm == 's':
            print("Saindo do Terminal Nexus. Até a próxima missão!")
            self.running = False
    
    def cmd_clear(self, args):
        """Limpa a tela do terminal"""
        clear_screen()
    
    def cmd_status(self, args):
        """Mostra o status atual do jogador"""
        print(f"\n{self.colors.YELLOW}=== STATUS DO HACKER ==={self.colors.RESET}")
        print(f"Nome: {self.player.username}")
        print(f"Nível: {self.player.level}")
        print(f"Experiência: {self.player.xp}/{self.player.xp_to_next_level}")
        print(f"Reputação: {self.player.reputation}")
        print(f"Dinheiro: ${self.player.money}")
        print(f"Missões completadas: {self.player.missions_completed}")
        print(f"IP atual: {self.player.current_ip}")
        print(f"Status: {'Conectado a ' + self.connected_to if self.connected_to else 'Desconectado'}")
        
        print(f"\n{self.colors.CYAN}Habilidades:{self.colors.RESET}")
        for skill, level in self.player.skills.items():
            print(f"  {skill.replace('_', ' ').title()}: {level}")
        
        if self.connected_to:
            system = self.network.get_system(self.connected_to)
            print(f"\n{self.colors.CYAN}Sistema conectado:{self.colors.RESET}")
            print(f"  Nome: {system['name']}")
            print(f"  Tipo: {system['type']}")
            print(f"  Segurança: {system['security']}/10")
            print(f"  Status: {'Comprometido' if system.get('compromised', False) else 'Seguro'}")
    
    def cmd_time(self, args):
        """Mostra o tempo atual do jogo"""
        hours = self.game_time // 60
        minutes = self.game_time % 60
        days = hours // 24
        hours_of_day = hours % 24
        
        print(f"\n{self.colors.YELLOW}Tempo de jogo:{self.colors.RESET}")
        print(f"Dia {days+1}, {hours_of_day:02d}:{minutes:02d}")
        
        # Eventos programados
        upcoming_events = [
            {"day": days+1, "time": "18:00", "event": "Atualização de segurança em sistemas corporativos"},
            {"day": days+2, "time": "03:00", "event": "Manutenção da rede governamental"},
            {"day": days+3, "time": "12:00", "event": "Leilão no mercado negro"}
        ]
        
        print(f"\n{self.colors.CYAN}Próximos eventos:{self.colors.RESET}")
        for event in upcoming_events:
            print(f"  Dia {event['day']}, {event['time']} - {event['event']}")
    
    def cmd_config(self, args):
        """Configura opções do jogo"""
        if not args:
            print(f"\n{self.colors.YELLOW}=== CONFIGURAÇÕES ==={self.colors.RESET}")
            for key, value in self.config.items():
                print(f"{key}: {value}")
            print("\nUso: config <opção> <valor>")
            return
        
        if len(args) == 1:
            option = args[0]
            if option in self.config:
                print(f"{option}: {self.config[option]}")
            else:
                print(f"{self.colors.RED}Opção '{option}' não encontrada.{self.colors.RESET}")
            return
        
        option, value = args[0], args[1]
        if option in self.config:
            # Converte o valor para o tipo apropriado
            if isinstance(self.config[option], bool):
                value = value.lower() in ('true', 'yes', 'y', '1')
            elif isinstance(self.config[option], int):
                try:
                    value = int(value)
                except ValueError:
                    print(f"{self.colors.RED}Valor inválido para {option}.{self.colors.RESET}")
                    return
            elif isinstance(self.config[option], float):
                try:
                    value = float(value)
                except ValueError:
                    print(f"{self.colors.RED}Valor inválido para {option}.{self.colors.RESET}")
                    return
            
            self.config[option] = value
            print(f"Configuração atualizada: {option} = {value}")
        else:
            print(f"{self.colors.RED}Opção '{option}' não encontrada.{self.colors.RESET}")
    
    def cmd_scan(self, args):
        """Escaneia a rede em busca de sistemas vulneráveis"""
        print("\nEscaneando rede em busca de sistemas vulneráveis...")
        progress = 0
        while progress < 100:
            progress += random.randint(5, 15)
            progress = min(progress, 100)
            sys.stdout.write(f"\rProgresso: [{progress*'#':{100}s}] {progress}%")
            sys.stdout.flush()
            time.sleep(0.1)
        print("\n")
        
        # Filtra sistemas baseado no nível do jogador
        available_systems = self.network.get_available_systems(self.player.level)
        
        if not available_systems:
            print("Nenhum sistema encontrado na sua faixa de habilidade.")
            return
        
        print(f"{self.colors.YELLOW}Sistemas encontrados:{self.colors.RESET}")
        for i, system in enumerate(available_systems):
            security_color = self.colors.GREEN if system["security"] <= 3 else (
                self.colors.YELLOW if system["security"] <= 6 else self.colors.RED)
            
            status = "Comprometido" if system.get("compromised", False) else "Seguro"
            status_color = self.colors.GREEN if status == "Comprometido" else self.colors.RED
            
            print(f"{i+1}. {system['name']} ({system['ip']})")
            print(f"   Tipo: {system['type']}, Segurança: {security_color}{system['security']}/10{self.colors.RESET}")
            print(f"   Status: {status_color}{status}{self.colors.RESET}")
            if "description" in system:
                print(f"   {system['description']}")
            print()
    
    def cmd_connect(self, args):
        """Conecta a um sistema remoto"""
        if not args:
            print("Uso: connect <ip>")
            return
            
        ip = args[0]
        system = self.network.get_system(ip)
        
        if not system:
            print(f"{self.colors.RED}Erro: IP {ip} não encontrado na rede.{self.colors.RESET}")
            return
            
        print(f"\nTentando conectar a {system['name']} ({ip})...")
        for i in range(5):
            dots = "." * (i % 4)
            sys.stdout.write(f"\rEstabelecendo conexão{dots:4}")
            sys.stdout.flush()
            time.sleep(0.3)
            
        # Calcula chance de sucesso baseada nas habilidades do jogador e segurança do sistema
        success_chance = min(90, 40 + (self.player.skills["networking"] * 10) - (system["security"] * 8))
        
        # Modificadores
        if self.player.active_vpn:
            success_chance += 15
            print(f"\n{self.colors.CYAN}[VPN ativa] Chance de conexão aumentada.{self.colors.RESET}")
        
        if system.get("compromised", False):
            success_chance += 30
            print(f"\n{self.colors.GREEN}[Sistema comprometido] Acesso facilitado.{self.colors.RESET}")
        
        if random.randint(1, 100) <= success_chance:
            print(f"\n{self.colors.GREEN}Conexão estabelecida com {system['name']}!{self.colors.RESET}")
            self.connected_to = ip
            
            # Atualiza o sistema de arquivos atual
            self.current_system = system
            
            # Chance de ganhar XP
            if random.random() < 0.3:  # 30% de chance
                xp_gained = system["security"] * 5
                self.player.add_xp(xp_gained)
                print(f"{self.colors.CYAN}+{xp_gained} XP{self.colors.RESET}")
        else:
            print(f"\n{self.colors.RED}Falha na conexão. Firewall bloqueou o acesso.{self.colors.RESET}")
            
            # Chance de ser detectado
            if random.random() < 0.2 and system["security"] > 5:  # 20% de chance em sistemas de alta segurança
                print(f"\n{self.colors.RED}ALERTA! Sua tentativa de conexão foi registrada pelo sistema de segurança!{self.colors.RESET}")
                self.player.add_heat(system["security"])
    
    def cmd_disconnect(self, args):
        """Desconecta do sistema atual"""
        if not self.connected_to:
            print("Você não está conectado a nenhum sistema.")
            return
            
        print("Desconectando", end="")
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.3)
        print()
        
        system_name = self.network.get_system_name(self.connected_to)
        self.connected_to = None
        self.current_system = None
        print(f"{self.colors.GREEN}Desconectado com sucesso de {system_name}.{self.colors.RESET}")
        print("Retornando ao seu sistema local.")
    
    def cmd_ping(self, args):
        """Verifica a conectividade com um host"""
        if not args:
            print("Uso: ping <ip>")
            return
            
        ip = args[0]
        system = self.network.get_system(ip)
        
        if not system:
            print(f"{self.colors.RED}Erro: IP {ip} não encontrado na rede.{self.colors.RESET}")
            return
            
        print(f"Enviando pacotes ICMP para {ip}...")
        
        # Simula latência baseada na "distância" do sistema
        latencies = []
        for i in range(4):
            latency = random.uniform(20, 200)
            latencies.append(latency)
            print(f"64 bytes de {ip}: icmp_seq={i+1} ttl=64 tempo={latency:.2f} ms")
            time.sleep(0.5)
            
        avg_latency = sum(latencies) / len(latencies)
        print(f"\n--- Estatísticas de ping para {ip} ---")
        print(f"4 pacotes transmitidos, 4 recebidos, 0% de perda de pacotes")
        print(f"RTT min/avg/max = {min(latencies):.2f}/{avg_latency:.2f}/{max(latencies):.2f} ms")
        print(f"{self.colors.GREEN}Conexão estabelecida.{self.colors.RESET}")
        print("Retornando ao seu sistema local.")

    def cmd_exit(self, args):
        """Sai do terminal"""
        print("Saindo do terminal...")
        time.sleep(1)
        print("Até a próxima!")
        sys.exit(0)

    def cmd_help(self, args):
        """Mostra a lista de comandos disponíveis"""
        print("Comandos disponíveis:")
        for command in self.commands:
            print(f"  {command}")
            if hasattr(self, f"cmd_{command}"):
                method = getattr(self, f"cmd_{command}")
                if method.__doc__:
                    print(f"    {method.__doc__}")
        print(f"  {self.colors.GREEN}help <comando>{self.colors.RESET} - Mostra ajuda detalhada sobre um comando específico.")
        print(f"  {self.colors.GREEN}exit{self.colors.RESET} - Sai do terminal.")
        print(f"  {self.colors.GREEN}clear{self.colors.RESET} - Limpa a tela.")
        print(f"  {self.colors.GREEN}config{self.colors.RESET} - Mostra as configurações atuais.")
        print(f"  {self.colors.GREEN}config <opção> <valor>{self.colors.RESET} - Altera uma configuração.")
        print(f"  {self.colors.GREEN}config reset{self.colors.RESET} - Reseta todas as configurações para os valores padrão.")
        print(f"  {self.colors.GREEN}config save{self.colors.RESET} - Salva as configurações atuais em um arquivo.")
        print(f"  {self.colors.GREEN}config load{self.colors.RESET} - Carrega as configurações de um arquivo.")
        print(f"  {self.colors.GREEN}config list{self.colors.RESET} - Lista todas as configurações disponíveis.")
        print(f"  {self.colors.GREEN}config help{self.colors.RESET} - Mostra ajuda detalhada sobre as configurações.")
        print(f"  {self.colors.GREEN}config exit{self.colors.RESET} - Sai do terminal.")
        print(f"  {self.colors.GREEN}config clear{self.colors.RESET} - Limpa a tela.")
    
    def cmd_config(self, args):
        """Mostra as configurações atuais"""
        if not args:
            print("Configurações atuais:")
            for key, value in self.config.items():
                print(f"  {key}: {value}")
            return
        
        if args[0] == "reset":
            self.config = self.default_config
            print("Configurações resetadas para os valores padrão.")
            return
        
        if args[0] == "save":
            with open("config.txt", "w") as f:
                for key, value in self.config.items():
                    f.write(f"{key}={value}\n")
            print("Configurações salvas em config.txt.")
            return
        
        if args[0] == "load":
            with open("config.txt", "r") as f:
                for line in f:
                    key, value = line.strip().split("=")
                    self.config[key] = value
            print("Configurações carregadas de config.txt.")
            return
        
        if args[0] == "list":
            print("Configurações disponíveis:")
            for key in self.config.keys():
                print(f"  {key}")
            return
        
        if args[0] == "help":
            print("Ajuda sobre as configurações:")
            for key, value in self.config.items():
                print(f"  {key}: {value}")
            return
        
        if args[0] == "exit":
            sys.exit(0)
        
        if args[0] == "clear":
            self.clear_screen()
            return
        
        if len(args) < 2:
            print("Uso: config <opção> <valor>")
            return
        
        option = args[0]
        value = args[1]
        self.config[option] = value
        print(f"Configuração {option} definida como {value}.")

    def cmd_clear(self, args):
        """Limpa a tela"""
        self.clear_screen()
        print("Tela limpa.")
