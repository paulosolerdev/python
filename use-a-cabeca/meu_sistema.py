"""
    Exibe informações do meu Sistema Operacional.
"""

import sys
import os

print(f"Este é o meu sistema operacional: {sys.platform.title()}") # Sistema Operacional

print(f"Esta é a versão do meu Python: {sys.version.title()}")  # Versão do Python

print(f"Esta é minha localização: {os.getcwd()}")

# Variáveis de ambiente em conjunto
print(f"{os.environ}")

# Variáveis de ambiente individualmente (especificamente)
print(f"{os.getenv('HOME')}")

