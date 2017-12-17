'''
Código de controle dos sistema de combate, encontros, dano, etc...
'''
from random import randint

d6 = lambda:randint(1,6)

score = 0
fim_de_jogo = False

def Combate (player, inimigos):
    global fim_de_jogo
    global score
    comando = input('Cálculo de iniciativa.\n')
    player['Iniciativa'] = player['H'] + d6()
    for inimigo in inimigos:
        inimigo['Iniciativa'] = inimigo['H']+d6()

    def ordenariniciativa (lista):
        if len(lista) == 1:
            return lista
        else:
            maior = lista[0]
            index = 0
            aux = 0
            for personagem in lista:
                if personagem['Iniciativa'] > maior['Iniciativa']:
                    maior = personagem
                    index = aux
                elif (personagem['Iniciativa'] == maior['Iniciativa']) and (personagem['H'] > maior['H']):
                    maior = personagem
                    index = aux
                aux += 1
            maior = lista.pop(index)
            return [maior]+ordenariniciativa(lista)

    ordem = ordenariniciativa([player]+inimigos)
    for personagem in ordem:
        print('{}:{}'.format(personagem['Nome'], personagem['Iniciativa']))
    while True:
        if player['PV'] <= 0:
            fim_de_jogo = True
            break
        else:
            vez = 0
            for personagem in ordem:
                if personagem['PV'] > 0 and personagem == player:
                    player['Ação'](player, inimigos)
                    VerificarDano(ordem)
                elif personagem['PV'] > 0:
                    personagem['AI'](player, personagem)
                    VerificarDano(ordem)
                else:
                    score += ordem.pop(vez)['score']
                    print(personagem['Morte'])
                vez += 1
        
def ActPlayer(player, inimigos):
    '''
    Função de controle das ações do jogador.
    '''
    print('...')
    print ('Chegou a sua vez. O que deseja fazer?\n')
    while True:
        comando = input()
        if comando in player['ATK']:
            if AcaoValida(player, comando):
                inimigo = SelecionarInimigo(comando, inimigos)
                player['ATK'][comando]['ATK'](player, inimigo)
                return
            else:
                print('Você nao possui PMs suficientes para isso.')
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
