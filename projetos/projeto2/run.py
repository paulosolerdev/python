#!/usr/bin/env python3
import os
import sys
import subprocess

def check_requirements():
    """Verifica se todas as dependências estão instaladas."""
    try:
        import tkinter
        import pyperclip
        import pygments
        import requests
        return True
    except ImportError as e:
        print(f"Dependência faltando: {e}")
        print("Instalando dependências...")
        subprocess.call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        return
