# nome: Goncalo Miguel Magro Veiga  curso:LETI  Projeto_2_v15

def cria_posicao(x, y):
    """
    Esta funcao recebe as coordenadas de uma posicao e devolve essa posicao
    :param x: int
    :param y: int
    :return: posicao
    """
    if type(x) != int or type(y) != int or x < 0 or y < 0:
        raise ValueError("cria_posicao: argumentos invalidos")
    return (x, y)


def cria_copia_posicao(p):
    """
    Esta funcao recebe uma posicao e cria uma copia dela
    :param p: posicao
    :return: posicao
    """
    p2 = cria_posicao(p[0], p[1])
    return p2


def obter_pos_x(p):
    """
    Esta funcao recebe uma posicao e devolve a componente x
    :param p: posicao
    :return: int
    """
    return p[0]


def obter_pos_y(p):
    """
    Esta funcao recebe uma posicao e devolve a componente y
    :param p: posicao
    :return: int
    """
    return p[1]


def eh_posicao(arg):
    """
    Esta funcao devolve True se arg corresponde a uma posicao e False caso contrario
    :param arg: universal
    :return: Boolean
    """
    if isinstance(arg,(int,float)) and arg < 1000:
        return False
    elif len(arg) != 2:
        return False
    elif type(arg[0]) != int or type(arg[1]) != int:
        return False
    elif arg[0] < 0 or arg[1] < 0:
        return False
    return True


def posicoes_iguais(p1, p2):
    """
    Esta funcao recebe 2 posicoes e devolve True se ambas sao iguais e False caso contrario
    :param p1: posicao
    :param p2: posicao
    :return: Boolean
    """
    if eh_posicao(p1) and eh_posicao(p2):
        return p1 == p2
    return False


def posicao_para_str(p):
    """
    Esta funcao devolve uma cadeia de caracteres que representa a posicao recebida
    :param p: posicao
    :return: string
    """
    return str(p)


def obter_posicoes_adjacentes(p):
    """
    Esta funcao devolve um tuplo com as pos adjacentes de p recebida, na ordem de leitura
    :param p: posicao
    :return: tuplo
    """
    conj = ()
    if p[1] - 1 >= 0:  # posiçao de cima, maze nao tem valores de tamanho negativos
        conj += (p[0], p[1] - 1),
    if p[0] - 1 >= 0:  # posiçao da esquerda, maze nao tem valores de tamanho negativos
        conj += (p[0] - 1, p[1]),
    conj += (p[0] + 1, p[1]), (
        p[0], p[1] + 1),  # estas posiçoes sao sempre validas e estao na ordem de leitura(cima,esquerda,direita,baixo)
    return conj


def cria_unidade(p, HP, ATK, exer):
    """
    Recebe uma posicao, um valor de vida e forca da unidade e o nome do exercito
    :param p: posicao
    :param HP: int
    :param ATK: int
    :param exer: string
    :return: unidade
    """
    if eh_posicao(p) == False or type(exer) != str or type(HP) != int or type(ATK) != int:
        raise ValueError("cria_unidade: argumentos invalidos")
    if HP <= 0 or ATK <= 0 or exer == "":
        raise ValueError("cria_unidade: argumentos invalidos")
    return [p, HP, ATK, exer]


def cria_copia_unidade(u):
    """
    Esta funcao devolve uma copia da unidade recebida
    :param u: unidade
    :return: unidade
    """
    u2 = u[:]
    return u2


def obter_posicao(u):
    """
    Esta funcao devolve a posicao da unidade u
    :param u: unidade
    :return: posicao
    """
    return u[0]


def obter_exercito(u):
    """
    Esta funcao devolve o nome do exercito da unidade u
    :param u: unidade
    :return: string
    """
    return u[3]


def obter_forca(u):
    """
    Esta funcao devolve o valor da forca da unidade u
    :param u: unidade
    :return: int
    """
    return u[2]


def obter_vida(u):
    """
    Esta funcao devolve o valor da vida da unidade u
    :param u: unidade
    :return: int
    """
    return u[1]


def muda_posicao(u, p):
    """
    Modifica destrutivamente a unidade u mudando a sua posicao com o valor p
    :param u: unidade
    :param p: posicao
    :return: unidade
    """
    u[0] = p
    return u


def remove_vida(u, HP):
    """
    Modifica destrutivamente a unidade u mudando o seu valor de vida com o de HP, devolve a unidade
    :param u: unidade
    :param HP: int
    :return: unidade
    """
    u = u[:1] + [obter_vida(u) - HP] + u[2:]
    return u


def eh_unidade(arg):
    """
    Devolve True caso arg seja uma unidade valida
    :param arg: universal
    :return: Boolean
    """
    if len(arg) != 4:
        return False
    elif type(arg[1]) != int or type(arg[2]) != int:
        return False
    elif arg[1] < 1 or arg[2] < 1:
        return False
    elif eh_posicao(arg[0]) != True:
        return False
    elif type(arg[3]) != str or arg[3] == "":
        return False
    return True


def unidades_iguais(u1, u2):
    """
    Devolve True caso u1 e u2 sejam unidade iguais e False caso contrario
    :param u1: unidade
    :param u2: unidade
    :return: Boolean
    """
    if eh_unidade(u1) == True and eh_unidade(u2) == True:
        return u1 == u2
    return False


def unidade_para_char(u):
    """
    Recebe uma unidade e devolve o primeiro caracter do exercito em maiuscula
    :param u: unidade
    :return: string
    """
    return obter_exercito(u)[0].upper()


def unidade_para_str(u):
    """
    Devolve a cadeia de caracteres que representa a unidade
    :param u: unidade
    :return: string
    """
    unidade_string = unidade_para_char(u) + str([obter_vida(u), obter_forca(u)]) + "@" + str((obter_posicao(u)))
    return unidade_string


def unidade_ataca(u1, u2):
    """
    Modifica destrutivamente u2, retirando o valor de pontos de vida correspondente ao ataque de u1, devolve True se u2 for destruida e False caso contrario
    :param u1: unidade
    :param u2: unidade
    :return: Boolean
    """
    res = obter_vida(u2) - obter_forca(u1)
    u2[1] = res
    if res <= 0:
        return True
    return False


def ordenar_unidades(t):
    """
    Ordena as unidades dentro do tuplo t pela ordem de leitura
    :param t: tuplo
    :return: tuplo
    """
    ordenacao = []
    for unidade in t:
        ordenacao += obter_posicao(unidade)[
                     ::-1],  # inversao de x e y de cada posicao para ser ordenado de forma correta no sorted, visto que queremos a ordem de leitura damos prioridade aos que estao por cima e de depois da esquerda para direita
    ordenacao = sorted(ordenacao)
    res_posicoes = ()
    for posicoes_invertidas in ordenacao:
        res_posicoes += posicoes_invertidas[::-1],
    unidades_ordenadas = ()
    for pos in res_posicoes:
        for unidade in t:  # ir buscar a unidade com a posicao correspondente
            if pos in unidade:
                unidades_ordenadas += unidade,
    return unidades_ordenadas


def cria_mapa(d, w, e1, e2):
    """
    Recebe d -> dimensao , w -> tuplo com paredes , e1 -> tuplo de unidades dum exercito e e2 ->tuplo de unidades doutro exercito e devolve um mapa (d,w,e1,e2) verificando todos os argumentos
    :param d: tuplo
    :param w: tuplo
    :param e1: tuplo
    :param e2: tuplo
    :return: mapa
    """
    if type(d) != tuple or len(d) != 2 or type(d[0]) != int or type(d[1]) != int or d[0] < 3 or d[1] < 3 or type(
            w) != tuple or type(e1) != tuple or type(e2) != tuple or len(e1) < 1 or len(e2) < 1:
        raise ValueError("cria_mapa: argumentos invalidos")
    if len(w) != 0:
        for posicoes in w:
            if posicoes == ():
                continue
            if eh_posicao(posicoes) == False or posicoes[0] >= d[0] - 1 or posicoes[1] >= d[1] - 1 or 0 in posicoes:
                raise ValueError("cria_mapa: argumentos invalidos")
    for unidade_e1 in e1:
        if eh_unidade(unidade_e1) == False:
            raise ValueError("cria_mapa: argumentos invalidos")
    for unidade_e2 in e2:
        if eh_unidade(unidade_e2) == False:
            raise ValueError("cria_mapa: argumentos invalidos")
    return d, w, e1, e2


def cria_copia_mapa(m):
    """
    Esta funcao recebe um mapa e devolve uma copia do mesmo mapa
    :param m: mapa
    :return: mapa
    """
    m_copia = []
    for e in m:
        m_copia.append(e)
    return tuple(m_copia)


def obter_tamanho(m):
    """
    Devolve um tuplo com as dimensoes do mapa, Nx e Ny
    :param m: mapa
    :return: tuplo
    """
    return m[0]


def obter_nome_exercitos(m):
    """
    Devolve um tuplo ordenado com os nomes dos exercitos do mapa
    :param m: mapa
    :return: tuplo
    """
    if eh_unidade(m[2]) == True:  # para o caso do exercito1 ter apenas 1 unidade
        nome_e1 = m[2][3]
    else:
        nome_e1 = m[2][0][3]  # como tem varias unidades,ele escolhe a primeira, [0]
    if eh_unidade(m[3]) == True:  # para o caso do exercito2 ter apenas 1 unidade
        nome_e2 = m[3][3]
    else:
        nome_e2 = m[3][0][3]  # como tem varias unidades,ele escolhe a primeira, [0]
    return tuple(sorted([nome_e1, nome_e2]))


def obter_unidades_exercito(m, e):
    """
    Devolve um tuplo com as unidades pertencentes ao exercito (e), ordenadas pela ordem de leitura
    :param m: mapa
    :param e: string
    :return: tuplo
    """
    if m[2] != () and ( e in m[2] or e in m[2][0]):
        return ordenar_unidades(m[2])
    return ordenar_unidades(m[3])


def obter_todas_unidades(m):
    """
    Devolve um tuplo com todas as unidades do mapa, ordenadas pela ordem de leitura
    :param m: mapa
    :return: tuplo
    """
    todas_uni = ()
    if eh_unidade(m[2]) == True:
        todas_uni += m[2],
    else:
        for unidade in m[2]:
            if eh_unidade(unidade):
                todas_uni += unidade,
    if eh_unidade(m[3]) == True:
        todas_uni += m[3],
    else:
        for unidade in m[3]:
            if eh_unidade(unidade):
                todas_uni += unidade,
    return ordenar_unidades(todas_uni)


def obter_unidade(m, p):
    """
    Devolve a unidade do mapa que se encontra na posicao p
    :param m: mapa
    :param p: posicao
    :return: unidade
    """
    res = []
    todas_uni = obter_todas_unidades(m)
    for unidade in todas_uni:
        if eh_unidade(todas_uni) == True:
            res = todas_uni
        if p in unidade:
            res += unidade
    return res


def eliminar_unidade(m, u):
    """
    Modifica destrutivamente o mapa m eliminando a unidade (u) do mapa (m), devolvendo m
    :param m: mapa
    :param u: unidade
    :return: mapa
    """
    if u in m[2]:  # verificar se esta no exercito 1
        new_e1 = ()
        for unidades in m[2]:  # percorrer unidades do exercito 1
            if eh_unidade(m[2]) == True:  # caso em que o exercito tem apenas uma unidade
                return (m[0], m[1], new_e1, m[3])
            if unidades != u:
                new_e1 += unidades,
        return (m[0], m[1], new_e1, m[3])
    if u in m[3]:  # verificar se esta no exercito 2
        new_e2 = ()
        for unidades in m[3]:  # percorrer unidades do exercito 2
            if eh_unidade(m[3]) == True:  # caso em que o exercito tem apenas uma unidade
                return (m[0], m[1], m[2], new_e2)
            if unidades != u:
                new_e2 += unidades,
        return (m[0], m[1], m[2], new_e2)
    return m


def mover_unidade(m, u, p):
    """
    Modifica destrutivamente o mapa (m) e a unidade (u) alterando a posicao da unidade no mapa para a nova posicao, devolvendo m
    :param m: mapa
    :param u: unidade
    :param p: posicao
    :return: mapa
    """
    if u in m[2] or u == m[2]:  # verificar se esta no exercito 1
        for unidades in m[2]:  # percorrer unidades do exercito 1
            if eh_unidade(m[2]) == True:  # caso em que o exercito tem apenas uma unidade
                m[2][0] = p
                return m
            if unidades == u:
                unidades[0] = p
                return m
    if u in m[3] or u == m[3]:  # verificar se esta no exercito 2
        for unidades in m[3]:  # percorrer unidades do exercito 2
            if eh_unidade(m[3]) == True:  # caso em que o exercito tem apenas uma unidade
                m[3][0] = p
                return m
            if unidades == u:
                unidades[0] = p
                return m
    return m


def eh_posicao_unidade(m, p):
    """
    Devolve True apenas no caso da posicao p do mapa estar ocupada por uma unidade e False caso contrario
    :param m: mapa
    :param p: posicao
    :return: Boolean
    """
    return p in obter_unidade(m, p)


def eh_posicao_corredor(m, p):
    """
    Devolve True apenas no caso da posicao p do mapa corresponder a um corredor e False caso contrario
    :param m: mapa
    :param p: posicao
    :return: Boolean
    """
    return p not in m[1] and p != m[1] and (0 not in p) and (m[0][0] - 1 != p[0]) and (m[0][1] - 1 != p[1])


def eh_posicao_parede(m, p):
    """
    Devolve True apenas no caso da posicao p do mapa corresponder a uma parede e False caso contrario
    :param m: mapa
    :param p: posicao
    :return: Boolean
    """
    return (p in m[1] or p == m[1]) or (0 in p) or (m[0][0] - 1 == p[0]) or (
            m[0][1] - 1 == p[1]) and p not in obter_unidade(m, p)


def mapas_iguais(m1, m2):
    """
    Devolve True se m1 e m2 forem mapas iguais e False caso contrario
    :param m1: mapa
    :param m2: mapa
    :return: Boolean
    """
    if len(m1) != len(m2):
        return False
    for i in range(len(m1)):
        if len(m1[i]) != len(m2[i]):
            return False
        for j in range(len(m1[i])):
            if m1[i][j] != m2[i][j]:
                return False
    return True

def mapa_para_str(m):
    """
    Devolve uma cadeia de caracteres que representa o mapa com as unidades representadas pela sua representacao externa
    :param m: mapa
    :return: str
    """
    mapa_string = ""
    max_x, max_y = m[0]
    for y in range(max_y):
        for x in range(max_x):
            if eh_posicao_corredor(m, (x, y)) == True and eh_posicao_unidade(m, (x, y)) == False :
                mapa_string += "."
            if eh_posicao_parede(m, (x, y)) == True:
                mapa_string += "#"
            if eh_posicao_unidade(m, (x, y)) == True:
                mapa_string += unidade_para_char(obter_unidade(m, (x, y)))

        if y < (max_y) - 1:  # para nao acrescentar um paragrafo a mais
            mapa_string += "\n"
    return mapa_string



def obter_inimigos_adjacentes(m, u):
    """
    Devolve um tuplo contendo as unidades inimigas adjacentes a unidade u, pela ordem de leitura
    :param m: mapa
    :param u: unidade
    :return: tuplo
    """
    inimigos_adjacentes = ()
    pos_adj = obter_posicoes_adjacentes(obter_posicao(u))
    if u in m[2] or u == m[2]:
        unidades_inimigas = m[3]
    else:
        unidades_inimigas = m[2]
    for posicao in pos_adj:  # ir a cada posicao adjacente
        for unidade in unidades_inimigas:  # percorrer todas as unidades inimigas e guardar as que sao adjacentes
            if eh_unidade(unidades_inimigas) == True:  # no caso das unidades inimigas ser apenas uma unica
                if obter_posicao(unidades_inimigas) == posicao:
                    inimigos_adjacentes += unidades_inimigas,
            if obter_posicao(unidade) == posicao:
                inimigos_adjacentes += unidade,
    return inimigos_adjacentes


def obter_movimento(mapa, unit):
    '''
    A funcao obter_movimento devolve a posicao seguinte da unidade argumento
    de acordo com as regras de movimento das unidades no labirinto.

    obter_movimento: mapa x unidade -> posicao
    '''

    ######################
    # Funcoes auxiliares #
    ######################
    def pos_to_tuple(pos):
        return obter_pos_x(pos), obter_pos_y(pos)

    def tuple_to_pos(tup):
        return cria_posicao(tup[0], tup[1])

    def tira_repetidos(tup_posicoes):
        conj_tuplos = set(tuple(map(pos_to_tuple, tup_posicoes)))
        return tuple(map(tuple_to_pos, conj_tuplos))

    def obter_objetivos(source):
        enemy_side = tuple(filter(lambda u: u != obter_exercito(source), obter_nome_exercitos(mapa)))[0]
        target_units = obter_unidades_exercito(mapa, enemy_side)
        tup_com_repetidos = \
            tuple(adj
                  for other_unit in target_units
                  for adj in obter_posicoes_adjacentes(obter_posicao(other_unit))
                  if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj))
        return tira_repetidos(tup_com_repetidos)

    def backtrack(target):
        result = ()
        while target is not None:
            result = (target,) + result
            target, _ = visited[target]
        return result

    ####################
    # Funcao principal #
    ####################
    # Nao mexer se ja esta' adjacente a inimigo
    if obter_inimigos_adjacentes(mapa, unit):
        return obter_posicao(unit)

    visited = {}
    # posicao a explorar, posicao anterior e distancia
    to_explore = [(pos_to_tuple(obter_posicao(unit)), None, 0)]
    # registro do numero de passos minimo ate primeira posicao objetivo
    min_dist = None
    # estrutura que guarda todas as posicoes objetivo a igual minima distancia
    min_dist_targets = []

    targets = tuple(pos_to_tuple(obj) for obj in obter_objetivos(unit))

    while to_explore:  # enquanto nao esteja vazio
        pos, previous, dist = to_explore.pop(0)

        if pos not in visited:  # posicao foi ja explorada?
            visited[pos] = (previous, dist)  # registro no conjunto de exploracao
            if pos in targets:  # se a posicao atual eh uma dos objetivos
                # se eh primeiro objetivo  ou se esta a  distancia minima
                if min_dist is None or dist == min_dist:
                    # acrescentor 'a lista de posicoes minimas
                    min_dist = dist
                    min_dist_targets.append(pos)
            else:  # nao 'e objetivo, acrescento adjacentes
                for adj in obter_posicoes_adjacentes(tuple_to_pos(pos)):
                    if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj):
                        to_explore.append((pos_to_tuple(adj), pos, dist + 1))

        # Parar se estou a visitar posicoes mais distantes que o minimo,
        # ou se ja encontrei todos os objetivos
        if (min_dist is not None and dist > min_dist) or len(min_dist_targets) == len(targets):
            break

    # se encontrei pelo menos uma posicao objetivo,
    # escolhe a de ordem de leitura menor e devolve o primeiro movimento
    if len(min_dist_targets) > 0:
        # primeiro dos objetivos em ordem de leitura
        tar = sorted(min_dist_targets, key=lambda x: (x[1], x[0]))[0]
        path = backtrack(tar)
        return tuple_to_pos(path[1])

    # Caso nenhuma posicao seja alcancavel
    return obter_posicao(unit)


def calcula_pontos(m, exer):
    """
    Devolve a pontuacao dum exercito (exer), ou seja, total de pontos de vida de todas as unidades desse exercito
    :param m: mapa
    :param exer: string
    :return: int
    """
    points = 0
    for unidades in obter_unidades_exercito(m, exer):
        if eh_unidade(unidades):
            points += obter_vida(unidades)
    return points


def simula_turno(m):
    """
    Modifica o mapa, de forma a que cada unidade viva realize um movimento e um ataque(caso esteja adjacente a inimigo) e devolve m
    :param m: mapa
    :return: mapa
    """
    todas_uni = obter_todas_unidades(m)
    for unidade in todas_uni:
        if eh_unidade(unidade):
            if m[2] != () and m[3] != ():
                unidade[0] = obter_movimento(m, unidade)
            close_enemies = obter_inimigos_adjacentes(m, unidade)
            if close_enemies != ():
                if eh_unidade(close_enemies):  # para o caso de close_enemies ter apenas uma unica unidade
                    if unidade_ataca(unidade, close_enemies):
                        m = eliminar_unidade(m, close_enemies)
                else:
                    if unidade_ataca(unidade, close_enemies[0]):
                        m = eliminar_unidade(m, close_enemies[0])
    return m


def simula_batalha(str,modo):
    """
    Simula turnos ate houver um vencedor(unidades inimigas eliminadas) ou EMPATE(nao sao possiveis mais turnos diferentes). Pode ser executado em 2 modos, verboso(True) que mostra o mapa e a pontuacao a cada turno, e quiet(False) que apenas mostra no inicio e no fim.
    :param str: string
    :param modo: Boolean
    :return: mapa
    """
    m,e1,e2,w = (),(),(),()
    with open(str,"r") as file:
        for line in file:
            m += eval(line[:-1]),  # avaliar o conteudo linha a linha do ficheiro
    d = m[0]
    for pos in m[3]:
        if eh_posicao(pos):
            w += tuple(pos),
    nome_e1,hp_e1,atk_e1 = m[1][0],m[1][1],m[1][2]
    nome_e2, hp_e2, atk_e2 = m[2][0], m[2][1], m[2][2]
    pos_e1,pos_e2 = m[4],m[5]
    for posicao in pos_e1:
        if eh_posicao(tuple(pos_e1)):
            e1 += [pos_e1,hp_e1,atk_e1,nome_e1],
        else:
            e1 += [tuple(posicao), hp_e1, atk_e1, nome_e1],
    for posicao in pos_e2:
        if eh_posicao(tuple(pos_e2)):
            e2 += [pos_e2,hp_e2,atk_e2,nome_e2],
        else:
            e2 += [tuple(posicao), hp_e2, atk_e2, nome_e2],
    m = cria_mapa(d,w,e1,e2)
    i = 0  # usar uma variavel de controlo para saber se eh o inicio da simulacao , usado no modo quiet
    while True:
        futuros_movimentos = []
        posicoes_atuais = []
        inimigos_adj = ()
        if modo == True or (modo == False and i == 0):
            print(mapa_para_str(m))
            if nome_e2 < nome_e1:
                nome_e1,nome_e2 = nome_e2,nome_e1
            print("[ " + nome_e1 + ":" + calcula_pontos(m, nome_e1).__str__() + " " + nome_e2 + ":" + calcula_pontos(m,nome_e2).__str__() + " ]")
        for unidade in obter_todas_unidades(m): # usado para verificar caso de EMPATE
            posicoes_atuais += obter_posicao(unidade),
            futuros_movimentos += obter_movimento(m,unidade),
            inimigos_adj += obter_inimigos_adjacentes(m,unidade)
        if posicoes_atuais == futuros_movimentos and inimigos_adj == (): # caso de EMPATE
            simula_turno(m)
            print(mapa_para_str(m))
            print("[ " + nome_e1 + ":" + calcula_pontos(m, nome_e1).__str__() + " " + nome_e2 + ":" + calcula_pontos(m,nome_e2).__str__() + " ]")
            return "EMPATE"
        m = simula_turno(m)
        if len(m[2]) == 0 or len(m[3]) == 0:
            print(mapa_para_str(m))
            if len(m[2]) == 0:
                print("[ " + nome_e1 + ":0" + " " + nome_e2 + ":" + calcula_pontos(m, nome_e2).__str__() + " ]")
                return nome_e2
                break
            elif len(m[3]) == 0:
                print("[ " + nome_e1 + ":" + calcula_pontos(m, nome_e1).__str__() + " " + nome_e2 + ":0 ]")
                return nome_e1
                break
        i = 1



print(simula_batalha("config.txt",True))