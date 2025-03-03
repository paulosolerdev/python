import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog
import socket
import threading
import json
import os
import re
import pyperclip
from datetime import datetime
import requests
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import Terminal256Formatter

class DevChat:
    def __init__(self, root):
        self.root = root
        self.root.title("DevChat - Mensageiro para Programadores")
        self.root.geometry("900x700")
        self.root.configure(bg="#1e1e1e")  # Tema escuro como IDEs
        
        self.username = ""
        self.server_socket = None
        self.client_socket = None
        self.connected = False
        
        self.setup_ui()
        
    def setup_ui(self):
        # Estilo
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TButton", background="#0078d7", foreground="white", font=('Consolas', 10))
        style.configure("TFrame", background="#1e1e1e")
        style.configure("TLabel", background="#1e1e1e", foreground="#ffffff", font=('Consolas', 10))
        
        # Frame principal
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Área de chat
        self.chat_area = scrolledtext.ScrolledText(main_frame, bg="#252526", fg="#d4d4d4", 
                                                  font=('Consolas', 10), wrap=tk.WORD)
        self.chat_area.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.chat_area.config(state=tk.DISABLED)
        
        # Frame de entrada
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Área de entrada de mensagem
        self.message_entry = scrolledtext.ScrolledText(input_frame, height=3, bg="#2d2d30", 
                                                      fg="#d4d4d4", font=('Consolas', 10))
        self.message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.message_entry.bind("<Control-Return>", self.send_message)
        
        # Botões
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.send_button = ttk.Button(buttons_frame, text="Enviar (Ctrl+Enter)", command=self.send_message)
        self.send_button.pack(side=tk.LEFT, padx=2)
        
        self.code_button = ttk.Button(buttons_frame, text="Formatar Código", command=self.format_code)
        self.code_button.pack(side=tk.LEFT, padx=2)
        
        self.snippet_button = ttk.Button(buttons_frame, text="Salvar Snippet", command=self.save_snippet)
        self.snippet_button.pack(side=tk.LEFT, padx=2)
        
        self.search_button = ttk.Button(buttons_frame, text="Pesquisar Stack Overflow", command=self.search_stackoverflow)
        self.search_button.pack(side=tk.LEFT, padx=2)
        
        # Barra lateral de ferramentas
        tools_frame = ttk.Frame(self.root, width=200)
        tools_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=5, pady=10)
        
        ttk.Label(tools_frame, text="Ferramentas do Desenvolvedor").pack(pady=5)
        
        ttk.Button(tools_frame, text="Compartilhar Arquivo", command=self.share_file).pack(fill=tk.X, pady=2)
        ttk.Button(tools_frame, text="Gerar Documentação", command=self.generate_docs).pack(fill=tk.X, pady=2)
        ttk.Button(tools_frame, text="Executar Código", command=self.run_code).pack(fill=tk.X, pady=2)
        ttk.Button(tools_frame, text="Debugger Colaborativo", command=self.collaborative_debug).pack(fill=tk.X, pady=2)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Desconectado")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Iniciar login
        self.show_login_dialog()
    
    def show_login_dialog(self):
        login_window = tk.Toplevel(self.root)
        login_window.title("DevChat - Login")
        login_window.geometry("300x150")
        login_window.configure(bg="#1e1e1e")
        login_window.transient(self.root)
        login_window.grab_set()
        
        ttk.Label(login_window, text="Nome de usuário:").pack(pady=10)
        
        username_entry = ttk.Entry(login_window, width=30)
        username_entry.pack(pady=5)
        username_entry.focus()
        
        def do_login():
            self.username = username_entry.get()
            if self.username:
                self.status_var.set(f"Conectado como: {self.username}")
                login_window.destroy()
                self.connect_to_server()
            
        ttk.Button(login_window, text="Entrar", command=do_login).pack(pady=10)
        
    def connect_to_server(self):
        # Simulação de conexão - em um app real, aqui seria a conexão com um servidor
        self.connected = True
        self.display_message("Sistema", "Conectado ao servidor DevChat!")
        self.display_message("Sistema", "Bem-vindo ao DevChat, o mensageiro para desenvolvedores!")
        self.display_message("Sistema", "Dica: Use ```python seu_codigo``` para formatar código Python")
    
    def send_message(self, event=None):
        message = self.message_entry.get("1.0", tk.END).strip()
        if message and self.connected:
            self.display_message(self.username, message)
            self.message_entry.delete("1.0", tk.END)
            
            # Detectar e formatar código automaticamente
            if re.search(r'```(\w+)?\n', message):
                self.format_code_in_message(message)
        
        return "break"  # Impede a inserção de nova linha com Ctrl+Enter
    
    def display_message(self, sender, message):
        self.chat_area.config(state=tk.NORMAL)
        timestamp = datetime.now().strftime("%H:%M")
        
        # Formatar mensagem
        self.chat_area.insert(tk.END, f"[{timestamp}] ", "timestamp")
        self.chat_area.insert(tk.END, f"{sender}: ", "sender")
        
        # Verificar se há código para formatar
        code_blocks = re.findall(r'```(\w+)?\n(.*?)```', message, re.DOTALL)
        if code_blocks:
            remaining_text = message
            for lang, code in code_blocks:
                # Encontrar a posição do bloco de código
                start_marker = f"```{lang}\n"
                end_marker = "```"
                start_pos = remaining_text.find(start_marker)
                
                # Inserir texto antes do bloco de código
                if start_pos > 0:
                    pre_text = remaining_text[:start_pos]
                    self.chat_area.insert(tk.END, pre_text)
                
                # Inserir o bloco de código formatado
                self.chat_area.insert(tk.END, "\n--- Código ")
                if lang:
                    self.chat_area.insert(tk.END, f"{lang} ")
                self.chat_area.insert(tk.END, "---\n", "code-header")
                self.chat_area.insert(tk.END, code, "code")
                self.chat_area.insert(tk.END, "\n-----------\n", "code-header")
                
                # Atualizar o texto restante
                end_pos = remaining_text.find(end_marker, start_pos) + len(end_marker)
                remaining_text = remaining_text[end_pos:]
            
            # Inserir qualquer texto restante após o último bloco de código
            if remaining_text:
                self.chat_area.insert(tk.END, remaining_text)
        else:
            self.chat_area.insert(tk.END, message)
        
        self.chat_area.insert(tk.END, "\n\n")
        self.chat_area.see(tk.END)
        self.chat_area.config(state=tk.DISABLED)
        
        # Configurar tags para estilização
        self.chat_area.tag_configure("timestamp", foreground="#888888")
        self.chat_area.tag_configure("sender", foreground="#0078d7", font=('Consolas', 10, 'bold'))
        self.chat_area.tag_configure("code", background="#2d2d30", foreground="#569cd6", 
                                    font=('Consolas', 9))
        self.chat_area.tag_configure("code-header", foreground="#888888", font=('Consolas', 8))
    
    def format_code(self):
        code = self.message_entry.get("1.0", tk.END).strip()
        if code:
            # Detectar linguagem ou assumir Python
            language = "python"  # Padrão
            
            # Formatar o código
            formatted_code = f"```{language}\n{code}\n```"
            
            # Substituir no campo de entrada
            self.message_entry.delete("1.0", tk.END)
            self.message_entry.insert("1.0", formatted_code)
    
    def format_code_in_message(self, message):
        # Esta função seria responsável por destacar a sintaxe do código
        # Em uma implementação real, usaria bibliotecas como Pygments
        pass
    
    def save_snippet(self):
        code = self.message_entry.get("1.0", tk.END).strip()
        if code:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".py",
                filetypes=[("Python files", "*.py"), ("All files", "*.*")]
            )
            if file_path:
                with open(file_path, "w") as file:
                    file.write(code)
                self.display_message("Sistema", f"Snippet salvo em {file_path}")
    
    def search_stackoverflow(self):
        query = self.message_entry.get("1.0", tk.END).strip()
        if query:
            # Em uma implementação real, faria uma chamada à API do Stack Overflow
            search_url = f"https://stackoverflow.com/search?q={query.replace(' ', '+')}"
            self.display_message("Sistema", f"Pesquisando no Stack Overflow: {search_url}")
            # Abrir navegador com a pesquisa
            # import webbrowser
            # webbrowser.open(search_url)
    
    def share_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            file_name = os.path.basename(file_path)
            with open(file_path, 'r') as file:
                try:
                    content = file.read()
                    # Detectar linguagem pelo nome do arquivo
                    extension = os.path.splitext(file_name)[1][1:]
                    if extension in ['py', 'js', 'java', 'c', 'cpp', 'cs', 'html', 'css', 'php']:
                        language = extension
                    else:
                        language = ""
                    
                    # Formatar e enviar
                    formatted_content = f"Arquivo compartilhado: {file_name}\n```{language}\n{content}\n```"
                    self.message_entry.delete("1.0", tk.END)
                    self.message_entry.insert("1.0", formatted_content)
                except:
                    self.display_message("Sistema", f"Erro ao ler o arquivo {file_name}")
    
    def generate_docs(self):
        code = self.message_entry.get("1.0", tk.END).strip()
        if code:
            # Em uma implementação real, usaria uma biblioteca para gerar documentação
            self.display_message("Sistema", "Funcionalidade de geração de documentação em desenvolvimento.")
    
    def run_code(self):
        code = self.message_entry.get("1.0", tk.END).strip()
        if code:
            # Em uma implementação real, executaria o código em um ambiente seguro
            self.display_message("Sistema", "Funcionalidade de execução de código em desenvolvimento.")
    
    def collaborative_debug(self):
        # Em uma implementação real, iniciaria uma sessão de depuração colaborativa
        self.display_message("Sistema", "Funcionalidade de depuração colaborativa em desenvolvimento.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DevChat(root)
    root.mainloop()
