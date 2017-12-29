'''
Módulo de controle da Inteligencia Artificial dos mobs.
'''
from random import randint

def Grunt (player, inimigo):
    comando = input('<!> Vez de {}.\n...\nPressione Enter para continuar.\n'.format(inimigo['Nome']))
    inimigo['ATK']['ataque']['ATK'](inimigo, player)

def Monstro(player, inimigo):
    pass

def General(player, inimigo):
    pass

def Chefe(player, inimigo):
    pass
