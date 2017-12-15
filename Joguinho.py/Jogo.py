'''
Joguinho em 3D&T Alpha para praticar o uso de dicionários de Python.

12-15-2017
00:06

Bem-vindo ao desafio de Valkaria, um RPG no cenário de Tormenta onde você enfrenta hordas de inimigos em um calabouço, em busca do Desbravador, a arma mágica da Deusa.

Opções:
CONTINUAR --> O personagem segue para enfrentar o próximo inimigo, escolhido aleatoriamente dentre um determinado número de inimigos.
SALVAR --> Salva o estado do jogador e o número de inimigos derrotados.
DESISTIR --> Salva um arquivo de Score contendo a pontuação do jogador.

Personagens:
GUERREIRO --> Força 3, Habilidade 2, Resistência 3, Armadura 2, Poder de Fogo 0, Pontos de Vida 15, Pontos de Magia 15
MAGO --> Força 1, Habilidade 3, Resistência 2, Armadura 0, Poder de Fogo 0, Pontos de Vida 10, Pontos de Magia 30
PALADINO --> Força 2, Habilidade 3, Resistência 3, Armadura 2, Poder de Fogo 0, Pontos de Vida 15, Pontos de Magia 15
ARQUEIRO --> Força 0, Habilidade 2, Resistência 2, Armadura 1, Poder de Fogo 3, Pontos de Vida 10, Pontos de Magia 10

Os personagens podem usar as seguintes ações.
GUERREIRO --> Machado; Ataque especial (2 PMs)
MAGO --> Cajado; Arpão (15 PMs), Bola de Fogo (5 PMs), O Crânio Voador de Vladislav (3 PMs)
PALADINO --> Espada; Cura mágica (1 PM), Ataque Especial (1 PM)
ARQUEIRO --> Arco; Tiro Preciso, Perigoso e Poderoso (4 PMs)

Já os inimigos são:
'''
from random import randint

def Main():
    '''
    Função principal do jogo.
    '''
    PLAYER = {'Nome': 'jogador', 'F':0, 'H':0, 'R':0, 'A':0, 'PdF':0, 'PV':1, 'PM':1, 'ATK':{}, 'Status':'Normal', 'dano': ''}
    rolar = lambda: randint(1,6)
    
    def MenuClasse():
        nonlocal PLAYER
        while True:
            comando = input('Ver(v/ver), Escolher(e/escolher).\n').lower()
            while comando.startswith('v'):
                print ('Estão disponíveis as seguintes classes:')
                classe = input('Arqueiro(a/arqueiro), Guerreiro (g/guerreiro), Mago(m/mago), Paladino (p/paladino), voltar(v/voltar).\n').lower()
                if classe.startswith('a'):
                    print ('Um antigo ditado diz que um arqueiro carrega um número de vidas em sua aljava, tamanha é a sua precisão.\n\
Conhecidos por serem silenciosos e mortais, os arqueiros geralmente são notados apenas quando a flecha atinge o alvo.')
                    print ('Você terá Força 0, Habilidade 2, Resistência 2, Armadura 1, Poder de Fogo 3\n\
10 PVs, 10 PMs e pode atacar com seu arco.\n\
Além disso, você pode realizar um poderoso disparo que tem mais chances de causar dano crítico e que,\n\
quando o faz, causa mais dano que os ataques normais ao custo de (4 PMs)')
                elif classe.startswith('g'):
                    print('Vindo diretamente das arenas de gladiadores, você parte pelo mundo em busca\n\
de provar que é o melhor guerreiro de toda Arton, e que nada poderá superar sua habilidade com a Espada')
                    print('Você terá Força 3, Habilidade 2, Resistência 3, Armadura 2, Poder de Fogo 0\n\
15 PVs, 15 PMs e além de poder atacar com seu machado, poderá também usar um poderoso golpe que causa dano crítico\n\
muaior.')
                elif classe.startswith('m'):
                    print('Armado de um grande cajado e de um extenso grimório, você tem como objetivo provar\n\
que é capaz de dominar a magia em todos os seus aspectos.')
                    print('você terá Força 1, Habilidade 3, Resistência 2, Armadura 0  e Poder de Fogo 0\n\
10 PVs, 30 PMs e será capaz de atacar com seu cajado, além das seguintes magias:\n\
Arpão (15 PMs): uma poderosa onda sônica de energia mágica capaz de obliterar um inimigo:\n\
Bola de fogo (6 PMs): uma bola de fogo que explode em uma área, atingindo até três inimigos;\n\
O Crânio Voador de Vladislav (3 PMs): um crânio mágico que explode contra um alvo, ignorando sua Armadura.')
                elif classe.startswith('p'):
                    pass
                else:
                    break
            while comando.startswith('e'):
                classe = input ('Escolha sua classe: Arqueiro(a/arqueiro), Guerreiro(g/guerreiro), Mago(m/mago), Paladino (p/paladino), Voltar(v/voltar)').lower()
                if classe.startswith('g'):
                    PLAYER['F'] = 3
                    PLAYER['H'] = 2
                    PLAYER['R'] = 3
                    PLAYER['A'] = 2
                    PLAYER['PV'] = 15
                    PLAYER['PM'] = 15
                    PLAYER['dano'] = 'seu machado'
                    PLAYER['ATK'] = {'Machado':{'ATK':Atacar, 'PM': 0}}  # DEPOIS DE FINALIZAR OS ATAQUES, VOLTAR AQUI
                    return
                elif classe.startswith('m'):
                    PLAYER['F'] = 1
                    PLAYER['H'] = 3
                    PLAYER['R'] = 2
                    PLAYER['A'] = 0
                    PLAYER['PV'] = 10
                    PLAYER['PM'] = 30
                    PLAYER['dano'] = 'seu cajado'
                    PLAYER['ATK'] = {'Arpão':{'ATK':Arpao, 'PM':15},'Cajado': {'ATK':Atacar, 'PM': 0}, 'Bola de Fogo': {'ATK': BolaDeFogo, 'PM': 5}}  # DEPOIS DE FINALIZAR OS ATAQUES, VOLTAR AQUI
                    return
                elif classe.startswith('a'):
                    PLAYER['H'] = 2
                    PLAYER['R'] = 2
                    PLAYER['A'] = 1
                    PLAYER['PdF'] = 3
                    PLAYER['PV'] = 10
                    PLAYER['PM'] = 10
                    PLAYER['dano'] = 'seu arco'
                    PLAYER['ATK'] = {'Arco':{'ATK':Disparar, 'PM':0}, 'Golpe Fatal':{'ATK':TiroCerteiro, 'PM':4}}  # DEPOIS DE FINALIZAR OS ATAQUES, VOLTAR AQUI
                    return
                elif classe.startswith('p'):
                    PLAYER['F'] = 2
                    PLAYER['H'] = 3
                    PLAYER['R'] = 3
                    PLAYER['A'] = 2
                    PLAYER['PV']= 15
                    PLAYER['PM'] = 15
                    PLAYER['dano'] = 'sua espada'
                    PLAYER['ATK'] = {'Espada':{'ATK':Atacar, 'PM':0}}

    def Atacar(atacante, vitima):
        '''
        Função definida para os ataques fisicos simples, feitos com F.
        '''
        nonlocal rolar
        msg = '{} ataca {} com {}'.format(atacante['Nome'], vitima['Nome'], atacante['dano'])
        dado = rolar()
        ataque = atacante['F']+atacante['H']+dado
        if dado == 6 and (atacante['F'] > 0):
            ataque+=atacante['F']
        dado = rolar()
        defesa = vitima['A'] + vitima['H']+dado
        if dado == 6 and (vitima['A'] > 0):
            defesa +=vitima['A']
        dano = ataque-defesa
        if dano<=0:
            msg += ', mas seu ataque falha.'
        elif dado == 1:
            msg += 'que é atingido em cheio, recebendo {} pontos de dano.'.format(dano)
            vitima['PV'] -= dano
        else:
            msg += ' e causa {} pontos de dano.'.format(dano)
            vitima['PV'] -= dano
        print(msg)
        
    def Disparar(atacante, vitima):
        '''
        Função definida para os ataques físicos a distância, feitos com PdF.
        '''
        nonlocal rolar
        msg = '{} dispara {} contra {}'.format(atacante['Nome'], atacante['dano'], vitima['Nome'])
        dado = rolar()
        ataque = atacante['PdF']+atacante['H']+dado
        if dado == 6 and (atacante['F'] > 0):
            ataque+=atacante['PdF']
        dado = rolar()
        defesa = vitima['A'] + vitima['H']+dado
        if dado == 6 and (vitima['A'] > 0):
            defesa +=vitima['A']
        dano = ataque-defesa
        if dano<=0:
            msg += ', mas erra o disparo.'
        elif dado == 1:
            msg += 'que é atingido em cheio, recebendo {} pontos de dano.'.format(dano)
            vitima['PV'] -= dano
        else:
            msg += ' e causa {} pontos de dano.'.format(dano)
            vitima['PV'] -= dano
        print(msg)

    def TiroCerteiro(atacante, vitima):
        '''
        Função definida para o tiro certeiro da classe arqueiro.
        '''
        nonlocal rolar
        dado = rolar()
        atacante['PM'] -= 4
        ataque = atacante['H'] + atacante['PdF'] + dado
        if dado >= 5:
            ataque += 2*atacante['PdF']
        msg = '{} concentra suas energias em {} antes de realizar o disparo fatal.'.format(atacante['Nome'], atacante['dano'])
        print(msg)
        dado = rolar()
        defesa = vitima['H'] + vitima['PdF'] + dado
        dano = ataque - defesa
        if dano <= 0:
            msg = 'No entanto, {} consegue proteger-se do disparo, fazendo {} errar seu alvo.'.format(vitima['Nome'], atacante['Nome'])
        elif dado == 1:
            msg = '{} é atingido em cheio pelo disparo que atravessa seu corpo, causando {} pontos de dano.'.format(vitima['Nome'], dano)
        else:
            msg = '{} é atingo pelo disparo sofrento {} pontos de dano.'.format(vitima['Nome'], dano)
        dano = max(dano, 0)
        vitima['PV'] -= dano
        print(msg)

    def Arpao (atacante, vitima):
        '''
        Função definida para o uso da magia Arpão
        '''
        nonlocal rolar
        atacante['PM'] -= 15
        msg = '{} junta uma grande quantidade de energia mágica em suas mãos e, com o sussurrar\n\
                de algumas palavras mágicas, disparando de suas mãos uma onda roxa na forma de um arpão.'.format(atacante['Nome'])
        print(msg)
        ataque = atacante['H']
        for i in range (6):
            ataque += rolar()
        dado = rolar()
        defesa = vitima['H']+vitima['A']+dado
        dano = ataque-defesa
        if dano <= 0:
            msg = 'Milagrosamente, {} consegue desviar do arpão mágico, saindo ileso do golpe.'.format(vitima['Nome'])
        elif dado == 1:
            msg = '{} é atingido em cheio pelo ataque, sendo arremessado para longe pelo impacto e sofrento {} pontos de dano.'.format(vitima['Nome'], dano)
        else:
            msg = '{} é atingo pelo disparo, sofrendo queimaduras mágicas por todo o corpo e recebendo {} pontos de dano.'.format(vitima['Nome'], dano)
        dano = max(dano, 0)
        vitima['PV'] -= dano
        
    def BolaDeFogo(atacante, *vitimas):
        '''
        Função definida para o uso da magia Bola de Fogo.
        '''
        nonlocal rolar
        ataque = atacante['H']+5+rolar()
        atacante['PM'] -= 5
        msg1 = '{} sussurra algumas palavras mágicas e extende as mãos em direção'.format(atacante['Nome'])
        if len(vitimas) == 1:
            msg1 += ' ao inimigo e de suas mãos uma grande bola de fogo é disparada.'
        else:
            msg1 += 'ao inimigo e de suas mãos uma grande bola de fogo é disparada.'
        print(msg1)
        for alvo in vitimas:
            dado = rolar()
            defesa = vitima['H']+vitima['A']+dado
            if (dado == 6) and (vitima['A']>0):
                defesa += vitima['A']
            dano = ataque-defesa
            if dano<=0:
                msg2 = '{} consegue defender-se da bola de fogo, saindo ileso do ataque.'.format(vitima['Nome'])
                print(msg2)
            elif dado == 1:
                msg = 'A bola de fogo atinge {} em cheio, causando {} ponto de dano.'.format(vitima['Nome'], dano)
                print(msg2)
                vitima['PV'] -= dano
            else:
                msg = 'A bola de fogo explode próxima a {}, causando-lhe {} pontos de dano.'.format(vitima['Nome'], dano)
                print(msg2)
                vitima['PV'] -= dano

    def CranioVoador(atacante, vitima):
        '''
        Função definida para a magia O Crânio Voador de Vladislav.
        '''
        nonlocal rolar
        ataque = atacante['H']+rolar()+rolar()
        atacante['PM'] -= 3
        msg = '{} dispara de suas mãos um horrendo crânio de energia mágica, que voa na direção de seu alvo.'.format(atacante['Nome'])
        print(msg)
        defesa = vitima['H']+rolar()
        dano = ataque-defesa
        if dano <= 0:
            msg = 'O crânio erra o alvo e {} sai ileso do ataque.'.format(vitima['Nome'])
        else:
            msg = '{} é atingido pelo crânio voador, que causa queimaduras mágicas pelo seu corpo.'.format(vitima['Nome'])
            vitima['PV'] -= dano
        print(msg)
