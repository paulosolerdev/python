

# Função para converter o texto para código Morse
# def texto_para_morse(texto):
#     texto = texto.upper()  # Converter para maiúsculas para combinar com o dicionário
#     morse_code = " ".join(morse_dict[char] for char in texto if char in morse_dict)
#     return morse_code

def texto_para_morse(texto):
    # Dicionário de caracteres em Código Morse
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
        'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
        '9': '----.', '0': '-----', ' ': '/'
    }

    return ''.join(morse_dict[i] for i in texto.upper())


# Entrada do usuário
texto = input("Digite o texto para converter em código Morse: ")
conversor = texto_para_morse(texto)
print(f"{texto} em Código Morse:", conversor)
