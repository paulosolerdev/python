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

# print(f'Before')

# for value in [9, 41, 12, 3, 74, 15]:
#     if value > 20:
#         print(f'Large number {value}')
# print(f'After')


#=============================================#



# found = False
# print(f'Before {found}')
# for value in [9, 41, 12, 3, 74, 15]:
#     if value == 3:
#         found = True
#     print(f'{found} {value}')
# print(f'After {found}')


#=============================================#



# largest_so_far = -1

# print(f'Before {largest_so_far}')

# for the_num in [9, 41, 12, 3, 74, 15]:
#     if the_num > largest_so_far:
#         largest_so_far = the_num
#     print(f'{largest_so_far} {the_num}')

# print(f'After {largest_so_far}')

#=============================================#


smallest = None

print(f'Before {smallest}')

for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(f'{smallest} {value}')

print(f'After {smallest}')
