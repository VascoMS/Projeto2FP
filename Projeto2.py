# VASCO SILVA IST199132

def cria_posicao(c, l):
    valores_possiveis_l = ('1', '2', '3')
    valores_possiveis_c = ('a', 'b', 'c')
    if l not in valores_possiveis_l or c not in valores_possiveis_c:
        raise ValueError('cria_posicao: argumentos invalidos')
    return [c, l]


def cria_copia_posicao(p):
    return p.copy()


def obter_pos_c(p):
    return p[0]


def obter_pos_l(p):
    return p[1]


def eh_posicao(arg):
    valores_possiveis_l = ('1', '2', '3')
    valores_possiveis_c = ('a', 'b', 'c')
    return type(arg) == list and len(arg) == 2 and obter_pos_c(arg) in valores_possiveis_c and obter_pos_l(arg) \
           in valores_possiveis_l


def posicoes_iguais(p1, p2):
    return eh_posicao(p1) and eh_posicao(p2) and p1 == p2


def posicao_para_str(p):
    return obter_pos_c(p) + obter_pos_l(p)


def pos_coordenadas(pos):
    """ Funcao auxiliar de obtencao de coordenadas(index da posicao na linha e index da linha de uma posicao num tuplo)
        de um posicao especificada

    Parametros:

    pos(int): posicao no tabuleiro.

    Returns:

    tup: coordenadas da posicao especificada.

    """
    pos_dic = {'a1': (0, 0), 'b1': (1, 0), 'c1': (2, 0), 'a2': (0, 1), 'b2': (1, 1), 'c2': (2, 1), 'a3': (0, 2),
               'b3': (1, 2), 'c3': (2, 2)}
    return pos_dic[posicao_para_str(pos)]


def obter_posicoes_adjacentes(p):
    valores_posiveis_c = ('a', 'b', 'c')
    valores_posiveis_l = ('1', '2', '3')
    pos_possiveis = [cria_posicao(c, l) for l in valores_posiveis_l for c in valores_posiveis_c]
    res_validos = ((1, 0), (0, 1), (-1, 0), (0, -1))  # as posicoes adjacentes a uma posicao podem ser obtidas
    res_validos_diag = ((1, 1), (-1, -1), (1, -1), (-1, 1))
    valores_com_diag = (cria_posicao('a', '1'), cria_posicao('c', '1'), cria_posicao('a', '3'), cria_posicao('c', '3'),
                        cria_posicao('b', '2'))
    # subtraindo o ord da coluna e o valor da linha a posicao argumento, e essa conta tem de originar um dos
    # resultados deste tuplo
    return tuple(i for i in pos_possiveis if ((ord(obter_pos_c(p)) - ord(obter_pos_c(i)), int(obter_pos_l(p)) -
                                               int(obter_pos_l(i))) in res_validos) or (i in valores_com_diag and
                                                                                        (ord(obter_pos_c(p)) - ord(
                                                                                            obter_pos_c(i)),
                                                                                         int(obter_pos_l(p)) -
                                                                                         int(obter_pos_l(
                                                                                             i))) in res_validos_diag))


def cria_peca(peca):
    pecas = {'X': 1, 'O': -1, ' ': 0}
    if type(peca) != str or peca not in pecas.keys():
        raise ValueError('cria_peca: argumento invalido')
    return pecas[peca]


def cria_copia_peca(peca):
    return int(peca)


def eh_peca(arg):
    pecas = (1, -1, 0)
    return type(arg) == int and arg in pecas


def pecas_iguais(p1, p2):
    return p1 == p2 and type(p1) == int and type(p2) == int


def peca_para_str(peca):
    dic = {1: 'X', -1: 'O', 0: ' '}
    return '[{}]'.format(dic[peca])


def peca_para_inteiro(peca):
    return 1 if peca_para_str(peca) == '[X]' else (-1 if peca_para_str(peca) == '[O]' else 0)


def inteiro_para_peca(inteiro):
    dic_pecas = {1: cria_peca('X'), -1: cria_peca('O'), 0: cria_peca(' ')}
    return dic_pecas[inteiro]


def cria_tabuleiro():
    return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def cria_copia_tabuleiro(tab):
    return [linha.copy() for linha in tab]


def obter_peca(tab, pos):
    coordenadas = pos_coordenadas(posicao_para_str(pos))
    return tab[coordenadas[1]][coordenadas[0]]


def obter_vetor(tab, conjunto):
    valores_possiveis_l = ('1', '2', '3')
    col = ()
    if conjunto in valores_possiveis_l:
        return tuple(peca for peca in tab[int(conjunto) - 1])
    for linha in range(len(tab)):
        col += (tab[linha][ord(conjunto) - ord('a')],)
    return tuple(peca for peca in col)


def coloca_peca(tab, peca, pos):
    coordenadas = pos_coordenadas(posicao_para_str(cria_posicao(obter_pos_c(pos), obter_pos_l(pos))))
    tab[coordenadas[1]][coordenadas[0]] = peca
    return tab


def remove_peca(tab, pos):
    coordenadas = pos_coordenadas(posicao_para_str(pos))
    tab[coordenadas[1]][coordenadas[0]] = cria_peca(' ')
    return tab


def move_peca(tab, p1, p2):
    peca = obter_peca(tab, p1)
    return coloca_peca(remove_peca(tab, p1), peca, p2)


def jogadores_ganhadores(tab):
    dic_ganhador = {-1: (cria_peca('O'), cria_peca('O'), cria_peca('O')),
                    1: (cria_peca('X'), cria_peca('X'), cria_peca('X'))}
    return [key for key in dic_ganhador for i in range(1, 4) if obter_vetor(tab, str(i)) == dic_ganhador[key]
            or obter_vetor(tab, chr(ord('a') + (i - 1))) == dic_ganhador[key]]


def n_pecas_jog(tab, jog):
    valores_posiveis_c = ('a', 'b', 'c')
    valores_posiveis_l = ('1', '2', '3')
    pos_possiveis = [cria_posicao(c, l) for l in valores_posiveis_l for c in valores_posiveis_c]
    res = 0
    for i in pos_possiveis:
        res += 1 if (pecas_iguais(obter_peca(tab, i), jog)) else 0
    return res


def eh_tabuleiro(tab):
    """ Funcao de verificacao da validade da representacao de um tabuleiro 3x3

    Parametros:

    tab: Argumento de qualquer tipo.

    Returns:

    True: Se o tab for um tuplo com tres subtuplos onde os seus valores
          sao -1, 0 ou 1, constituindo um tabuleiro valido.
    False: Se o tab nao respeitar alguma das condicoes referidas acima,
           nao constituindo um tabuleiro valido.
    """
    valores_posiveis = (cria_peca('O'), cria_peca('X'), cria_peca(' '))
    n_pecas = [n_pecas_jog(tab, jog) for jog in valores_posiveis[:2]]
    dif_pecas = [abs(len([j for i in tab for j in i if j == cria_peca('X')]) - len(
        [j for i in tab for j in i if j == cria_peca('O')])) <= 1]
    res = [type(tab) == list and len(tab) == 3] + [
        type(linha) == list and len(linha) == 3 and type(valor) == int and valor in valores_posiveis for linha in tab
        for valor in linha] + [len(jogadores_ganhadores(tab)) <= 1] + dif_pecas + [i <= 3 for i in n_pecas]
    return False not in res


def eh_posicao_livre(tab, pos):
    return pecas_iguais(obter_peca(tab, pos), cria_peca(' '))


def tabuleiros_iguais(t1, t2):
    return t1 == t2 and eh_tabuleiro(t1) and eh_tabuleiro(t2)


def tabuleiro_para_str(tab):
    return '   a   b   c\n1 {}-{}-{}\n   | \\ | / |\n2 {}-{}-{}\n   | / | \\ |\n3 {}-{}-{}'.format(
        peca_para_str(obter_peca(tab, cria_posicao('a', '1'))),
        peca_para_str(obter_peca(tab, cria_posicao('b', '1'))), peca_para_str(obter_peca(tab, cria_posicao('c', '1'))),
        peca_para_str(obter_peca(tab, cria_posicao('a', '2'))), peca_para_str(obter_peca(tab, cria_posicao('b', '2'))),
        peca_para_str(obter_peca(tab, cria_posicao('c', '2'))),
        peca_para_str(obter_peca(tab, cria_posicao('a', '3'))), peca_para_str(obter_peca(tab, cria_posicao('b', '3'))),
        peca_para_str(obter_peca(tab, cria_posicao('c', '3'))))


def tuplo_para_tabuleiro(tup):
    return list(map(list, tup))


def obter_ganhador(tab):
    dic_ganhador = {cria_peca('O'): (cria_peca('O'), cria_peca('O'), cria_peca('O')),
                    cria_peca('X'): (cria_peca('X'), cria_peca('X'), cria_peca('X'))}
    res = [key for key in dic_ganhador for i in range(1, 4) if obter_vetor(tab, str(i)) == dic_ganhador[key]
           or obter_vetor(tab, chr(ord('a') + (i - 1))) == dic_ganhador[key]]
    return res[0] if res else cria_peca(' ')


def obter_posicoes_livres(tab):
    valores_posiveis_c = ('a', 'b', 'c')
    valores_posiveis_l = ('1', '2', '3')
    return tuple(cria_posicao(c, l) for l in valores_posiveis_l for c in valores_posiveis_c if
                 eh_posicao_livre(tab, cria_posicao(c, l)))


def obter_posicoes_jogador(tab, jog):
    valores_posiveis_c = ('a', 'b', 'c')
    valores_posiveis_l = ('1', '2', '3')
    return tuple(cria_posicao(c, l) for l in valores_posiveis_l for c in valores_posiveis_c if
                 pecas_iguais(obter_peca(tab, cria_posicao(c, l)), jog))


#  2.2 Funcoes adicionais
def block(tab, jog):
    return not [pos_adj for pos in obter_posicoes_jogador(tab, jog) for pos_adj in obter_posicoes_adjacentes(pos)
                if eh_posicao_livre(tab, pos_adj)] and n_pecas_jog(tab, jog) != 0


def obter_movimento_manual(tab, jog):
    valores_posiveis_c = ('a', 'b', 'c')
    valores_posiveis_l = ('1', '2', '3')
    pos_possiveis = [posicao_para_str(cria_posicao(c, l)) for l in valores_posiveis_l for c in valores_posiveis_c]
    if n_pecas_jog(tab, jog) < 3:
        pos = input('Turno do jogador. Escolha uma posicao: ')
        if pos not in pos_possiveis or not eh_posicao_livre(tab, pos):
            raise ValueError('obter_movimento_manual: escolha invalida')
        return cria_posicao(obter_pos_c(pos), obter_pos_l(pos)),
    mov = input('Turno do jogador. Escolha um movimento: ')
    if mov[:2] not in pos_possiveis or mov[2:] not in pos_possiveis or \
            (obter_peca(tab, cria_posicao(mov[:2][0], mov[:2][1])) != jog or
             obter_peca(tab, cria_posicao(mov[2:][0], mov[2:][1])) not in (
                     cria_peca(' '), jog)) or cria_posicao(mov[2:][0], mov[2:][1]) not in obter_posicoes_adjacentes(
        cria_posicao(mov[:2][0], mov[:2][1])) + (cria_posicao(mov[:2][0], mov[:2][1]),) or (
            cria_posicao(mov[2:][0], mov[2:][1]) == cria_posicao(mov[:2][0], mov[:2][1]) and not block(tab, jog)):
        raise ValueError('obter_movimento_manual: escolha invalida')
    return cria_posicao(obter_pos_c(mov[:2]), obter_pos_l(mov[:2])), cria_posicao(obter_pos_c(mov[2:]),
                                                                                  obter_pos_l(mov[2:]))


def auto_coloc(tab, jog):
    pos_livres = [pos for pos in obter_posicoes_livres(tab)]
    adv = inteiro_para_peca(-peca_para_inteiro(jog))
    centro = cria_posicao('b', '2')
    cantos = {'Canto1': cria_posicao('a', '1'), 'Canto2': cria_posicao('c', '1'),
              'Canto3': cria_posicao('a', '3'), 'Canto4': cria_posicao('c', '3')}
    laterais = {'lat1': cria_posicao('b', '1'), 'lat2': cria_posicao('a', '2'),
                'lat3': cria_posicao('c', '2'), 'lat4': cria_posicao('b', '3')}
    for pos in pos_livres:
        if pecas_iguais(obter_ganhador(coloca_peca(cria_copia_tabuleiro(tab), jog, pos)), jog):
            return pos
    for pos in pos_livres:
        if pecas_iguais(obter_ganhador(coloca_peca(cria_copia_tabuleiro(tab), adv, pos)), adv):
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
    adv = inteiro_para_peca(-peca_para_inteiro(jog))
    melhor_seq_mov = ()
    if not pecas_iguais(obter_ganhador(tab), cria_peca(' ')) or prof == 0:
        return peca_para_inteiro(obter_ganhador(tab)), seq_mov
    else:
        melhor_res = adv
        for pos in obter_posicoes_jogador(tab, jog):
            for pos_adj in obter_posicoes_adjacentes(pos):
                if eh_posicao_livre(tab, pos_adj):
                    novo_tab = move_peca(cria_copia_tabuleiro(tab), pos, pos_adj)
                    novo_res, nova_seq_mov = minimax(novo_tab, adv, prof - 1, seq_mov + ((pos, pos_adj)))
                    if not melhor_seq_mov or (pecas_iguais(jog, cria_peca('X')) and novo_res > melhor_res) or \
                            (pecas_iguais(jog, cria_peca('O')) and novo_res < melhor_res):
                        melhor_res, melhor_seq_mov = novo_res, nova_seq_mov
        return melhor_res, melhor_seq_mov


def obter_movimento_auto(tab, jog, dif):
    if n_pecas_jog(tab, jog) < 3:
        return auto_coloc(tab, jog),
    if block(tab, jog):
        return obter_posicoes_jogador(tab, jog)[0], obter_posicoes_jogador(tab, jog)[0]
    if dif == 'facil' or (dif == 'normal' and minimax(tab, jog, 1, ())[0] == peca_para_inteiro(cria_peca(' '))):
        for pos in obter_posicoes_jogador(tab, jog):
            for pos_adj in obter_posicoes_adjacentes(pos):
                if eh_posicao_livre(tab, pos_adj):
                    return pos, pos_adj
    if dif == 'normal':
        return minimax(tab, jog, 1, ())[1]
    if dif == 'dificil':
        return minimax(tab, jog, 5, ())[1][:2]


def moinho(jog, dif):
    dic_peca = {'[X]': cria_peca('X'), '[O]': cria_peca('O')}
    niveis = ('facil', 'normal', 'dificil')
    if type(jog) != str or type(dif) != str or jog not in dic_peca or dif not in niveis:
        raise ValueError('moinho: argumentos invalidos')
    tab = cria_tabuleiro()
    jog = dic_peca[jog]
    res = cria_peca(' ')
    adv = inteiro_para_peca(-peca_para_inteiro(jog))
    print('Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade {}.'.format(dif))
    print(tabuleiro_para_str(tab))
    if pecas_iguais(jog, '[O]'):
        while pecas_iguais(res, cria_peca(' ')):
            print('Turno do computador ({}):'.format(dif))
            if len(obter_posicoes_jogador(tab, adv)) < 3:
                tab = coloca_peca(tab, adv, obter_movimento_auto(tab, adv, dif)[0])
            else:
                mov = obter_movimento_auto(tab, adv, dif)
                tab = move_peca(tab, mov[0], mov[1])
            res = obter_ganhador(tab)
            print(tabuleiro_para_str(tab))
            if not pecas_iguais(res, cria_peca(' ')):
                break
            if len(obter_posicoes_jogador(tab, jog)) < 3:
                tab = coloca_peca(tab, jog, obter_movimento_manual(tab, jog)[0])
            else:
                mov = obter_movimento_manual(tab, jog)
                tab = move_peca(tab, mov[0], mov[1])
            res = obter_ganhador(tab)
            print(tabuleiro_para_str(tab))
    else:
        while pecas_iguais(res, cria_peca(' ')):
            if len(obter_posicoes_jogador(tab, adv)) < 3:
                tab = coloca_peca(tab, jog, obter_movimento_manual(tab, jog)[0])
            else:
                mov = obter_movimento_manual(tab, jog)
                tab = move_peca(tab, mov[0], mov[1])
            res = obter_ganhador(tab)
            print(tabuleiro_para_str(tab))
            if not pecas_iguais(res, cria_peca(' ')):
                break
            print('Turno do computador ({}):'.format(dif))
            if len(obter_posicoes_jogador(tab, adv)) < 3:
                tab = coloca_peca(tab, adv, obter_movimento_auto(tab, adv, dif)[0])
            else:
                mov = obter_movimento_auto(tab, adv, dif)
                tab = move_peca(tab, mov[0], mov[1])
            res = obter_ganhador(tab)
            print(tabuleiro_para_str(tab))
    return peca_para_str(res)
