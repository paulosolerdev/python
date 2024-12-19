import re


# minha_string = 'Paulo chegará à meia-noite.'

# print(re.findall(r'Paul.', minha_string))

# texto1 = '''No dia trinta de março de dois mil e vinte
# foi inaugurado o novo ginásio de esportes da escola estadual 
# Professor Annes Dias, na cidade de Cruz Alta, no estado do
# Rio Grande do Sul. A obra inicialmente orçada em um milhão 
# de reais acabou não utilizando de todo o recurso, uma vez
# que dois grandes empresários da cidade, João Fagundes e 
# Maria Terres doaram juntos em torno de duzentos mil reais.
# João Fagundes se manifestou dizendo que apoiou a obra pois
# acredita no desenvolvimento da cidade, assim investe 
# regularmante para hospitais e escolas da mesma. Maria Terres
# não quis se pronunciar sobre o assunto.'''

# print(re.sub(r'jOãO', 'Carlos', texto1, flags=re.I))


# minha_string = 'Paulo chegará à meia-noite.'

# print(re.match(r'Paulo', minha_string))
# print(re.match(r'noite', minha_string))


minha_string2 = 'Paulo chegará, a meia noite.'

print(re.split(r',', minha_string2))
