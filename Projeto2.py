# VASCO SILVA IST199132
def cria_posicao(c, l):
    valores_possiveis_l = ('1', '2', '3')
    valores_possiveis_c = ('a', 'b', 'c')
    if l not in valores_possiveis_l or c not in valores_possiveis_c:
        raise ValueError('cria posicao: argumentos invalidos')
    return [c, l]


def cria_copia_posicao(p):
    return p


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
    # subtraindo o ord da coluna e o valor da linha a posicao argumento, e essa conta tem de originar um dos
    # reultados deste tuplo
    return tuple(i for i in pos_possiveis if (ord(obter_pos_c(p)) - ord(obter_pos_c(i)), int(obter_pos_l(p)) -
                                              int(obter_pos_l(i))) in res_validos)


def cria_peca(peca):
    pecas = ('X', 'O', ' ')
    if peca not in pecas:
        raise ValueError('cria peca: argumento invalido')
    return peca


def cria_copia_peca(peca):
    return peca


def eh_peca(arg):
    pecas = ('X', 'O', ' ')
    return type(arg) == str and arg in pecas


def pecas_iguais(p1, p2):
    return p1 == p2


def peca_para_str(peca):
    return '[{}]'.format(peca)


def peca_para_inteiro(peca):
    return 1 if peca_para_str(peca) == '[X]' else (-1 if peca_para_str(peca) == '[O]' else 0)


def inteiro_para_peca(peca):
    dic_pecas = {1: 'X', -1: 'O', 0: ' '}
    return dic_pecas[peca]


def cria_tabuleiro():
    return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def cria_copia_tabuleiro(tab):
    return tab


def obter_peca(tab, pos):
    coordenadas = pos_coordenadas(posicao_para_str(pos))
    return inteiro_para_peca(tab[coordenadas[1]][coordenadas[0]])


def obter_vetor(tab, conjunto):
    valores_possiveis_l = ('1', '2', '3')
    col = ()
    if conjunto in valores_possiveis_l:
        return tuple(inteiro_para_peca(peca) for peca in tab[int(conjunto) - 1])
    for linha in range(len(tab)):
        col += (tab[linha][ord(conjunto) - ord('a')],)
    return tuple(inteiro_para_peca(peca) for peca in col)


def obter_vetor_int(tab, conjunto):
    return tuple(peca_para_inteiro(peca) for peca in obter_vetor(tab, conjunto))


def coloca_peca(tab, peca, pos):
    coordenadas = pos_coordenadas(posicao_para_str(cria_posicao(obter_pos_c(pos), obter_pos_l(pos))))
    tab[coordenadas[1]][coordenadas[0]] = peca_para_inteiro(cria_peca(peca))
    return tab


def remove_peca(tab, pos):
    coordenadas = pos_coordenadas(posicao_para_str(pos))
    tab[coordenadas[1]][coordenadas[0]] = peca_para_inteiro(cria_peca(' '))
    return tab


def move_peca(tab, p1, p2):
    peca = obter_peca(tab, p1)
    return coloca_peca(remove_peca(tab, p1), peca, p2)


def jogadores_ganhadores(tab):
    dic_ganhador = {-1: (-1, -1, -1), 1: (1, 1, 1)}
    return [key for key in dic_ganhador for i in range(1, 4) if obter_vetor_int(tab, str(i)) == dic_ganhador[key]
            or obter_vetor_int(tab, chr(ord('a') + (i - 1))) == dic_ganhador[key]]


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
    valores_posiveis = (-1, 0, 1)
    n_pecas = [len([j for i in tab for j in i if j == 1]) - len([j for i in tab for j in i if j == -1]) < 1]
    res = [type(tab) == list and len(tab) == 3] + [
        type(linha) == list and len(linha) == 3 and type(valor) == int and valor
        in valores_posiveis for linha in tab for valor in linha] + [len(jogadores_ganhadores(tab)) < 1] + n_pecas
    return False not in res


def eh_posicao_livre(tab, pos):
    return peca_para_inteiro(obter_peca(tab, pos)) == peca_para_inteiro(cria_peca(' '))


def tabuleiros_iguais(t1, t2):
    return t1 == t2


def n_pecas_jog(tab, jog):
    valores_posiveis_c = ('a', 'b', 'c')
    valores_posiveis_l = ('1', '2', '3')
    pos_possiveis = [cria_posicao(c, l) for l in valores_posiveis_l for c in valores_posiveis_c]
    res = 0
    for i in pos_possiveis:
        res += 1 if obter_peca(tab, i) == cria_peca(jog) else 0
    return res


def tabuleiro_para_str(tab):
    return '   a   b   c\n1 [{}]-[{}]-[{}]\n   | \\ | / |\n2 [{}]-[{}]-[{}]\n   | / | \\ |\n3 [{}]-[{}]-[{}]'.format(
        obter_peca(tab, cria_posicao('a', '1')),
        obter_peca(tab, cria_posicao('b', '1')), obter_peca(tab, cria_posicao('c', '1')),
        obter_peca(tab, cria_posicao('a', '2')), obter_peca(tab, cria_posicao('b', '2')),
        obter_peca(tab, cria_posicao('c', '2')),
        obter_peca(tab, cria_posicao('a', '3')), obter_peca(tab, cria_posicao('b', '3')),
        obter_peca(tab, cria_posicao('c', '3')))


def tuplo_para_tabuleiro(tup):
    return list(map(list, tup))


def obter_ganhador(tab):
    dic_ganhador = {-1: (-1, -1, -1), 1: (1, 1, 1)}
    res = [key for key in dic_ganhador for i in range(1, 4) if obter_vetor_int(tab, str(i)) == dic_ganhador[key]
           or obter_vetor_int(tab, chr(ord('a') + (i - 1))) == dic_ganhador[key]]
    return inteiro_para_peca(res[0]) if res else cria_peca(' ')


def obter_posicoes_livres(tab):
    valores_posiveis_c = ('a', 'b', 'c')
    valores_posiveis_l = ('1', '2', '3')
    return tuple(cria_posicao(c, l) for l in valores_posiveis_l for c in valores_posiveis_c if
                 eh_posicao_livre(tab, cria_posicao(c, l)))


def obter_posicoes_jogador(tab, jog):
    valores_posiveis_c = ('a', 'b', 'c')
    valores_posiveis_l = ('1', '2', '3')
    return tuple(cria_posicao(c, l) for l in valores_posiveis_l for c in valores_posiveis_c if
                 peca_para_inteiro(obter_peca(tab, cria_posicao(c, l))) == peca_para_inteiro(cria_peca(jog)))


#  2.2 Funcoes adicionais

def obter_movimento_manual(tab, jog):
    valores_posiveis_c = ('a', 'b', 'c')
    valores_posiveis_l = ('1', '2', '3')
    pos_possiveis = [posicao_para_str(cria_posicao(c, l)) for l in valores_posiveis_l for c in valores_posiveis_c]
    if n_pecas_jog(tab, jog) < 3:
        pos = input('Turno do jogador. Escolha uma posicao: ')
        if pos not in pos_possiveis or not eh_posicao_livre(tab, pos):
            raise ValueError('obter movimento manual: escolha invalida')
        return cria_posicao(obter_pos_c(pos), obter_pos_l(pos)),
    mov = input('Turno do jogador. Escolha um movimento: ')
    if (obter_peca(tab, cria_posicao(obter_pos_c(mov[:2]), obter_pos_l(mov[:2]))) != cria_peca(jog) or
        obter_peca(tab, cria_posicao(obter_pos_c(mov[2:]), obter_pos_l(mov[2:]))) not in (
                cria_peca(' '), cria_peca(jog))) or mov[:2] not in pos_possiveis or mov[2:] not in pos_possiveis:
        raise ValueError('obter movimento manual: escolha invalida')
    return cria_posicao(obter_pos_c(mov[:2]), obter_pos_l(mov[:2])), cria_posicao(obter_pos_c(mov[2:]),
                                                                                  obter_pos_l(mov[2:]))


def auto_coloc(tab, jog):
    pos_livres = [posicao_para_str(pos) for pos in obter_posicoes_livres(tab)]
    adv = inteiro_para_peca(-peca_para_inteiro(jog))
    centro = posicao_para_str(cria_posicao('b', '2'))
    cantos = {'Canto1': posicao_para_str(cria_posicao('a', '1')), 'Canto2': posicao_para_str(cria_posicao('c', '1')),
              'Canto3': posicao_para_str(cria_posicao('a', '3')), 'Canto4': posicao_para_str(cria_posicao('c', '3'))}
    laterais = {'lat1': posicao_para_str(cria_posicao('b', '1')), 'lat2': posicao_para_str(cria_posicao('a', '2')),
                'lat3': posicao_para_str(cria_posicao('c', '2')), 'lat4': posicao_para_str(cria_posicao('b', '3'))}
    for pos in pos_livres:
        if obter_ganhador(coloca_peca(tab, cria_peca(jog), pos)) == peca_para_str(cria_peca(jog)):
            return pos
        elif obter_ganhador(coloca_peca(tab, adv, pos)) == peca_para_str(cria_peca(adv)):
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
    if obter_ganhador(tab) != cria_peca(' ') or prof == 0:
        return peca_para_inteiro(obter_ganhador(tab)), seq_mov
    else:
        melhor_res = peca_para_inteiro(adv)
        for pos in obter_posicoes_jogador(tab, jog):
            for pos_adj in obter_posicoes_adjacentes(pos):
                if eh_posicao_livre(tab, pos_adj):
                    novo_tab = move_peca(cria_copia_tabuleiro(tab), pos, pos_adj)
                    novo_res, nova_seq_mov = minimax(novo_tab, adv, prof - 1, seq_mov + ((pos, pos_adj)))
                    if not melhor_seq_mov or (jog == cria_peca('X') and novo_res > melhor_res) or (jog == cria_peca('O') and novo_res < melhor_res):
                        melhor_res, melhor_seq_mov = novo_res, nova_seq_mov
        return melhor_res, melhor_seq_mov


def obter_movimento_auto(tab, jog, dif):
    if n_pecas_jog(tab, jog) < 3:
        return auto_coloc(tab, jog),
    if dif == 'facil' or minimax(tab, jog, 1, ())[0] == peca_para_inteiro(cria_peca(' ')):
        for pos in obter_posicoes_jogador(tab, jog):
            if len(obter_posicoes_adjacentes(pos)) > 0:
                return pos, obter_posicoes_adjacentes(pos)[0]
    if dif == 'normal':
        print(minimax(tab, jog, 1, ()))
        return minimax(tab, jog, 1, ())[1][1]
    if dif == 'perfeito':
        return minimax(tab, jog, 5, ())[1][1]



print(obter_ganhador(((1,0,-1),(0,1,-1),(1,-1,0))))