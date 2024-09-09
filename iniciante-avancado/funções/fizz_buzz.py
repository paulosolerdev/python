def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return f'FizzBuzz, {num} é divisível por 3 e por 5.'
    if num % 5 == 0:
        return f'Buzz, {num} é dividível por 5.'
    if num % 3 == 0:
        return f'Fizz, {num} é divisível por 3.'
    
    return num

print(fizz_buzz(num=int(input('Digite um número: '))))
