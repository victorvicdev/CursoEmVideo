n1 = int(input('Digite o valor: '))
n2 = int(input('Digite o valor: '))
s = n1 + n2
# print('A soma entre ', n1,' e ', n2, ' vale: ', s)
print('A soma entre {} e {} vale {}'.format(n1, n2, s))
print('O número', s, ' é inteiro?', s.is_integer())