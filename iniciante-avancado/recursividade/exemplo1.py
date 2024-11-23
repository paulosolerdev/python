def fatorial(num: int) -> int:
    if num == 1:
        return 1
    

    return num * fatorial(num - 1)


fator = fatorial(9)

print(fator)
