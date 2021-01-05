# VASCO SILVA IST199132

#  2.1.1 TAD posicao

def cria_posicao(c, l):
    """ Funcao de operacao basica para criar uma posicao. Foi escolhida a representacao na forma de lista.

    :param c: (str) coluna do tabuleiro representada pelos valores em valores_possiveis_c
    :param l: (str) linha do tabuleiro representada pelos valores em valores_possiveis_1
    :return:  (list) lista com o primeiro termo a representar o valor da coluna e o segundo a representar o da linha
    """
    valores_possiveis_l = ('1', '2', '3')
    valores_possiveis_c = ('a', 'b', 'c')
    if l not in valores_possiveis_l or c not in valores_possiveis_c:
        raise ValueError('cria_posicao: argumentos invalidos')
    return [c, l]


def cria_copia_posicao(p):
    """ Funcao de operacao basica para criar uma copia de uma posicao.

    :param p: (list) posicao com a representacao escolhida neste caso uma lista
    :return: (list) uma nova copia da posicao
    """
    return p.copy()


def obter_pos_c(p):
    """ Funcao de operacao basica para obter a coluna da posicao passada como argumento.

    :param p: (list) posicao com a representacao escolhida neste caso uma lista
    :return: (str) coluna da posicao
    """
    return p[0]


def obter_pos_l(p):
    """ Funcao de operacao basica para obter a linha da posicao passada como argumento.

    :param p: (list) posicao com a representacao escolhida neste caso uma lista
    :return: (str) linha da posicao
    """

    return p[1]


def eh_posicao(arg):
    """ Funcao de operacao basica para verificar se o argumento introduzido se trata de uma posicao

    :param arg: (any type) argumento de qualquer tipo.
    :return: (bool) True se for uma posicao valida False caso contrario.
    """
    valores_possiveis_l = ('1', '2', '3')
    valores_possiveis_c = ('a', 'b', 'c')
    return type(arg) == list and len(arg) == 2 and obter_pos_c(arg) in valores_possiveis_c and obter_pos_l(arg) \
           in valores_possiveis_l


def posicoes_iguais(p1, p2):
    """ Funcao de operacao basica para verificar se duas posicoes sao iguais

    :param p1: (list) posicao com a representacao escolhida neste caso uma lista
    :param p2: (list) posicao com a representacao escolhida neste caso uma lista
    :return: (bool) True caso as posicoes sejam iguais False caso contrario.
    """
    return eh_posicao(p1) and eh_posicao(p2) and p1 == p2


def posicao_para_str(p):
    """ Funcao de operacao basica para representar uma posicao na forma de string

    :param p: (list) posicao com a representacao escolhida neste caso uma lista
    :return: (str) posicao na forma de string
    """
    return obter_pos_c(p) + obter_pos_l(p)


def obter_posicoes_adjacentes(p):
    """ Funcao de alto nivel que permite obter as posicoes adjacentes num tabuleiro de jogo do moinho da posicao
        especificada.

    :param p:  posicao com qualquer representacao
    :return: (tuple) tuplo com as posicoes adjacentes
    """
    valores_posiveis_c = ('a', 'b', 'c')
    valores_posiveis_l = ('1', '2', '3')
    pos_possiveis = [cria_posicao(c, l) for l in valores_posiveis_l for c in valores_posiveis_c]
    res_validos = ((1, 0), (0, 1), (-1, 0), (0, -1))  # as posicoes adjacentes a uma posicao podem ser obtidas
    res_validos_diag = ((1, 1), (-1, -1), (1, -1), (-1, 1))
    valores_com_diag = (cria_posicao('a', '1'), cria_posicao('c', '1'), cria_posicao('a', '3'), cria_posicao('c', '3'),
                        cria_posicao('b', '2'))
    # subtraindo o ord da coluna e o valor da linha a posicao argumento, se a posicao for adjacente obtemos um dos
    # resultados do tuplo res_validos ou res_validos_diag visto que as posicoes adjacentes se encontram um valor para a
    # direita, para esquerda, para cima ou para baixo ou mesmo uma combinacao de dois membros deste conjunto dependendo
    # da posicao no tabuleiro
    return tuple(i for i in pos_possiveis if ((ord(obter_pos_c(p)) - ord(obter_pos_c(i)), int(obter_pos_l(p)) -
                                               int(obter_pos_l(i))) in res_validos) or (i in valores_com_diag and
                                                                                        (ord(obter_pos_c(p)) - ord(
                                                                                            obter_pos_c(i)),
                                                                                         int(obter_pos_l(p))
                                                                                         - int(obter_pos_l(
                                                                                             i))) in res_validos_diag))


#  2.1.2 TAD peca

def cria_peca(peca):
    """ Funcao de operacao basica que cria uma peca de acordo com a representacao escolhida, neste caso um inteiro

    :param peca: (str) recebe um representante de cada peca na forma 'X', 'O' ou ' '
    :return: (int) devolve um inteiro correspondente, 1 oara 'X', -1 para 'O' e 0 para ' '
    """
    pecas = {'X': 1, 'O': -1, ' ': 0}
    if type(peca) != str or peca not in pecas.keys():
        raise ValueError('cria_peca: argumento invalido')
    return pecas[peca]


def cria_copia_peca(peca):
    """ Funcao de operacao basica que cria uma copia da peca especificada

    :param peca: (int) peca na representacao escolhida neste caso um inteiro
    :return: (int) copia da peca
    """
    return int(peca)


def eh_peca(arg):
    """ Funcao de operacao basica que verifica se o argumento introduzido se trata de uma peca

    :param arg: (any type) argumento de qualquer tipo
    :return: (bool) True se o argumento se tratar de um peca do tipo 1, -1 ou 0 e False caso contrario
    """
    pecas = (1, -1, 0)
    return type(arg) == int and arg in pecas


def pecas_iguais(p1, p2):
    """ Funcao de operacao basica para verificar se duas pecas ssao iguais

    :param p1: (int) peca na representacao escolhida neste caso um inteiro
    :param p2: (int) peca na representacao escolhida neste caso um inteiro
    :return: (bool) True se as duas pecas forem iguais False caso contrario
    """
    return p1 == p2


def peca_para_str(peca):
    """ Funcao de operacao basica que transforma um peca na representacaao escolhida numa peca na forma '[X]', '[O]' ou
        '[ ]'

    :param peca: (int) peca na representacao escolhida neste caso um inteiro
    :return: peca na forma '[X]', '[O]' ou '[ ]'
    """
    dic = {1: 'X', -1: 'O', 0: ' '}
    return '[{}]'.format(dic[peca])


def peca_para_inteiro(peca):
    """ Funcao de alto nivel que transforma uma peca na sua representacao sob a forma de inteiro 1, 0 ou -1

    :param peca: peca com qualquer representacao
    :return: inteiro correspondente a peca
    """
    return 1 if peca_para_str(peca) == '[X]' else (-1 if peca_para_str(peca) == '[O]' else 0)


def inteiro_para_peca(inteiro):
    """ Funcao auxiliar que converte um inteiro valido na sua peca correspondente

    :param inteiro: (int) inteiro 1, -1 ou 0
    :return: peca correspondente de acordo com a associacao feita na funcao anterior
    """
    dic_pecas = {1: cria_peca('X'), -1: cria_peca('O'), 0: cria_peca(' ')}
    return dic_pecas[inteiro]


#  2.1.3 TAD tabuleiro


def cria_tabuleiro():
    """ Funcao de operacao basica para criar um tabuleiro na representacao escolhida

    :return: (list) Tabuleiro na representacao escolhida neste uma lista com sublistas
    """
    return [[cria_peca(' '), cria_peca(' '), cria_peca(' ')], [cria_peca(' '), cria_peca(' '), cria_peca(' ')],
            [cria_peca(' '), cria_peca(' '), cria_peca(' ')]]


def cria_copia_tabuleiro(tab):
    """ Funcao de operaca basica para criar uma nova copia de um tabuleiro

    :param tab: (list) Tabuleiro
    :return: (list) uma nova copia do tabuleiro passado como argumento
    """
    return [linha.copy() for linha in tab]


def pos_coordenadas(pos):
    """ Funcao auxiliar de obtencao de coordenadas(index da posicao na linha e index da linha de uma posicao num tuplo
         ou lista) de um posicao especificada

    :param pos: (list) posicao com a representacao escolhida neste caso uma lista
    :return: (tuple) coordenadas da posicao no tabuleiro
    """
    pos_dic = {'a1': (0, 0), 'b1': (1, 0), 'c1': (2, 0), 'a2': (0, 1), 'b2': (1, 1), 'c2': (2, 1), 'a3': (0, 2),
               'b3': (1, 2), 'c3': (2, 2)}
    return pos_dic[posicao_para_str(pos)]


def obter_peca(tab, pos):
    """ Funcao de operacao basica para obter a peca que se encontra na posicao especificada

    :param tab: (list) Tabuleiro
    :param pos: (list) posicao com a representacao escolhida
    :return: (int) peca na representacao escolhida neste caso um inteiro
    """
    coordenadas = pos_coordenadas(posicao_para_str(pos))
    return tab[coordenadas[1]][coordenadas[0]]


def obter_vetor(tab, conjunto):
    """ Funcao de operacao basica que permite obter um as pecas de um vetor (linha ou coluna) na forma de tuplo

    :param tab: (list) Tabuleiro
    :param conjunto: (str) linha ou coluna
    :return: (tuple) tuplo com as pecas presentes na linha ou coluna especificada
    """
    valores_possiveis_l = ('1', '2', '3')
    col = ()
    if conjunto in valores_possiveis_l:
        return tuple(peca for peca in tab[int(conjunto) - 1])
    for linha in range(len(tab)):
        col += (tab[linha][ord(conjunto) - ord('a')],)  # a coordenada de coluna pode ser obtida subtraindo o ord de a
        # ao ord da coluna especificada
    return tuple(peca for peca in col)


def coloca_peca(tab, peca, pos):
    """ Funcao de operacao basica que permite colcoar uma peca numa certa posicao do tabuleiro

    :param tab: (list) Tabuleiro
    :param peca: (int) Peca
    :param pos: (list) Posicao
    :return: (list) O mesmo tabuleiro mas com uma peca alterada
    """
    coordenadas = pos_coordenadas(posicao_para_str(pos))
    tab[coordenadas[1]][coordenadas[0]] = peca
    return tab


def remove_peca(tab, pos):
    """ Funcao de operacao basica que remove a peca de uma posicao do tabuleiro tornando-a uma peca vazia

    :param tab: (list) Tabuleiro
    :param pos: (list) Posicao
    :return: (list) O memso tabuleiro mas com a posicao passada como argumento agora vazia
    """
    coordenadas = pos_coordenadas(posicao_para_str(pos))  # recorremos a funcao auxiliar pos_coordenadas para obter as
    #  coordenadas da posicao para aceder a mesma no tabuleiro
    tab[coordenadas[1]][coordenadas[0]] = cria_peca(' ')
    return tab


def move_peca(tab, p1, p2):
    """ Funcao de operacao basica que permite mover uma peca entre duas posicoes

    :param tab: (list) Tabuleiro
    :param p1:  (list) Posicao de partida
    :param p2:  (list) Posicao de chegada
    :return: (list) O mesmo tabuleiro mas com uma peca movimentada
    """
    peca = obter_peca(tab, p1)
    return coloca_peca(remove_peca(tab, p1), peca, p2)  # ao utilizarmos o remove_peca e o coloca_peca conseguimos tirar
    #  a peca de p1 e coloca-la em p2


def jogadores_ganhadores(tab):
    """ Funcao auxiliar de obtencao de jogadores ganhadores num tabuleiro de jog do moinho, isto e os jogadores que
        tenham 3 pecas em linha horizontal ou verticalmente

    :param tab: (list) Tabuleiro
    :return: (list) lista dos ganhadores no tabuleiro especificado
    """
    ganhador = ((cria_peca('O'), cria_peca('O'), cria_peca('O')),
                (cria_peca('X'), cria_peca('X'), cria_peca('X')))
    return [win for win in ganhador for i in range(1, 4) if obter_vetor(tab, str(i)) == win
            or obter_vetor(tab, chr(ord('a') + (i - 1))) == win]  # iteramos sobre os tuplos ganhadores do ganahdor e
    # comparamos com o tuplo obtido com o obter_vetor


def n_pecas_jog(tab, jog):
    """ Funcao auxiliar que permite contar quantas pecas e que o jogador especificado tem num tabuleiro

    :param tab: (list) Tabuleiro (funciona com qualquer representacao)
    :param jog: (int) Peca que representa o jogador (funciona com qualquer representacao)
    :return: (int) numero de pecas do jogador
    """
    valores_posiveis_c = ('a', 'b', 'c')
    valores_posiveis_l = ('1', '2', '3')
    pos_possiveis = [cria_posicao(c, l) for l in valores_posiveis_l for c in valores_posiveis_c]
    res = 0
    for i in pos_possiveis:
        res += 1 if (pecas_iguais(obter_peca(tab, i), jog)) else 0
    return res


def eh_tabuleiro(tab):
    """ Funcao de verificacao da validade da representacao de um tabuleiro 3x3 de jogo do moinho

    :param tab: (list) Tabuleiro
    :return: (bool) True se o tabuleiro respeitar a representacao escolhida, neste caso uma lista com 3 sublistas onde
                    cada peca e representada pela representacao na TAD peca, neste caso um inteiro, e tiver um maximo
                    de 3 pecas de cada jogador, uma peca de diferenca entre o numero de pecas de cada jogador e apenas
                    1 ganhador em simultaneo. Caso alguma das condicoes acima nao for respeitada o output sera False
    """
    valores_posiveis = (cria_peca('O'), cria_peca('X'), cria_peca(' '))
    if type(tab) != list or len(tab) != 3:
        return type(tab) == list and len(tab) == 3
    for linha in tab:
        if type(linha) != list or len(linha) != 3:
            return type(linha) == list and len(linha) == 3
        for valor in linha:
            if type(valor) != int or valor not in valores_posiveis:
                return type(valor) == int and valor in valores_posiveis
    n_pecas = [n_pecas_jog(tab, jog) for jog in valores_posiveis[:2]]  # lista com o numero de pecas de cada jogador O e
    #  X
    dif_pecas = [abs(len([j for i in tab for j in i if pecas_iguais(j, cria_peca('X'))]) - len(
        [j for i in tab for j in i if pecas_iguais(j, cria_peca('O'))])) <= 1]  # diferenca entre o numero de pecas de
    # cada jogador iterando sobre o tabuleiro e fazendo o modulo da diferenca para verificar se e maior que 1
    res = [len(jogadores_ganhadores(tab)) <= 1] + dif_pecas + [i <= 3 for i in n_pecas]  # ao concatenarmos as listas
    #  criadas para cada condicao conseguimos obter um resultado
    return False not in res  # se False estiver em res entao o tabuleiro nao e valido


def eh_posicao_livre(tab, pos):
    """ Funcao de operacao basica para verificar se um posiao do tabuleiro esta livre

    :param tab: (list) Tabuleiro
    :param pos: (list) Posicao
    :return: (bool) True se a posicao for livre e False caso contrario
    """
    return pecas_iguais(obter_peca(tab, pos), cria_peca(' '))


def tabuleiros_iguais(t1, t2):
    """ Funcao de operacao basica para verificar se dois tabuleiro sao iguais

    :param t1: (list) Tabuleiro 1
    :param t2: (list) Tabuleiro 2
    :return: (bool) True se forem iguais False caso contrario
    """
    return t1 == t2 and eh_tabuleiro(t1) and eh_tabuleiro(t2)


def tabuleiro_para_str(tab):
    """ Funcao de operacao basica que permite representar o tabuleiro na forma de uma string permitindo criar um
    tabuleiro mais compreensivel para ao utilizador

    :param tab: (list) Tabuleiro
    :return: (str) Tabuleiro na forma     a   b   c  (representacao com print())
                                       1 [ ]-[ ]-[ ]
                                          | \ | / |
                                       2 [ ]-[ ]-[ ]
                                          | / | \ |
                                       3 [ ]-[ ]-[ ]
    """
    return '   a   b   c\n1 {}-{}-{}\n   | \\ | / |\n2 {}-{}-{}\n   | / | \\ |\n3 {}-{}-{}'.format(
        peca_para_str(obter_peca(tab, cria_posicao('a', '1'))),
        peca_para_str(obter_peca(tab, cria_posicao('b', '1'))), peca_para_str(obter_peca(tab, cria_posicao('c', '1'))),
        peca_para_str(obter_peca(tab, cria_posicao('a', '2'))), peca_para_str(obter_peca(tab, cria_posicao('b', '2'))),
        peca_para_str(obter_peca(tab, cria_posicao('c', '2'))),
        peca_para_str(obter_peca(tab, cria_posicao('a', '3'))), peca_para_str(obter_peca(tab, cria_posicao('b', '3'))),
        peca_para_str(obter_peca(tab, cria_posicao('c', '3'))))


def tuplo_para_tabuleiro(tup):
    """ Funcao de operacao basica que permite transformar uma representacao de um tabuleiro na forma de tuplo de
        subtuplos com pecas na forma de inteiro, na representacao escolhida na TAD, neste caso uma lista de sublistas
        com pecas na forma de inteiro

    :param tup: (tuple) Tabuleiro na forma de tuplo
    :return: (list) Tabuleiro na representacao escolhida neste caso lista
    """
    return list(map(list, tup))


def obter_ganhador(tab):
    """ Funcao de alto nivel que permite obter o jogadore ganhadore num tabuleiro de jog do moinho, isto e o jogador
        que tiver 3 pecas em linha horizontal ou verticalmente

    :param tab: (list) Tabuleiro (aceita qualquer representacao)
    :return: peca que representa o jogador que tem uma combinacao ganhadora
    """
    ganhador = ((cria_peca('O'), cria_peca('O'), cria_peca('O')), (cria_peca('X'), cria_peca('X'), cria_peca('X')))  #
    # tuplo com tuplos correspondentes a um obter_vetor ganhador
    res = [win for win in ganhador for i in range(1, 4) if obter_vetor(tab, str(i)) == win
           or obter_vetor(tab, chr(ord('a') + (i - 1))) == win]  # lista de tuplos ganhadores obtidos atraves da funcao
    # obter_vetor sendo que ao iterar sobre o range(1,4) para alem das linhas 1,2 e 3 se subtrairmos 1 a i e somarmos ao
    #  ord de a conseguimos obter as 3 colunas a,b e c
    return res[0][0] if res else cria_peca(' ')


def obter_posicoes_livres(tab):
    """ Funcao de alto nivel para obter as posicoes livres num tabuleiro

    :param tab: (list) Tabuleiro (aceita qualquer representacao)
    :return: (tuple) tuplo com as posicoes livres
    """
    valores_posiveis_c = ('a', 'b', 'c')
    valores_posiveis_l = ('1', '2', '3')
    return tuple(cria_posicao(c, l) for l in valores_posiveis_l for c in valores_posiveis_c if
                 eh_posicao_livre(tab, cria_posicao(c, l)))


def obter_posicoes_jogador(tab, jog):
    """ Funcao de alto nivel para obter as posicoes de um jogador num tabuleiro

    :param tab: (list) Tabuleiro (aceita qualquer representacao)
    :param jog: (int) peca que representa o jogador (aceita qualquer representacao)
    :return: (tuple) tuplo com as posicoes ocupadas pelo jogador
    """
    valores_posiveis_c = ('a', 'b', 'c')
    valores_posiveis_l = ('1', '2', '3')
    return tuple(cria_posicao(c, l) for l in valores_posiveis_l for c in valores_posiveis_c if
                 pecas_iguais(obter_peca(tab, cria_posicao(c, l)), jog))


#  2.2 Funcoes adicionais
def block(tab, jog):
    """ Funcao auxiliar para verificar se todas as pecas do jogador estao bloqueadas por pecas adversarias

    :param tab: (list) Tabuleiro (aceita qualquer representacao)
    :param jog: (int) peca que representa o jogador (aceita qualquer representacao)
    :return:  (bool) True se todas as pecas estiverem bloqueadas e False caso contrario
    """
    return not [pos_adj for pos in obter_posicoes_jogador(tab, jog) for pos_adj in obter_posicoes_adjacentes(pos)
                if eh_posicao_livre(tab, pos_adj)] and n_pecas_jog(tab, jog) != 0


def obter_movimento_manual(tab, jog):
    """ Funcao adicional de alto nivel que permite ao utilizador fazer o input da posicao onde quer colocar uma peca
        ou do movimento que quer efetuar

    :param tab: (list) Tabuleiro (aceita qualquer representacao)
    :param jog: (int) peca que representa o jogador (aceita qualquer representacao)
    :return: (tuple) tuplo com a posicao de colocacao ou com as posicoes de movimento
    """
    valores_posiveis_c = ('a', 'b', 'c')
    valores_posiveis_l = ('1', '2', '3')
    pos_possiveis = [posicao_para_str(cria_posicao(c, l)) for l in valores_posiveis_l for c in valores_posiveis_c]
    if n_pecas_jog(tab, jog) < 3:
        pos = input('Turno do jogador. Escolha uma posicao: ')  # input na fase de colocacao
        if pos not in pos_possiveis or not eh_posicao_livre(tab, cria_posicao(pos[0], pos[1])):
            raise ValueError('obter_movimento_manual: escolha invalida')
        return cria_posicao(pos[0], pos[1]),
    mov = input('Turno do jogador. Escolha um movimento: ')  # imput na fase de movimento
    if len(mov) < 4 or mov[:2] not in pos_possiveis or mov[2:] not in pos_possiveis:
        raise ValueError('obter_movimento_manual: escolha invalida')
    mov_1 = cria_posicao(mov[:2][0], mov[:2][1])
    mov_2 = cria_posicao(mov[2:][0], mov[2:][1])
    if (obter_peca(tab, mov_1) != jog or obter_peca(tab, mov_2) not in (
            cria_peca(' '), jog)) or mov_2 not in obter_posicoes_adjacentes(mov_1) + (mov_1,) or (
            mov_2 == mov_1 and not block(tab, jog)) or (pecas_iguais(obter_peca(tab, mov_2), jog) and not
    posicoes_iguais(mov_1, mov_2)):  # verificacoes de movimentos validos (posicao de chegada e adjacente e livre se
        # nao houver bloqueio ou pertence ao jogador e e a mesma que a de partida se houver;
        # posicao de partida contem a peca do jogador
        raise ValueError('obter_movimento_manual: escolha invalida')
    return cria_posicao(mov[0], mov[1]), cria_posicao(mov[2], mov[3])


def auto_coloc(tab, jog):
    """ Funcao auxiliar para correr o algoritmo de colocacao automatica do jogo do moinho

    :param tab: (list) Tabuleiro (aceita qualquer representacao)
    :param jog: (int) peca que representa o jogador (aceita qualquer representacao)
    :return: (int) posicao na representacao escolhida de acordo com o seguinte algoritmo:
    1. Se o jogador tiver duas das suas pecas em linha e uma posicao livre entao deve marcar na posicao livre
    2. Se o adversario tiver duas das suas pecas em linha e uma posicao livre entao deve marcar na posicao livre
    3. Se a posicao central estiver livre entao jogar na posicao central
    4. Se um canto for uma posicao livre entao jogar nesse canto
    5. Se uma posicao lateral (que nem e o centro, nem um canto) for livre entao jogar nesse lateral
    """
    pos_livres = [pos for pos in obter_posicoes_livres(tab)]
    adv = inteiro_para_peca(-peca_para_inteiro(jog))
    centro = cria_posicao('b', '2')
    cantos = {'Canto1': cria_posicao('a', '1'), 'Canto2': cria_posicao('c', '1'),
              'Canto3': cria_posicao('a', '3'), 'Canto4': cria_posicao('c', '3')}
    laterais = {'lat1': cria_posicao('b', '1'), 'lat2': cria_posicao('a', '2'),
                'lat3': cria_posicao('c', '2'), 'lat4': cria_posicao('b', '3')}
    for pos in pos_livres:
        if pecas_iguais(obter_ganhador(coloca_peca(cria_copia_tabuleiro(tab), jog, pos)), jog):  # verificar se ao
            # colocar uma peca numa posicao livre o jogador e ganhador
            return pos
    for pos in pos_livres:
        if pecas_iguais(obter_ganhador(coloca_peca(cria_copia_tabuleiro(tab), adv, pos)), adv):  # verificar se ao
            # colocar uma peca numa posicao livre o adversario e ganhador e deve ser bloqueado
            return pos
    if centro in pos_livres:
        return centro
    for canto in sorted(cantos.keys()):
        if cantos[canto] in pos_livres:
            return cantos[canto]
    for lat in sorted(laterais.keys()):
        if laterais[lat] in pos_livres:
            return lat


def minimax(tab, jog, prof, seq_mov):
    """ Funcao auxiliar que executa o algoritmo minimax

    :param tab: (list) Tabuleiro (aceita qualquer representacao)
    :param jog: (int) peca que representa o jogador (aceita qualquer representacao)
    :param prof: (int) profundidade pretendida para a recursao do algoritmo
    :param seq_mov: (tuple) inicializar a sequencia com () para que possa ser depois utilizada com mais movimentos
                            durante a recursao
    :return: (tuple) tuplo com o melhor resultado na forma de peca e com a melhor sequencia de movimentos na forma de
                     posicoes
    """
    adv = inteiro_para_peca(-peca_para_inteiro(jog))
    melhor_seq_mov = ()
    if not pecas_iguais(obter_ganhador(tab), cria_peca(' ')) or prof == 0:
        return obter_ganhador(tab), seq_mov
    else:
        melhor_res = adv
        for pos in obter_posicoes_jogador(tab, jog):
            for pos_adj in obter_posicoes_adjacentes(pos):
                if eh_posicao_livre(tab, pos_adj):
                    novo_tab = move_peca(cria_copia_tabuleiro(tab), pos, pos_adj)
                    novo_res, nova_seq_mov = minimax(novo_tab, adv, prof - 1, seq_mov + (pos, pos_adj))
                    if not melhor_seq_mov or (
                            pecas_iguais(jog, cria_peca('X')) and peca_para_inteiro(novo_res) > peca_para_inteiro(
                            melhor_res)) or \
                            (pecas_iguais(jog, cria_peca('O')) and peca_para_inteiro(novo_res) < peca_para_inteiro(
                                melhor_res)):
                        melhor_res, melhor_seq_mov = novo_res, nova_seq_mov
        return melhor_res, melhor_seq_mov


def obter_movimento_auto(tab, jog, dif):
    """ Funcao de alto nivel que permite ao computador jogar de acordo com a dificuldade

    :param tab: (list) Tabuleiro (aceita qualquer representacao)
    :param jog: (int) peca que representa o jogador (aceita qualquer representacao)
    :param dif: (str) dificuldade do jogo (facil, normal, dificil)
    :return: (tuple) tuplo com a peca a colocar ou com o movimento a realizar
    """
    if n_pecas_jog(tab, jog) < 3:
        return auto_coloc(tab, jog),
    if block(tab, jog):
        return obter_posicoes_jogador(tab, jog)[0], obter_posicoes_jogador(tab, jog)[0]  # se todas as pecas estiverem
    # bloqueadas e devolvido movimento da primeira peca do jogador para ela propria(saltando o turno)
    if dif == 'facil' or (dif == 'normal' and pecas_iguais(minimax(tab, jog, 1, ())[0], cria_peca(' '))):
        for pos in obter_posicoes_jogador(tab, jog):
            for pos_adj in obter_posicoes_adjacentes(pos):
                if eh_posicao_livre(tab, pos_adj):
                    return pos, pos_adj
    if dif == 'normal':
        return minimax(tab, jog, 1, ())[1]
    if dif == 'dificil':
        return minimax(tab, jog, 5, ())[1][:2]


def moinho(jog, dif):
    """ Funcao de alto nivel de interface para ser jogado o jogo do moinho na consola de python

    :param jog: (int) peca que representa o jogador (aceita qualquer representacao)
    :param dif: (str) dificuldade do jogo (facil, normal, dificil)
    :return: (str) vencedor do jogo
    INFO: E de frisar que embora o return seja apenas o vencedor, esta funcao imprime no ecra uma mensagem de
          boas-vindas, o tabuleiro com as posicoes marcadas e uma mensagem a indicar o turno em vigor e o nivel de jogo.
    """
    if jog not in ('[X]', '[O]') or dif not in ('facil', 'normal', 'dificil'):
        raise ValueError('moinho: argumentos invalidos')
    tab, res = cria_tabuleiro(), cria_peca(' ')
    jog = cria_peca('X') if jog == '[X]' else cria_peca('O')
    adv = inteiro_para_peca(-peca_para_inteiro(jog))
    turno = -1 if pecas_iguais(jog, cria_peca('O')) else 1  # os turnos permitem controlar a ordem de movimentos(auto ou
    # manual)
    print('Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade {}.'.format(dif))
    print(tabuleiro_para_str(tab))
    while pecas_iguais(res, cria_peca(' ')):
        if turno == 1:
            mov = obter_movimento_manual(tab, jog)
            tab = coloca_peca(tab, jog, mov[0]) if len(obter_posicoes_jogador(tab, jog)) \
                                                   < 3 else move_peca(tab, mov[0], mov[1])
            res = obter_ganhador(tab)
            print(tabuleiro_para_str(tab))
            turno *= -1
        else:
            print('Turno do computador ({}):'.format(dif))
            mov = obter_movimento_auto(tab, adv, dif)
            tab = coloca_peca(tab, adv, mov[0]) if len(obter_posicoes_jogador(tab, adv)) < 3 else move_peca(tab, mov[0],
                                                                                                            mov[1])
            turno *= -1
            res = obter_ganhador(tab)
            print(tabuleiro_para_str(tab))
    return peca_para_str(res)
