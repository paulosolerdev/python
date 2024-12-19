# # # Conjuntos (set)

# # s1 = set('Paulo')
# # print(s1)

# s1 = {'Paulo', 1, 2, 2, 2, 2, 3, 3, 3}
# print(s1)

# Métodos úteis:
# add, update, clear, discard
# s1 = set()
# s1.add('Paulo')
# s1.add(1)
# s1.update(('Olá mundo', 1, 2, 3, 4))
# print(s1)

# #s1.clear()
# s1.discard('Olá mundo')
# print(s1)

s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1 | s2
print(s3)

s3 = s1 & s2
print(s3)

s3 = s1 - s2
print(s3)

s3 = s2 - s1
print(s3)

s3 = s1 ^ s2
print(s3)
