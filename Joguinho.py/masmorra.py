'''
Código de controle dos sistema de combate, encontros, dano, etc...
'''
from random import randint

d6 = lambda:randint(1,6)

fim_de_jogo = False
vilao = False

def Combate (player, inimigos):
    global fim_de_jogo
    comando = input('Cálculo de iniciativa.\nPressione enter para continuar.\n')
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

    def verificardano ():
        nonlocal player
        nonlocal inimigos
        if player['PV'] <= 0:
            player['Morte'](player)
        aux = 0
        for npc in inimigos:
            if npc['PV'] <= 0:
                player['score'] += npc['score']
                print(npc['Morte'])
                del(inimigos[aux])
            aux += 1
    
    ordem = ordenariniciativa([player]+inimigos)
    for personagem in ordem:
        print('{}:{}'.format(personagem['Nome'], personagem['Iniciativa']))
    while True:
        if player['PV'] <= 0:
            fim_de_jogo = True
            return
        else:
            vez = 0
            for personagem in ordem:
                if personagem['PV'] > 0 and personagem == player:
                    player['Ação'](player, inimigos)
                elif personagem['PV'] > 0:
                    personagem['AI'](player, personagem)
                verificardano()
                vez += 1
            if len(inimigos) == 0:
                print('')  # Mensagem de Vitória da Sala
                return
        
def ActPlayer(player, inimigos):
    '''
    Função de controle das ações do jogador.
    '''
    print('...')
    print('PV: {}, PM: {}'.format(player['PV'], player['PM']))
    print ('Chegou a sua vez. O que deseja fazer?\n(Em caso de duvidas utilize o comando "Ajuda")\n')
    while True:
        comando = input()
        if comando in player['ATK']:
            if comando.lower() == 'ajuda':
                player['ATK']['Ajuda']['ATK']()
            elif player['ATK'][comando]['PM'] <= player['PM']:
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
            inimigos = []
            print ('Escolha o alvo primário:')
            aux = 1
            for inimigo in lista_inimigos:
                print ('({}) {}({} PV)'.format(aux, inimigo['Nome'], inimigo['PV']))
                aux += 1
            index = int(input())
            if (index < 0) or (index>aux):
                print('Não entendi sua escolha. Tente novamente.')
                continue
            else:
                inimigos.append(lista_inimigos[index-1])
                for inimigo in lista_inimigos:
                    if not (inimigo in inimigos):
                        inimigos.append(inimigo)
                return inimigos
    elif comando == 'Cura Mágica':
        return []
    else:
        while True:
            print ('Quem você vai atacar?')
            aux = 1
            for inimigo in lista_inimigos:
                print ('({}) {}({} PV)'.format(aux, inimigo['Nome'], inimigo['PV']))
                aux += 1
            index = int(input())
            if (index < 0) or index>aux:
                print('Não entendi sua escolha. Tente novamente.')
                continue
            else:
                alvo = lista_inimigos[index-1]
                return alvo
            
def GameOver(player):
    global fim_de_jogo
    fim_de_jogo = True
    print('Sua pontuação foi de {} Pontos.'.format(player['score']))
