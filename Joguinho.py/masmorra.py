'''
Código de controle dos sistema de combate, encontros, dano, etc...
'''
from random import randint
d6 = lambda:randint(1,6)

def Turno(personagens):
    '''
    Função para o cálculo da iniciativa no início de um combate
    '''
    if len(personagens) == 1:
        personagens[0]['Ação']()
    else:
        turno = personagens
        maior = 0
        vez = None
        for personagem in turno:
            personagem['Iniciativa'] = personagem['H']+d6
            if personagem ['Iniciativa'] > maior:
                maior = personagem['Iniciativa']
                vez = personagem
        vez['Ação']()
        return Turno(personagens.__delitem__(vez))

def ActPlayer(player, inimigos):
    '''
    Função de controle das ações do jogador.
    '''
    print ('Chegou a sua vez. O que deseja fazer?\n')
    while True:
        comando = input()
        if comando in player['ATK']:
            if AcaoValida(player, comando):
                inimigo = SelecionarInimigo(comando, inimigos)
                player['ATK'][comando]['ATK'](player, inimigo)
            else:
                print('Você nao possui PMs suficientes para isso.')
                continue
        else:
            print ('Não entendi. Tende novamente.')

def AcaoValida (player, acao):
    '''
    Função que verifica se o Player tem PM suficiente para usar seu comando.
    '''
    return player['ATK'][acao]['PM'] <= player['PM']

def SelecionarInimigo (comando, lista_inimigos):
    '''
    Função definida para a selação de inimigos.
    '''
    if comando == 'Bola de Fogo':
        while True:
            print ('Quem você vai atacar?')
            aux = 1
            for inimigo in lista_inimigos:
                print ('({}) {}'.format(aux, inimigo['Nome']))
                aux += 1
            index = int(input())
            if (select < 0) or select>aux:
                print('Não entendi sua escolha. Tente novamente.')
                continue
            else:
                inimigos = (lista_inimigos[index-1], lista_inimigos[index], lista_inimigos[index-2])
                return inimigos
    else:
        while True:
            print ('Quem você vai atacar?')
            aux = 1
            for inimigo in lista_inimigos:
                print ('({}) {}'.format(aux, inimigo['Nome']))
                aux += 1
            index = int(input())
            if (select < 0) or select>aux:
                print('Não entendi sua escolha. Tente novamente.')
                continue
            else:
                alvo = lista_inimigos[index-1]
                return alvo
    
