data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2015'
print(f'Data -> {data}')

atpos = data.find('@')
print(f'atpos -> {atpos}')

sppos = data.find(' ', atpos)
print(f'sppos -> {sppos}')

host = data[atpos+1 : sppos]
print(host)
