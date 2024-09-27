string = input('Digite um número: ')

try:
    string = int(string)
except:
    string = -1


if string > 0:
    print('Nice work')
else:
    print('Not a number')
