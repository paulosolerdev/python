def find_average(nums):
    # Verifica se a lista não está vazia
    if len(nums) == 0:
        return 0  # Evita divisão por zero
    
    # Soma os números e divide pela quantidade
    return sum(nums) / len(nums)

# Exemplo de uso
lista = [1, 3, 5, 7]
media = find_average(lista)
print("A média é:", media)
