'''
Módulo de controle da Inteligencia Artificial dos npcs.
'''
from random import randint

def Grunt (player, inimigo):
    comando = input('<!> Vez de {}.\n...\nPressione Enter para continuar.\n'.format(inimigo['Nome']))
    inimigo['ATK']['ataque']['ATK'](inimigo, player)

def Monstro(player, inimigo):
    comando = input('<!> Vez de {}.\n...\nPressione Enter para continuar.\n'.format(inimigo['Nome']))
    if not inimigo['PV'] <= inimigo['R']:
        inimigo['ATK']['ataque']['ATK'](inimigo, player)
    else:
        inimigo['AKT']['habilidade']['ATK'](inimigo, player)

def General(player, inimigo):
    pass

def Chefe(player, inimigo):
    pass
