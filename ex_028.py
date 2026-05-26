from random import randint
from time import sleep
pc = randint(0, 5) # Faz o pc pensar num n°.
print('--=--' * 11)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('--=--' * 11)
jogador = int(input('Em que número eu pensei?')) #Jogador tenta adivinhar.
print('PROCESSANDO...')
sleep(2)
if jogador == pc:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no n° {} e não no {}!'.format(pc, jogador))
