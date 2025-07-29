#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo comutador. O programa deverá escrever na tela se o usuário perdeu ou venceu.
'''import random
numero_computador = random.randint(0, 5)
numero_usuario = int(input('Digite o número que você acha que o computador pensou entre 0 e 5: '))
if numero_usuario == numero_computador:
    print('Certa resposta!!!')
else:
    print(f'Você errou!!! O numero correto era {numero_computador}.')''' #esse foi o que eu fiz

#programa criado pelo Professor Guanabara
from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador "pensar"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!')
print('-=-' * 20) #imprime o que está entre aspas 20 vezes
jogador = int(input('Em que número eu pensei? ')) #pergunta para o jogador adivinhar
print('PROCESSANDO...') #comando para o sleep
sleep(3) #faz o computador dormir pelos segundos que você escolher
if jogador == computador:
    print('PARABÉNS! Você conseguiu vencer!')
else:
    print(f'GANHEI! Eu pensei em {computador} e não em {jogador}')
