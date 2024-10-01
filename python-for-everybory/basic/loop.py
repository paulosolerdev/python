# zork = 0

# print(f'Before {zork}')

# for thing in [9, 41, 12, 3, 75, 15]:
#     zork = zork + 1
#     print(f'{zork} \t->\t {thing}')
# print(f'After {zork}')


#=============================================#


# zork = 0
# print(f'Before {zork}')
# for thing in [9, 41, 12, 3, 74, 15]:
#     zork += thing
#     print(f'{zork} \t->\t {thing}')
# print(f'After {zork}')

#=============================================#



# count = 0
# sum = 0
# print(f'Before -> Contador = {count} e Soma = {sum}')
# for value in [9, 41, 12, 3, 74, 15]:
#     count = count + 1
#     sum = sum + value
#     print(f'{count} {sum} {value}')
# print(f'After -> Contador = {count} e Soma = {sum}, Soma/Contador = {sum/count:.2f}')


#=============================================#



# Filtering in a Loop

print(f'Before')

for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print(f'Large number {value}')
print(f'After')
