'''
Joguinho em 3D&T Alpha para praticar o uso de dicionários de Python.

12-15-2017
00:06

Bem-vindo a masmorra de treinos do Protetorado do Reino, um RPG no cenário de Tormenta onde você enfrenta hordas de inimigos em um calabouço, em busca do Desbravador, a arma mágica da Deusa.

Opções:
CONTINUAR --> O personagem segue para enfrentar o próximo inimigo, escolhido aleatoriamente dentre um determinado número de inimigos.
SALVAR --> Salva o estado do jogador e o número de inimigos derrotados.
DESISTIR --> Salva um arquivo de Score contendo a pontuação do jogador.

Personagens:
GUERREIRO --> Força 3, Habilidade 2, Resistência 3, Armadura 2, Poder de Fogo 0, Pontos de Vida 20, Pontos de Magia 10
MAGO --> Força 1, Habilidade 3, Resistência 2, Armadura 1, Poder de Fogo 0, Pontos de Vida 10, Pontos de Magia 30
PALADINO --> Força 2, Habilidade 2, Resistência 3, Armadura 2, Poder de Fogo 0, Pontos de Vida 15, Pontos de Magia 15
ARQUEIRO --> Força 1, Habilidade 2, Resistência 2, Armadura 1, Poder de Fogo 3, Pontos de Vida 10, Pontos de Magia 10

Os personagens podem usar as seguintes ações.
GUERREIRO --> Machado; Ataque especial perigoso e poderoso (3 PMs)
MAGO --> Cajado; Arpão (15 PMs), Bola de Fogo (5 PMs), O Crânio Voador de Vladislav (3 PMs)
PALADINO --> Espada; Ataque Vorpal (3 PMs), Cura Mágica (2 PMs), Esconjuro (5 PMs)
ARQUEIRO --> Faca, Arco; Tiro Preciso, Perigoso e Poderoso (4 PMs)

Já os inimigos são:
'''
from random import randint
from masmorra import *
from dummies import *

def Main():
    '''
    Função principal do jogo.
    '''
    global fim_de_jogo
    PLAYER = {'Nome': 'jogador', 'F':0, 'H':0, 'R':0, 'A':0, 'PdF':0, 'PV':1, 'PM':1, 'PE':0, 'ATK':{}, 'Status':'Normal', 'dano': '', 'Ação':ActPlayer, 'Tipo': 'Humano', 'score':0}
    PLAYER['Morte'] = GameOver
    rolar = lambda: randint(1,6)
    testar = (lambda x: rolar() <= x)
    
    def MenuClasse():
        nonlocal PLAYER
        while True:
            print('...')
            comando = input('Arqueiro(a/arqueiro), Guerreiro(g/guerreiro), Mago(m/mago), Paladino(p/paladino).\n...\n').lower()
            print('...')
            if comando.startswith('a'):
                print ('<Arkam Braço Metálico> -- Um antigo ditado diz que um arqueiro carrega um número de vidas em sua aljava, tamanha é a sua precisão.\n'
                       '<Arkam Braço Metálico> Conhecidos por serem silenciosos e mortais, um bom arqueiro só é notado depois que sua fleche atinge seu alvo.')
                print ('<!> Você terá Força 0, Habilidade 2, Resistência 2, Armadura 1, Poder de Fogo 3\n'
                       '<!> 10 PVs, 10 PMs e pode atacar com seu arco.\n'
                       '<!> Além disso, você pode realizar um poderoso disparo que tem mais chances de causar dano crítico e que, quando o faz, causa mais dano que os ataques normais ao custo de 4 PMs.')
                print ('...')
                comando = input('Confirmar (c/confirmar), voltar(v/voltar)\n').lower()
                if comando.startswith('c'):
                    PLAYER['F'] = 1
                    PLAYER['H'] = 2
                    PLAYER['R'] = 2
                    PLAYER['A'] = 1
                    PLAYER['PdF'] = 3
                    PLAYER['PV'] = 10
                    PLAYER['PM'] = 10
                    PLAYER['MAX'] = (10, 10)
                    PLAYER['dano'] = 'seu arco'
                    PLAYER['ATK'] = {'Arco':{'ATK':Disparar, 'PM':0}, 'Faca':{'ATK':Atacar, 'PM':0},'Golpe Fatal':{'ATK':TiroCerteiro, 'PM':4}}
                    PLAYER['classe'] = 1
                    break
                elif comando.startswith('v'):
                    continue
                else:
                    print('...')
                    print('<Arkam Braço Metálico> -- Não entendi. Pode repetir?')
            elif comando.startswith('g'):
                print('<Arkam Braço Metálico> -- Os guerreiros costumam ser a alma de um grupo de aventureiros.\n'
                      '<Arkam Braço Metálico> A força e bravura de um guerreiro pode ser a diferença entre encontrar um tesouro ou ir para ao encontro dos deuses.')
                print('<!> Você terá Força 3, Habilidade 2, Resistência 3, Armadura 2, Poder de Fogo 0\n'
                      '<!> 20 PVs, 10 PMs e usará um machado.\n'
                      '<!> Além disso, você poderá também usar um poderoso golpe que causa muito mais dano por 3 PMs.')
                print('...')
                comando = input('Confirmar (c/confirmar), voltar(v/voltar)\n').lower()
                if comando.startswith('c'):
                    PLAYER['F'] = 3
                    PLAYER['H'] = 2
                    PLAYER['R'] = 3
                    PLAYER['A'] = 2
                    PLAYER['PV'] = 20
                    PLAYER['PM'] = 10
                    PLAYER['MAX'] = (20, 10)
                    PLAYER['dano'] = 'seu machado'
                    PLAYER['ATK'] = {'Machado':{'ATK':Atacar, 'PM': 0}, 'Golpe Demolidor':{}}
                    PLAYER['classe'] = 2
                    break
                elif comando.startswith('v'):
                    continue
                else:
                    print('...')
                    print('<Arkam Braço Metálico> -- Não entendi. Pode repetir?')
            elif comando.startswith('m'):
                print('<Arkam Braço Metálico> -- Em todo lugar de Arton, grandes histórias são contadas sobre magos e seus poderes.'
                      '<Arkam Braço Metálico> -- Com certeza ser um mago requer inteligencia e é uma tarefa difícil... mas nao sei se a masmorra é um bom lugar pra você.')
                print('<!> Você terá Força 1, Habilidade 3, Resistência 2, Armadura 0  e Poder de Fogo 0\n'
                      '<!> 10 PVs, 30 PMs e será capaz de atacar com seu cajado, além das seguintes magias:\n'
                      '<!> Arpão (15 PMs): uma poderosa onda sônica de energia mágica capaz de obliterar um inimigo:\n'
                      '<!> Bola de fogo (6 PMs): uma bola de fogo que explode em uma área, atingindo até três inimigos;\n'
                      '<!> O Crânio Voador de Vladislav (3 PMs): um crânio mágico que explode contra um alvo, ignorando sua Armadura.')
                print('...')
                comando = input('Confirmar (c/confirmar), voltar(v/voltar)\n').lower()
                if comando.startswith('c'):
                    PLAYER['F'] = 1
                    PLAYER['H'] = 3
                    PLAYER['R'] = 2
                    PLAYER['A'] = 1
                    PLAYER['PV'] = 10
                    PLAYER['PM'] = 30
                    PLAYER['MAX'] = (10, 30)
                    PLAYER['dano'] = 'seu cajado'
                    PLAYER['ATK'] = {'Arpão':{'ATK':Arpao, 'PM':15},'Cajado': {'ATK':Atacar, 'PM': 0}, 'Bola de Fogo': {'ATK': BolaDeFogo, 'PM': 5}}
                    PLAYER['classe'] = 3
                    break
                elif comando.startswith('v'):
                    continue
                else:
                    print('...')
                    print('<Arkam Braço Metálico> -- Não entendi. Pode repetir?')
            elif comando.startswith('p'):
                print('<Arkam Braço Metálico> -- Os deuses escolheram você para cumprir uma missão divina em Arton.\n'
                      '<Arkam Braço Metálico> -- Mas será que suas orações serão suficientes para fazê-lo vencer esse desafio? É o que vamos descobrir.')
                print('<!> Você terá Força 2, Habilidade 2, Resistência 3, Armadura 2, Poder de Fogo 0\n'
                      '<!> 15 PVs, 15 PMs e poderá usar sua Espada para ataques simples. Além disso, terá a sua disposição as seguintes magias:\n'
                      '<!> Ataque Vorpal (3 PMs): um poderoso ataque que, em caso de acerto crítico, pode decapitar um inimigo.\n'
                      '<!> Cura mágica (2 PMs): você recupera entre 1 e 6 PVs próprios.\n'
                      '<!> Esconjuro (5 PMs): pode ser usada apenas contra mortos-vivos. Caso tenha sucesso, sua magia bane o alvo, destruindo de uma so vez.')
                print('...')
                comando = input('Confirmar (c/confirmar), voltar(v/voltar)\n').lower()
                if comando.startswith('c'):
                    PLAYER['F'] = 2
                    PLAYER['H'] = 2
                    PLAYER['R'] = 3
                    PLAYER['A'] = 2
                    PLAYER['PV'] = 15
                    PLAYER['PM'] = 15
                    PLAYER['MAX'] = (15, 15)
                    PLAYER['dano'] = 'sua espada'
                    PLAYER['ATK'] = {'Espada':{'ATK':Atacar, 'PM':0}, 'Cura Mágica':{'ATK':CuraMagica, 'PM':2}, 'Esconjuro':{'ATK': Esconjuro, 'PM': 5}, 'Ataque Vorpal':{'ATK':AtaqueVorpal, 'PM': 3}}
                    PLAYER['classe'] = 4
                    break
                elif comando.startswith('v'):
                    continue
                else:
                    print('...')
                    print('<Arkam Braço Metálico> -- Não entendi. Pode repetir?')
                    
    def Atacar(atacante, vitima):
        '''
        Função definida para os ataques fisicos simples, feitos com F.
        '''
        nonlocal rolar
        msg = '<!> {} ataca {} com {}'.format(atacante['Nome'], vitima['Nome'], atacante['dano'])
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
            msg += ', atingido-lhe em cheio, recebendo {} pontos de dano.'.format(dano)
            vitima['PV'] -= dano
        else:
            msg += ' e causa {} pontos de dano.'.format(dano)
            vitima['PV'] -= dano
        print(msg)

    def Ajuda():
        '''
        Função definida para o menu de ajuda.
        '''
        nonlocal PLAYER
        msg = 'Ações disponíveis: '
        aux = 1
        for comando in PLAYER['ATK']:
            msg += comando
            if aux != len(PLAYER['ATK']):
                msg+=', '
            else:
                msg+='.'
            aux += 1
        print(msg)
        
    def AtaqueVorpal (atacante, vitima):
        '''
        Função definida para o uso da magia "Ataque Vorpal" do Paladino.
        '''
        nonlocal rolar
        nonlocal testar
        atacante['PM'] -= 3
        print ('<!> {} ora para que os deuses abençoem a lâmina de sua espada e investe contra {}.'.format(atacante['Nome'],vitima['Nome']))
        critico = False
        dadoAtaque = rolar()
        ataque = atacante['F']+atacante['H']+dadoAtaque+1
        if dadoAtaque == 6:
            critico = True
            ataque += atacante['F']+1
        dadoDefesa = rolar()
        defesa = vitima['A']+vitima['H']+dadoDefesa
        if dadoDefesa == 6:
            defesa += vitima['A']
        dano = ataque-defesa
        dano = max(0, dano)
        if (dano != 0) and critico:
            if testar(vitima['R']):
                print('<!> A espada corta o ar em direção a cabeça de {}, que consegue esquivar da lâmina, mas acaba atingido pelo corte que viaja através do vento,\n\
sofrendo {} pontos de dano.'.format(vitima['Nome'], dano))
            else:
                print('<!> Girando seu corpo rapidamente, {} consegue separar a cabeça de {} do corpo, que cai inerte no chão.'.format(atacante['Nome'], vitima['Nome']))
                vitima['PV'] = 0
        elif dano!= 0:
            print ('<!> {} brande a espada ferozmente em um giro que corta o ar a sua volta, atingindo {} e causando {} pontos de dano.'.format(atacante['Nome'], vitima['Nome'], dano))
        else:
            print('<!> {} consegue desviar do seu golpe no último instante, dando um salto para trás e saindo ileso do ataque.'.format(vitima['Nome']))
        vitima['PV'] -= dano
        
    def CuraMagica (*args):
        '''
        Função definida para a magia cura mágica
        '''
        nonlocal rolar
        nonlocal PLAYER
        dado = rolar()
        PLAYER['PM'] -= 2
        PLAYER['PV'] = min(PLAYER['MAX'][0], PLAYER['PV'] + dado)
        print ('<!> {0} concentra energias mágicas em suas mãos, levando-as ao corpo para amenizar seus ferimentos.'.format(PLAYER['Nome']))
        print ('<!> {} recupera {} pontos de vida.'.format(PLAYER['Nome'], dado))
        
    def Disparar(atacante, vitima):
        '''
        Função definida para os ataques físicos a distância, feitos com PdF.
        '''
        nonlocal rolar
        msg = '<!> {} dispara {} contra {}'.format(atacante['Nome'], atacante['dano'], vitima['Nome'])
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

    def Esconjuro(atacante, vitima):
        '''
        Função definida para a magia esconjuro, efetiva apenas contra mortos vivos.
        '''
        nonlocal testar
        atacante['PM'] -= 5
        msg ='<!> Depois de uma oração, {} estende as mãos na direção de {}'.format(atacante['Nome'], vitima['Nome'])
        if (testar(vitima['R'])) or (vitima['Tipo'] != 'morto-vivo'):
            msg+=', mas nada acontece.'
        else:
            msg+=', liberando uma grande quantidade de luz que atinge seu alvo em cheio, destruindo-o.'
            vitima['PV'] = 0
        print(msg)

    def GolpeDemolidor(atacante, vitima):
        '''
        Função definida para o ataque especial do guerreiro.
        '''
        nonlocal rolar
        atacante['PM'] -= 3
        dado = rolar()
        ataque = dado+atacante['F']+atacante['H']+2
        critico = False
        if dado == 6 or dado == 5:
            critico = True
            ataque += 2*atacante['F']
        dado = rolar()
        defesa = vitima['A']+vitima['H']+dado
        if dado == 6:
            defesa += vitima['A']
        dano = ataque-defesa
        dano = max(0, dano)
        if dano != 0 and critico:
            print('<!> {} gira seu machado com violência, descendo-o rapidamente em um golpe vertical.\n {} É atingido em cheio, sofrendo {} pontos de dano.'.format(atacante['Nome'],vitima['Nome'], dano))
        elif dano!= 0:
            print('<!> () brande seu machado furiosamente contra {}, atingido-o e causando {} pontos de dano.'.format(atacante['Nome'],vitima['Nome'],dano))
        else:
            print('<!> {} avança com o machado em mãos, brandindo-o em um movimento rápido, mas acaba por errar {}, que se esquiva sem dificuldades.'.format(atacante['Nome'], vitima['Nome']))
        vitima['PV'] -= dano
        
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
        msg = '<!> {} concentra suas energias em {} antes de realizar o disparo fatal.'.format(atacante['Nome'], atacante['dano'])
        print(msg)
        dado = rolar()
        defesa = vitima['H'] + vitima['PdF'] + dado
        dano = ataque - defesa
        if dano <= 0:
            msg = '<!> No entanto, {} consegue proteger-se do disparo, fazendo {} errar seu alvo.'.format(vitima['Nome'], atacante['Nome'])
        elif dado == 1:
            msg = '<!> {} é atingido em cheio pelo disparo que atravessa seu corpo, causando {} pontos de dano.'.format(vitima['Nome'], dano)
        else:
            msg = '<!> {} é atingo pelo disparo sofrento {} pontos de dano.'.format(vitima['Nome'], dano)
        dano = max(dano, 0)
        vitima['PV'] -= dano
        print(msg)

    def Arpao (atacante, vitima):
        '''
        Função definida para o uso da magia Arpão
        '''
        nonlocal rolar
        atacante['PM'] -= 15
        msg = '<!> {} junta uma grande quantidade de energia mágica em suas mãos e, com o sussurrar\n\
                de algumas palavras mágicas, disparando de suas mãos uma onda roxa na forma de um arpão.'.format(atacante['Nome'])
        print(msg)
        ataque = atacante['H']
        for i in range (6):
            ataque += rolar()
        dado = rolar()
        defesa = vitima['H']+vitima['A']+dado
        dano = ataque-defesa
        if dano <= 0:
            msg = '<!> Milagrosamente, {} consegue desviar do arpão mágico, saindo ileso do golpe.'.format(vitima['Nome'])
        elif dado == 1:
            msg = '<!> {} é atingido em cheio pelo ataque, sendo arremessado para longe pelo impacto e sofrento {} pontos de dano.'.format(vitima['Nome'], dano)
        else:
            msg = '<!> {} é atingo pelo disparo, sofrendo queimaduras mágicas por todo o corpo e recebendo {} pontos de dano.'.format(vitima['Nome'], dano)
        print(msg)
        dano = max(dano, 0)
        vitima['PV'] -= dano
        
    def BolaDeFogo(atacante, vitimas):
        '''
        Função definida para o uso da magia Bola de Fogo.
        '''
        nonlocal rolar
        ataque = atacante['H']+5+rolar()
        atacante['PM'] -= 5
        msg1 = '<!> {} sussurra algumas palavras mágicas e extende as mãos em direção'.format(atacante['Nome'])
        if len(vitimas) == 1:
            msg1 += ' ao inimigo e de suas mãos uma grande bola de fogo é disparada.'
        else:
            msg1 += 'aos inimigos e de suas mãos uma grande bola de fogo é disparada.'
        print(msg1)
        redutor = 0
        for alvo in vitimas:
            dado = rolar()
            defesa = alvo['H']+alvo['A']+dado
            if (dado == 6) and (alvo['A']>0):
                defesa += alvo['A']
            dano = ataque-defesa-redutor
            dano = max(0, dano)
            if dano == 0:
                msg2 = '<!> {} consegue defender-se da bola de fogo, saindo ileso do ataque.'.format(alvo['Nome'])
                print(msg2)
            elif dado == 1:
                msg2 = '<!> A bola de fogo atinge {} em cheio, causando {} ponto de dano.'.format(alvo['Nome'], dano)
                print(msg2)
                alvo['PV'] -= dano
            else:
                msg2 = '<!> A bola de fogo explode próxima a {}, causando-lhe {} pontos de dano.'.format(alvo['Nome'], dano)
                print(msg2)
                alvo['PV'] -= dano
        redutor += 2

    def CranioVoador(atacante, vitima):
        '''
        Função definida para a magia O Crânio Voador de Vladislav.
        '''
        nonlocal rolar
        ataque = atacante['H']+rolar()+rolar()
        atacante['PM'] -= 3
        msg = '<!> {} dispara de suas mãos um horrendo crânio de energia mágica, que voa na direção de seu alvo.'.format(atacante['Nome'])
        print(msg)
        defesa = vitima['H']+rolar()
        dano = ataque-defesa
        if dano <= 0:
            msg = '<!> O crânio erra o alvo e {} sai ileso do ataque.'.format(vitima['Nome'])
        else:
            msg = '<!> {} é atingido pelo crânio voador, que causa queimaduras mágicas pelo seu corpo.'.format(vitima['Nome'])
            vitima['PV'] -= dano
        print(msg)

    def MordidaVampiro (atacante, vitima):
        '''
        Função definida para o ataque padrão do Vampiro.
        '''
        nonlocal rolar
        ataque = atacante['F']+atacante['H']+rolar()
        print ('<!> {} salta na direção de {}, abrindo ao máximo sua boca e expondo grandes caninos prontos para dilacerar.'.format(atacante['Nome'], vitima['Nome']))
        dado = rolar()
        defesa = vitima['A']+vitima['H']+dado
        if dado == 6:
            defesa += vitima['A']
        dano = ataque-defesa
        dano = max(0, dano)
        if dano <= 0:
            print('<!> No último instante, {} rola para o lado, escapando do ataque ileso.'.format(vitima['Nome']))
        else:
            print('<!> {0} É atingido pela mordida de {1}, que corta seu pescoço, dilacerando sua carne.\n'
                  '{0} sofre {2} pontos de dano e {1} recupera {2} ponto de vida.'.format(vitima['Nome'], atacante['Nome'], dano))
        vitima['PV'] -= dano
        atacante['PV'] += dano

    def Berserker (usuario):
        '''
        Função definida para o modo berserker do ogre.
        '''
        usuario['PM'] = 0
        usuario['PV'] += 5
        usuario['F'] += 2
        usuario['ATK']['poder'] = {'ATK':Atacar, 'PM':0}
        print('<!> {0} dá um urro de fúria, fazendo as paredes da masmorra ao redor tremerem.\n'
              '<!> {0} começa a babar e rosnar, segurando mais forte {1}.'.format(usuario['Nome'],usuario['dano']))

    def EnxamedeTrovoes(atacante, vitima):
        '''
        Função definida para a magia especial do Necromante.
        '''
        nonlocal rolar
        nonlocal testar
        atacante['PM'] -= 5
        print('Depois de algumas palavras mágicas, {} dispara de suas mãoes uma rajada de energia negra que emite um ruído estridente.'.format(atacante['Nome']))
        ataque = rolar()+rolar()+atacante['H']
        defesa = rolar()+vitima['H']
        dano = ataque-defesa
        dano = max(0, dano)
        if dano == 0:
            print('{} consegue saltar para longe da rajada de energia, escapando ileso do ataque.'.format(vitima['Nome']))
        else:
            if testar(vitima['A']):
                queda = 0
            else:
                queda = rolar()
            print('{} é atingido pela rajada de energia e arremessado para trás com violência.'.format(vitima['Nome']))
            if queda:
                print('{} sofre {} pontos de dano da magia e {} pontos de dano do impacto de sua queda.'.fomat(vitima['Nome'],dano, queda))
            else:
                print('{} sofre {} pontos de dano do golpe.'.format(vitima['Nome'],dano))

    def ProtecaoMagica(usuario):
        '''
        Função definida para a magia especial do Necromante.
        '''
        usuario['A'] += 2
        usuario['Status'] = 'Armadura'
        print('{} sussurra palavras mágicas obscuras, fazendo surgir ao redor de seu corpo uma armadura de energia negra que aparenta ser feita de ossos.'.format(usuario['Nome']))
        

    def EncontrarInimigo():  #IA de controle de inimigos
        nonlocal PLAYER
        nonlocal Grunts
        nonlocal Monstros
        nonlocal Generais
        nonlocal rolar
        global vilao
        print('...\n')
        def ContarInimigos(lista):
            inimigos = []
            for e in lista:
                qtd = '{} {}'.format(lista.count(e), e['Nome'])
                if qtd not in inimigos:
                    inimigos.append(qtd)
            mensagem = ''
            aux = 1
            for qtd in inimigos:
                msg = qtd
                if aux != len(inimigos):
                    msg += ', '
                elif (len(inimigos) != 1):
                    msg = 'e ' + msg + '.'
                else:
                    msg += '.'
                mensagem += msg
                aux += 1
            return mensagem
        if (PLAYER['score'] >= 30):  # Enfrentar General
            vilao = True
            return [Generais[0]]
        elif (PLAYER['score'] > 0) and (PLAYER['score']%5 == 0):  # Enfrentar Monstro
            fator = randint(1, 6)%2
            return [Monstros[fator].copy()]
        else:
            ending = (PLAYER['score']%5 or 2)
            fator = randint(1, ending)+1
            inimigos = []
            for a in range(fator):
                inimigos.append(Grunts[randint(1, (len(Grunts)-1))].copy())
            print('<!> Você segue caminhando pela masmorra, atravessando seus corredores escuros quando, se depara com '
            'um grupo de inimigos que vem em sua direção.')
            grupo_inimigo = ContarInimigos(inimigos)
            print(grupo_inimigo)
            return inimigos
        print('<!>')

    def Jogar():
        '''
        Função definida para o Menu entre as batalhas.
        '''
        global fim_de_jogo
        PLAYER['ATK']['Ajuda']  = {'ATK':Ajuda, 'PM':0}
        while True:
            print('...')
            comando = input('Continuar(c/continuar), Salvar(s/salvar), Personagem(p/personagem), Gastar Experiência (e/exp), Desistir(d/desistir)\n')
            if comando.startswith('c'):
                break
            elif comando.startswith ('s'):
                try:
                    arquivo = open('continue.txt', 'a')
                except FileNotFoundError:
                    arquivo = open('continue.txt','w')
                finally:
                    arquivo.write('{}\n'.format(PLAYER['Nome']))
                    arquivo.write('{}f{}h{}r{}a{}p{}v{}m{}e{}c\n'.format(PLAYER['F'],PLAYER['H'],PLAYER['R'],PLAYER['A'],PLAYER['PdF'],PLAYER['PV'],PLAYER['PM'],PLAYER['PE'],PLAYER['classe']))
                    arquivo.write('{}\n'.format(PLAYER['score']))
                    print('...')
                    print ('<!> {} salvo com sucesso!'.format(PLAYER['Nome']))
            elif comando.startswith ('p'):  # Visualização do Personagem
                print('...')
                print('Força {}, Habilidade {}, Resistência {}, Armadura {}, Poder de Fogo {}, PV {}/{}, PM {}/{}'.format(PLAYER['F'], PLAYER['H'], PLAYER['R'], PLAYER['A'], PLAYER['PdF'], PLAYER['PV'], PLAYER['MAX'][0], PLAYER['PM'], PLAYER['MAX'][1]))
                print('Pontos de Experiência: {}\nPontuação: {}'.format(PLAYER['PE'], PLAYER['score']))
                msg = 'Ações: '
                aux = 1
                for comando in PLAYER['ATK']:
                    msg += comando
                    if aux != len(PLAYER['ATK']):
                        msg+=', '
                    else:
                        msg+='.'
                    aux += 1
            elif comando.startswith('e'):  # Menu de Experiência
                print('...')
                print('Pontos de Experiência: {}'.format(PLAYER['PE']))
                while True:
                    comando = input('Recuperar PVs [1 PE](v/vida), Recuperar PMs [2 PE](m/magia), Aumentar Característica [10 PE](c/caracteristica), Sair(s/sair)').lower()
                    print('...')
                    if comando.startswith('v'):
                        if (PLAYER['PE'] >= 1) and (PLAYER['PV'] < PLAYER['MAX'][0]):
                            PLAYER['PV'] = PLAYER['MAX'][0]
                            PLAYER['PE'] -= 1
                            print('Pontos de Vida restaurados para {}'.format(PLAYER['PV']))
                        elif (PLAYER['PV'] >= PLAYER['MAX'][0]):
                            print('Seus Pontos de Vida estão no máximo, volte quando sofrer danos.')
                        else:
                            print('Você nao tem Pontos de Experiência suficientes')
                    elif comando.startswith('m'):
                        if (PLAYER['PE'] >= 2) and (PLAYER['PM'] < PLAYER['MAX'][1]):
                            PLAYER['PM'] = PLAYER['MAX'][1]
                            PLAYER['PE'] -= 2
                            print('Pontos de Magia restaurados para {}'.format(PLAYER['PV']))
                        elif (PLAYER['PM'] >= PLAYER['MAX'][1]):
                            print('Você nao pode ter mais que {} Pontos de Magia'.format(PLAYER['MAX'][1]))
                        else:
                            print('Você nao tem Pontos de Experiência suficientes')
                    elif comando.startswith('c'):
                        if (PLAYER['PE'] >= 10):
                            print('...')
                            print('Força: {}, Habilidade: {}, Resistência: {}, Armadura: {}, Poder de Fogo: {}'.format(PLAYER['F'],PLAYER['H'],PLAYER['R'],PLAYER['A'],PLAYER['PdF']))
                            print('Qual caracteristica deseja aprimorar?\nForça(F), Habilidade(H), Resistencia(R), Armadura(A), Poder de Fogo(P)')
                            comando = input().lower()
                            print('...')
                            if comando.startswith('f'):
                                if PLAYER['F'] < 5:
                                    PLAYER['PE'] -= 10
                                    PLAYER['F'] += 1
                                    print('Você aumentou sua Força em +1 Ponto. Seus ataques corporais agora causam mais dano.')
                                else:
                                    print('Você já atingiu o valor limite para essa característica.')
                            elif comando.startswith('h'):
                                if PLAYER['H'] < 5:
                                    PLAYER['PE'] -= 10
                                    PLAYER['H'] += 1
                                    print('Você aumentou sua Habilidade em +1 Ponto. Você se tornou mais rápido e preciso.')
                                else:
                                    print('Você já atingiu o valor limite para essa característica.')
                            elif comando.startswith('r'):
                                if PLAYER['R'] < 5:
                                    PLAYER['PE'] -= 10
                                    PLAYER['R'] += 1
                                    PLAYER['PV'] += 5
                                    PLAYER['PM'] += 5
                                    PLAYER['MAX'] = ((PLAYER['MAX'][0]+5),(PLAYER['MAX'][1]+5))
                                    print('Você aumentou sua Resistênciaça em +1 Ponto. Seus Pontos de Vida e Magia tambem aumentaram.')
                                else:
                                    print('Você já atingiu o valor limite para essa característica.')
                            elif comando.startswith('a'):
                                if PLAYER['A'] < 5:
                                    PLAYER['PE'] -= 10
                                    PLAYER['A'] += 1
                                    print('Você aumentou sua Armadura em +1 Ponto. Você agora é mais resistente a danos.')
                                else:
                                    print('Você já atingiu o valor limite para essa característica.')
                            elif comando.startswith('p'):
                                if PLAYER['PdF'] < 5:
                                    PLAYER['PE'] -= 10
                                    PLAYER['PdF'] += 1
                                    print('Você aumentou seu Poder de Fogo em +1 Ponto. Seus ataques a distancia agora causam mais dano.')
                                else:
                                    print('Você já atingiu o valor limite para essa característica.')
                        else:
                            print('Você não tem Pontos de Experiência suficientes para evoluir uma característica.')
                    elif comando.startswith('s'):
                        break
                    else:
                        print('Comando inválido. Tente novamente.')
            elif comando.startswith('d'):
                fim_de_jogo = True
                break
            else:
                print('...')
                print('Escolha um comando válido.')
            
    def CarregarJogos():
        '''
        Função definida para o carregamento de jogos salvos.
        '''
        try:
            arquivo = open('continue.txt','r')
        except FileNotFoundError:
            return []
        else:
            codigo = 'Tormenta 2018'
            jogos = []
            while codigo != '':
                codigo = arquivo.readline()
                if codigo != '':
                    nome = ''
                    for c in codigo:
                        if c!='\n':
                            nome += c
                    codigo = arquivo.readline()
                    temp = ''
                    for c in codigo:
                        if c == 'f':
                            f = int(temp)
                            temp = ''
                        elif c == 'h':
                            h = int(temp)
                            temp = ''
                        elif c == 'r':
                            r = int(temp)
                            temp = ''
                        elif c == 'a':
                            a = int(temp)
                            temp = ''
                        elif c == 'p':
                            pdf = int(temp)
                            temp = ''
                        elif c == 'v':
                            pv = int(temp)
                            temp = ''
                        elif c == 'm':
                            pm = int(temp)
                            temp = ''
                        elif c == 'e':
                            pe = int(temp)
                            temp = ''
                        elif c == 'c':
                            classe = int(temp)
                            temp = ''
                        else:
                            temp += c
                    codigo = arquivo.readline()
                    score = ''
                    for c in codigo:
                        if c != '\n':
                            score += c
                    score = int(score)
                    if classe == 1:
                        atk = {'Arco':{'ATK':Disparar, 'PM':0}, 'Faca':{'ATK':Atacar, 'PM':0},'Golpe Fatal':{'ATK':TiroCerteiro, 'PM':4}}
                        dano = 'seu arco'
                        maximo = (10, 10)
                    elif classe == 2:
                        atk = {'Machado':{'ATK':Atacar, 'PM': 0}, 'Golpe Demolidor':{}}
                        dano = 'seu machado'
                        maximo = (20, 10)
                    elif classe == 3:
                        atk = {'Arpão':{'ATK':Arpao, 'PM':15},'Cajado': {'ATK':Atacar, 'PM': 0}, 'Bola de Fogo': {'ATK': BolaDeFogo, 'PM': 5}}
                        dano = 'seu cajado'
                        maximo = (10, 30)
                    elif classe == 4:
                        atk = {'Espada':{'ATK':Atacar, 'PM':0}, 'Cura Mágica':{'ATK':CuraMagica, 'PM':2}, 'Esconjuro':{'ATK': Esconjuro, 'PM': 5}, 'Ataque Vorpal':{'ATK':AtaqueVorpal, 'PM': 3}}
                        dano = 'sua espada'
                        maximo = (15, 15)
                    jogos.append(dict(Nome=nome, F=f, H=h, R=r, A=a, PdF=pdf, score=score, PV=pv, PM=pm, PE=pe, ATK=atk, dano=dano, MAX=maximo, classe=classe))
            return jogos
                
    #  Fichas dos inimigos abaixo:

    ZUMBI = {'Nome': 'Zumbi', 'F':1, 'H':1, 'R':1, 'A':0, 'PdF':0, 'PV':5, 'PM':5, 'Status':'Normal', 'dano': 'suas garras', 'Tipo': 'morto-vivo', 'score':1}
    ZUMBI['ATK'] = {'ataque': {'ATK': Atacar, 'PM': 0}}
    ZUMBI['Morte'] = 'O zumbi cai no chão, onde permanece imóvel.'
    
    TROG = {'Nome': 'Troglodita', 'F':2, 'H':1, 'R':2, 'A':1, 'PdF': 0, 'PV':10, 'PM':10, 'Status': 'Normal', 'dano': 'sua clava', 'Tipo': 'trog', 'score':2}
    TROG['ATK'] = {'ataque':{'ATK': Atacar, 'PM': 0}}
    TROG['Morte'] = 'O horrendo lagarto trog cai no chão segurando as entranhas onde morre.'

    ESQUELETO = {'Nome': 'Esqueleto', 'F': 2, 'H':0, 'R':2, 'A':1, 'PdF':0, 'PV': 10, 'PM':10, 'Status':'Normal', 'dano':'seus punhos', 'Tipo':'morto-vivo','score':2}
    ESQUELETO['ATK'] = {'ataque':{'ATK':Atacar, 'PM':0}}
    ESQUELETO['Morte'] = 'O esqueleto se desmonta, tornando-se uma pilha de ossos comuns.'

    KOBOLD = {'Nome': 'Kobold', 'F':0, 'H':2, 'R':1, 'A':0, 'PdF':2, 'PV': 5, 'PM': 5, 'Status':'Normal', 'dano':'sua funda', 'Tipo':'Humanoide', 'score':1}
    KOBOLD['ATK'] = {'ataque':{'ATK':Disparar, 'PM':0}}
    KOBOLD['Morte'] = 'O Kobold cai no chão imóvel.'

    # Monstros
    VAMPIRO = {'Nome': 'Vampiro', 'F':2, 'H':2, 'R':3, 'A':1, 'PdF':0, 'PV':10, 'PM':10, 'Status':'Normal', 'dano': 'suas garras', 'Tipo':'morto-vivo', 'score':2}
    VAMPIRO['ATK'] = {'poder':{'ATK': MordidaVampiro, 'PM':3}, 'ataque':{'ATK':Atacar, 'PM':0}}
    VAMPIRO['Morte'] = 'A besta vampira se desfaz em uma poça de sangue e gosma.'

    OGRO = {'Nome': 'Ogre', 'F':3, 'H':1, 'R':2, 'A':2, 'PdF':0, 'PV':15, 'PM':5, 'Status':'Normal', 'dano':'sua clava', 'Tipo':'Humanoide','score':3}
    OGRO['ATK'] = {'ataque':{'ATK':Atacar, 'PM':0}, 'poder':{'ATK':Berserker, 'PM':5}}
    OGRO['Morte'] = 'A pancada do corpanzil inerte do ogre atingindo o chão faz as paredes da masmorra tremerem.'

    #General
    NECROMANTE = {'Nome': 'Necromante', 'F':0, 'H':3, 'R':3, 'A':2, 'PdF':3, 'PV': 15, 'PM':25, 'Status':'Normal', 'dano':'energia negra', 'Tipo':'Humano', 'score':10}
    NECROMANTE['ATK'] = {'ataque': {'ATK': Disparar, 'PM':0}, 'poder':{'ATK':CranioVoador, 'PM':3}, 'especial':{'ATK':EnxamedeTrovoes, 'PM':5}, 'proteção':{'ATK':ProtecaoMagica, 'PM': 4}}
    NECROMANTE['Morte'] = 'O Necromante começa a se desfazer em uma nuvem de fumaça negra.'
    NECROMANTE['AI'] = General

    # Grupos de inimigos
    Grunts = [ZUMBI, TROG, ESQUELETO, KOBOLD]
    for i in Grunts:
        i['AI'] = Grunt
    Monstros = [VAMPIRO, OGRO]
    for i in Monstros:
        i['AI'] = Monstro
    Generais = [NECROMANTE]
    
    # Inicio do Jogo
    while True:
        print('...')
        escolha = input('Novo Jogo(n/novo), Continuar(c/continuar), Sair(s/sair)\n').lower()
        fim_de_jogo = False
        if escolha.startswith('c'):
            jogos_salvos = CarregarJogos()
            if len(jogos_salvos) == 0:
                print("Não existem jogos salvos a serem carregados.")
            else:
                print("Selecione o personagem que deseja carregar:\n")
                aux = 1
                for personagem in jogos_salvos:
                      print(str(aux)+' - {} (F{} H{} R{} A{} PdF{} PV{}/{} PM{}/{} PE{})'.format(personagem['Nome'], personagem['F'], personagem['H'], personagem['R'], personagem['A'], personagem['PdF'], personagem['PV'], personagem['MAX'][0], personagem['PM'], personagem['MAX'][1], personagem['PE']))
                      aux += 1
                escolha = int(input('\n\nDigite o número correspondente ao personagem\n'))
                try:
                    selecionado = jogos_salvos[escolha-1]
                except IndexError:
                    print('Selecione um personagem válido')
                else:
                    PLAYER['Nome'] = selecionado['Nome']
                    PLAYER['F'] = selecionado['F']
                    PLAYER['H'] = selecionado['H']
                    PLAYER['R'] = selecionado['R']
                    PLAYER['A'] = selecionado['A']
                    PLAYER['PdF'] = selecionado['PdF']
                    PLAYER['PV'] = selecionado['PV']
                    PLAYER['PM'] = selecionado['PM']
                    PLAYER['PE'] = selecionado['PE']
                    PLAYER['MAX'] = selecionado['MAX']
                    PLAYER['score'] = selecionado['score']
                    PLAYER['ATK'] = selecionado['ATK']
                    PLAYER['dano'] = selecionado['dano']
                    PLAYER['classe'] = selecionado['classe']
                    print('<!> {}, bem-vindo de volta a masmorra.'.format(selecionado['Nome']))
                    while not fim_de_jogo:
                        Jogar()
                        if not fim_de_jogo:
                            inimigos = EncontrarInimigo()
                            print('...')
                            Combate(PLAYER, inimigos)
                            if not fim_de_jogo and not vilao:
                                PLAYER['PE'] += 1
                            elif vilao:
                                print('...')
                                print('<!> Depois de derrotar o necromante uma alçapão se abre sobre a sua cabeça.\n'
                                      '<!> Por um instante a claridade o deixa cego, mas aos poucos você recupera a sua visão.\n'
                                      '<!> De dentro do alçapão uma luva de metal, como um braço de armadura oferece-lhe ajuda.\n'
                                      '<!> Era Arkam, o braço metálico, com um sorriso estampado no rosto.'
                                      '<Arkamm Braço Metálico> -- Você é um dos primeiros aventureiros novatos a conseguir concluir o desafio da masmorra.\n'
                                      '<Arkam Braço Metálico> -- Parabéns!\n'
                                      '<!> Atrás de Arkam outras pessoas sorriam e aplaudiam o seu feito, dando-lhe as boas vindas ao protetorado do reino.\n'
                                      '<!> O Círculo se reunira mais uma vez, e a união de aventureiros tão poderosos só poderia significar uma coisa:\n'
                                      '<!> Artom estava com problemas.')
                                print('Parabéns, {}. Sua pontuação é de {} Pontos.'.format(PLAYER['Nome'],PLAYER['score']))
                    
                
        elif escolha.startswith('s'):
            break
        elif escolha.startswith('n'):
            fim_de_jogo = False
            print('<!> Bem-vindo, aventureiro, ao desafio da masmorra do protetorado do reino.\n\n\n')
            PLAYER['Nome'] = input('<Arkam Braço Metálico> -- Então você acha que é capaz de vencer o desafio? Bom, isso é o que vamos ver.\n'
                                   '<Arkam Braço Metálico> -- Antes de entrar, diga-me, qual seu nome?\n...\n').capitalize()
            print('...')
            print('<Arkam Braço Metálico>: -- Bem-vindo, {}. A masmorra está pronta para recebê-lo, mas pelo visto você ainda não está pronto para prosseguir.\n'
                  '*Arkam lhe aponta uma mesa com armas e equipamentos de diversos tipos.*'
                  '\n<Arkam Braço Metálico> -- Na masmorra você precisa usar equipamentos especiais, feitos para as mais diversas classes de aventureiros. Escolha com sabedoria.'.format(PLAYER['Nome']))
            MenuClasse()
            print('...')
            print('<!>Arkam permite que você pegue seus equipamentos e o guia através de um corredor escuro até uma porta de madeira velha.\n'
                  '<!> A porta está protegida por uma barra de metal brilhante, provavelmente mágico, que emite uma fraca luz azul.')
            print('<Arkam Braço Metálico> -- É aqui que nos separamos, {}. Espero encontrá-lo do outro lado da masmorra. Hahaha'
                  '<Arkam Braço Metálico> -- Boa sorte.'.format(PLAYER['Nome']))
            print('<!> A porta se abre e você a entra, ouvindo o rangido e a batida da porta fechando-se logo atrás de você.')
            while not fim_de_jogo:
                Jogar()
                if not fim_de_jogo:
                    inimigos = EncontrarInimigo()
                    print('...')
                    Combate(PLAYER, inimigos)
                    if not fim_de_jogo:
                        PLAYER['PE'] += 2
                else:  # Definir Game Over
                    pass
        else:
            print('<!> Comando inválido. Tente novamente.')

Main()
print('Obrigado por jogar!')
print(':)')
