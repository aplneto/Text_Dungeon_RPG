'''
Módulo de controle da Inteligencia Artificial dos npcs.
'''
from random import randint

def Grunt (player, inimigo):
    comando = input('<!> Vez de {}.\n...\nPressione Enter para continuar.\n'.format(inimigo['Nome']))
    inimigo['ATK']['ataque']['ATK'](inimigo, player)

def Monstro(player, inimigo):
    comando = input('<!> Vez de {}.\n...\nPressione Enter para continuar.\n'.format(inimigo['Nome']))
    act = randint(1,6)
    if (act <= 2) and (inimigo['PM'] >= inimigo['ATK']['poder']['PM']):
        inimigo['PM'] -= inimigo['ATK']['poder']['PM']
        inimigo['ATK']['poder']['ATK'](inimigo, player)
    elif (inimigo['PM'] >= inimigo['ATK']['poder']['PM']) and (inimigo['PV'] <= inimigo['R']):
        inimigo['PM'] -= inimigo['ATK']['poder']['PM']
        inimigo['ATK']['poder']['ATK'](inimigo, player)
    else:
        inimigo['ATK']['ataque']['ATK'](inimigo, player)

def General(player, inimigo):
    comando = input('<!> Vez de {}.\n...\nPressione Enter para continuar.\n'.format(inimigo['Nome']))
    if (player['PV'] >= (player['MAX'][0]//2)) and (inimigo['PM'] >= 2*(inimigo['ATK']['especial']['PM'])):
        if inimigo['PM'] >= 15 and inimigo['PV'] >= 8:
            inimigo['ATK']['poder']['ATK'](inimigo, player)
        elif inimigo['Status'] != 'Armadura':
            inimigo['ATK']['proteção']['ATK'](inimigo)
        else:
            inimigo['ATK']['especial']['ATK'](inimigo, player)
    elif (player['PV'] < (player['MAX'][0]//2)) and (inimigo['PM'] >= inimigo['ATK']['poder']['PM']):
        if inimigo['PM'] >= inimigo['ATK']['especial']['PM']:
            inimigo['ATK']['especial']['ATK'](inimigo, player)
        else:
            inimigo['ATK']['poder']['ATK'](inimigo, player)
    elif (inimigo['Status'] != 'Armadura') and (inimigo['PM'] >= inimigo['ATK']['proteção']['PM']):
        inimigo['ATK']['proteção']['ATK'](inimigo)
    elif (player['PV'] <= player['R']):
        if inimigo['PM'] >= inimigo['ATK']['especial']['PM']:
            inimigo['ATK']['especial']['ATK'](inimigo, player)
        elif inimigo['PM'] >= inimigo['ATK']['poder']['PM']:
            inimigo['ATK']['poder']['ATK'](inimigo, player)
        else:
            print('{} junta as mãos e começa a sussurrar palavras mágicas. É possivel ver energia mágica se acumulando ao seu redor.'.format(inimigo['Nome']))
            dado = randint(1,6)
            inimigo['PM'] += dado
    else:
        inimigo['ATK']['ataque']['ATK'](inimigo, player)
