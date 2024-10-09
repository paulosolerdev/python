# fhand = open('arquivo-texto.txt')

# print(fhand)

#=====================================#

# xfile = open('arquivo-texto.txt')
# for cheese in xfile:
#     print(cheese)


#=====================================#



# fhand = open('arquivo-texto.txt')
# count = 0
# for line in fhand:
#     count = count + 1
# print(f'Line Count: {count}')


#=====================================#


# fhand = open('arquivo-texto.txt')
# inp = fhand.read()
# print(len(inp))

# print(inp[:101])


#=====================================#


fhand = open('arquivo-texto.txt')

for line in fhand:
    if line.startswith('From:'):
        print(line)
