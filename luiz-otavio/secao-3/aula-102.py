import re
import sys


# Limpeza e validação inicial do CPF
entrada = input('Digite o CPF: ')
cpf_usuario = re.sub(r'[^0-9]', '', entrada)  # Remove tudo que não é número

entrada_e_sequencial = entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

# Verifica se o CPF possui 11 dígitos
if len(cpf_usuario) != 11:
    print("CPF inválido: deve conter 11 dígitos.")
    exit()

# Cálculo do primeiro dígito verificador
nove_digitos = cpf_usuario[:9]
contador_regressivo_1 = 10
resultado_digito_1 = 0

for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

# Cálculo do segundo dígito verificador
dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11
resultado_digito_2 = 0

for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

# Montagem do CPF gerado
cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

# Validação final
if cpf_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_usuario} é válido.')
else:
    print(f'{cpf_usuario} é inválido.')
