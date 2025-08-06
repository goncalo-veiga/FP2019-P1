# nome: Goncalo Miguel Magro Veiga curso:LETI

def eh_labirinto(maze):
    """2.1.1
    Esta funcao recebe um valor universal e verifica se este corresponde a um conjunto valido de tuplos que representem o labirinto
    verificando assim se esta rodeado por paredes, labirinto de tamanho minimo 3x3 com largura sempre igual e possui
    apenas 0 e 1 dentro dos tuplos
    Retorna se True ou False
    :param maze: argumento universal
    :return: argumento booleano
    """
    if type(maze) != tuple:
        return False
    if len(maze) < 3:                   # comprimento do labirinto
        return False
    for e in maze:
        if type(e) != tuple:
            return False
        if len(e) < 3:                  # largura lab
            return False
        if e[0] != 1 or e[-1] != 1:     # paredes com 1
            return False
        if len(e) != len(maze[0]):      # manter a largura constante
            return False
        for n in e:                     # Verificar que apenas existem 0 e 1
            if type(n) != int:
                return False
            if n != 1:
                if n != 0:
                    return False
    if 0 in maze[0] or 0 in maze[-1]:   # Verificar que o primeiro e ultimo tuplo nao tem 0
        return False

    return True

def eh_posicao(t):
    """2.1.2
    Esta funcao recebe um valor universal e verifica se este corresponde a uma posicao do tipo tuplo, sendo que este tem apenas dois valores int positivos
    Retorna se True ou False
    :param t: argumento universal
    :return: argumento booleano
    """
    if type(t) != tuple:
        return False
    if len(t) != 2:            # apenas 2 valores, x e y
        return False
    if t[0] < 0 or t[1] < 0 or type(t[0]) != int or type(t[1]) != int:   # apenas inteiros nao negativos
        return False
    else:
        return True

def eh_conj_posicoes(conj):
    """2.1.3
    Esta funcao recebe um valor universal e verifica se este corresponde a um conjunto de 0 ou mais posicoes/tuplos diferentes
    Retorna True ou False
    :param conj: argumento universal
    :return: argumento booleano
    """
    if type(conj) != tuple:
        return False
    if len(conj) == 0:          # Para conjunto de 0 posiçoes
        return True
    for pos in conj:
        if type(pos) == int:    # Para apenas 1 tuplo dentro do conjunto
            if len(conj) != 2:  # apenas 2 valores, x e y
                return False
            if type(conj[0]) != int or type(conj[1]) != int or conj[0] < 0 or conj[1] < 0:  # apenas inteiros nao negativos
                return False
            else:
                return True
        if type(pos) != tuple:
            return False
        if conj.count(pos) > 1: # verificar se a posicao unica
            return False
        if pos == ():           # para pos vazio
            continue
        if len(pos) != 2:       # apenas 2 valores, x e y
            return False
        if type(pos[0]) != int or type(pos[1]) != int or pos[0] < 0 or pos[1] < 0:  # apenas inteiros nao negativos
            return False
    return True

def tamanho_labirinto(maze):
    """2.1.4
    Esta funcao recebe um labirinto/maze e obtem o valor do comprimento(x) e largura(y) do maze, caso o maze seja um labirinto valido
    Retorna um tuplo que contem os valores int de comprimento e largura
    :param maze: argumento tuplo
    :return: argumento tuplo
    """
    if eh_labirinto(maze) == True:
        x = len(maze)
        y = len(maze[0])  # numero de elementos num tuplo da maze
        return (x,y)
    else:
        raise ValueError("tamanho_labirinto: argumento invalido")

def eh_mapa_valido(maze,conj):
    """2.1.5
    Esta funcao recebe um labirinto e um conjunto de posicoes verificando a validade de ambos e avalia se as posicoes no
    conjunto correspondem a posicoes livres(nao ocupadas por paredes do labirinto, cujo o valor no maze e 1) e se estao dentro dos limites do labirinto
    Retorna True ou False
    :param maze: argumento tuplo
    :param conj: argumento tuplo
    :return: argumento booleano
    """
    if eh_labirinto(maze) == False or eh_conj_posicoes(conj) == False:
        raise ValueError("eh_mapa_valido: algum dos argumentos e invalido")
    for pos in conj:
        if type(pos) == tuple:
            if pos[0] > tamanho_labirinto(maze)[0] or pos[1] > tamanho_labirinto(maze)[1]: # esta dentro dos limites
                return False
            if maze[pos[0]][pos[1]] != 0: # ver se posicao esta livre
                return False
        else:   # no caso de ter apenas um tuplo, pois pos sera considerado int(para um elemento em um unico tuplo)
            if conj[0] > (tamanho_labirinto(maze)[0] - 1) or conj[1] > (tamanho_labirinto(maze)[1] -1):
                return False
            if maze[conj[0]][conj[1]] != 0:
                return False
    return True

def eh_posicao_livre(maze,unidades,t):
    """2.1.6
     Esta funcao recebe um labirinto(maze), um conjunto de posicoes(unidades) e uma posicao(t) e verifica se todos os
     argumentos sao validos e caso o sejam, avalia se a posicao(t) nao esta contida numa das unidades nem em paredes
    :param maze: argumento tuplo
    :param unidades: argumento tuplo
    :param t: argumento tuplo
    :return: Booleano
    """
    if eh_labirinto(maze) == False or eh_conj_posicoes(unidades) == False or eh_posicao(t) == False or eh_mapa_valido(
            maze, unidades) == False:
        raise ValueError("eh_posicao_livre: algum dos argumentos e invalido")
    for pos in unidades:
        if type(pos) == tuple:
            if pos == t:
                return False
        else:
            if unidades == t:
                return False
    if maze[t[0]][t[1]] == 1:
        return False

    return True

def posicoes_adjacentes(pos):
    """2.1.7
    Esta funcao recebe uma posicao(pos) verificando a validade desta, depois cria um tuplo vazio das posicoes adjacentes,
    formando uma a uma pela ordem de leitura(cima,esquerda,direita,baixo)
    Retorna o tuplo das posicoes adjacentes
    :param pos: argumento tuplo
    :return: argumento tuplo
    """
    if eh_posicao(pos) == False:
        raise ValueError("posicoes_adjacentes: argumento invalido")
    conj = ()
    if pos[1] -1 >= 0:                     # posiçao de cima, maze nao tem valores de tamanho negativos
        conj += ((pos[0],pos[1]-1),)
    if pos[0] -1 >= 0:                     # posiçao da esquerda, maze nao tem valores de tamanho negativos
        conj += ((pos[0]-1,pos[1]),)
    conj += ((pos[0]+1,pos[1]),) + ((pos[0],pos[1] +1),)  # estas posiçoes sao sempre validas e estao na ordem de leitura(cima,esquerda,direita,baixo)
    return conj

def mapa_str(maze,unidades):
    """2.1.8
    Esta funcao recebe um labirinto(maze) e um conjunto de posicoes(unidades),verificando a validade de ambos e se as
    unidades pertencem a posicoes livres e tem como objetivo retornar um "mapa grafico" do tipo string, de maze com as
    unidades, sendo que as paredes "1" -> "#", as posicoes livres "0" -> "." e as posicoes do conjunto "O"->"O"
    Para isso a funcao vai a cada coluna n buscar o elemento i e adicionar a uma lista map que depois vai ser
    transformada em string, de elemento x em x
    :param maze: argumento tuplo
    :param unidades: argumento tuplo
    :return map_res: argumento string
    """
    if eh_labirinto(maze) == False or eh_conj_posicoes(unidades) == False or eh_mapa_valido(maze,unidades) == False:
        raise ValueError("mapa_str: algum dos argumentos e invalido")
    map = []
    map_res = ""
    n = 0  # serve como valor de controlo
    i = 0  # serve como valor de controlo
    while n < len(maze):                               # numero de colunas da maze
        map += [maze[n][i]]
        n += 1
        if n == len(maze) and i < len(maze[0])-1:      # quando acabar de ver o elemento i de cada coluna, aumenta o i  e repete de novo o mesmo processo dando reset no valor de n, tambem adicionando \n ao map para este dps representar paragrafos quando estiver em formato string
            i += 1
            n = 0
            map += "\n"
    for n in unidades:                                 # altera o valor no mapa correspondente à coordenada da unidade mais o numero de elementos que tem de saltar
        if type(n) == tuple:
            map[n[0]+(len(maze)+1)*n[1]] = "O"
        else:                                          # no caso de ter apenas um tuplo, pois pos sera considerado int
            map[unidades[0]+(len(maze)+1)*unidades[1]] = "O"
    for x in map:
        if x == 1:
            map_res += "#"
        if x == 0:
            map_res += "."
        if x == "O":
            map_res += "O"
        if x == "\n":
            map_res += "\n"
    return map_res

def obter_objetivos(maze,unidades,pos):
    """2.2.1
    Esta funcao recebe um labirinto(maze), um conjunto de posicoes(unidades) e uma posicao(pos) e verifica a validade de todos os argumentos
    Retorna conjunto de posicoes nao ocupadas(ou livres),adjacentes as unidades SEM CONTAR com a posicao(pos)
    :param maze: argumento tuplo
    :param unidades: argumento tuplo
    :param pos: argumento tuplo
    :return obj: argumento tuplo
    """
    if eh_labirinto(maze) == False or eh_conj_posicoes(unidades) == False or eh_posicao(pos) == False or eh_mapa_valido(maze, unidades) == False:
        raise ValueError("obter_objetivos: algum dos argumentos e invalido")
    if pos not in unidades:  # a posicao(pos) TEM de pertencer ao conjunto(unidades)
        raise ValueError("obter_objetivos: algum dos argumentos e invalido")
    obj = ()
    for e in unidades:
        if e != pos:                        # ver unidades diferentes da pos
            adj = posicoes_adjacentes(e)
            for x in adj:                   # sendo x um tuplo adjacente de e
                if eh_mapa_valido(maze,x) == True and x not in obj and x != pos and x not in unidades: # cada pos adjacente tem de estar dentro do maze e nao repete ,caso haja alguma em obj e unidades
                    obj += x,
    return obj

def obter_caminho(maze, unidades, pos):
    """2.2.2
    Esta funcao recebe um labirinto, um conjunto de posicoes(unidades) e uma posicao, verificando a validade de todos os
    argumentos e tem como objetivo obter um caminho(path) do tipo tuplo que contem as posicoes que constituem no caminho
    de numero minimo de passos, desde a posicao(pos) ate a uma das posicoes do conjunto de posicoes(unidades) sem contar a propria pos.
    Para isso foi seguido o Algoritmo 1 descrito no enunciado e usado como base nesta funcao, ou seja e criada um lista
    visited com as posicoes ja usadas e uma lista explore correspondente as posicoes que vao ser futuramente visitadas.
    Retorna o tuplo(path) com as posicoes correspondentes ao caminho
    :param maze: argumento tuplo
    :param unidades: argumento tuplo
    :param pos: argumento tuplo
    :return path: argumento tuplo
    """
    if eh_labirinto(maze) == False or eh_conj_posicoes(unidades) == False or eh_posicao(pos) == False or eh_mapa_valido(
            maze, unidades) == False:
        raise ValueError("obter_caminho: algum dos argumentos e invalido")
    if pos not in unidades:
        raise ValueError("obter_caminho: algum dos argumentos e invalido")
    explore = [(pos,())]  # comeca com a posicao(pos)
    visited = []          # começa vazio
    objs = obter_objetivos(maze, unidades, pos)  # tuplo com as unidades livres a volta de de cada posicao em unidades
    if objs == ():   # no caso de nao haver objetivos
        return ()
    while explore != []:
        pos_atual = explore[0][0]  # corresponde ao primeiro elemento dentro do primeiro elemento de explore, que sera sempre tuplo
        path = explore[0][1]       # a segunda posicao no primeiro elemento de explore sera o path a prosseguir
        explore = explore[1:]      # primeira posicao descartada
        if pos_atual not in visited:
            visited += [pos_atual] # atualizar posicoes visitadas
            path += pos_atual,     # atualizar caminho

            if pos_atual in objs:
                return tuple(path) # resultado passado de lista para tuplo

            else: # dentro deste ciclo sao buscadas as novas posicoes em explore que sao as posicoes adjacentes a atual posicao
                adjacentes = posicoes_adjacentes(pos_atual)
                for pos_adj in adjacentes:
                    if maze[pos_adj[0]][pos_adj[1]] == 0:
                        explore += [(pos_adj,path)]

    else:
        return ()

def mover_unidade(maze,unidades,pos):
    """2.2.3
    Esta funcao recebe um labirinto, um conjunto de posicoes(unidades) e uma posicao, verificando a validade de todos os
    argumentos. Ela atualiza os valores das posicoes em unidades de forma a que a posicao(pos) de um passo seguindo o
    caminho(path) minimo entre posicao(pos) e as posicoes em unidades.
    Retorna o tuplo unidades com valores atualizados(podendo em alguns casos ser os mesmos)
    :param maze: argumento tuplo
    :param unidades: argumento tuplo
    :param pos: argumento tuplo
    :return unidades: argumento tuplo
    """
    if eh_labirinto(maze) == False or eh_conj_posicoes(unidades) == False or eh_posicao(pos) == False or eh_mapa_valido(maze, unidades) == False:
        raise ValueError("mover_unidade: algum dos argumentos e invalido")
    if pos not in unidades:
        raise ValueError("mover_unidade: algum dos argumentos e invalido")
    path = obter_caminho(maze,unidades,pos) # obter conjunto das posicoes que formam o caminho entre a pos e as unidades
    new_unidades = []
    for adj in posicoes_adjacentes(pos):   # para o caso de pos estar adjacente a uma das unidades, para que nao se mova
        if adj in unidades:
            return unidades

    for next in path:
        if next not in unidades:        # verficar a cada posicao(next) do caminho(path) se esta pertence a unidades
            new_unidades += next,
            for n in unidades:
                if n != pos:            # ver apenas tuplos em unidades que nao sejam a propria posicao(pos)
                    new_unidades += n,
            unidades = tuple(sorted(new_unidades))  # ordernar a lista para que fiquem na ordem correta e tuplificar a lista
            return unidades
    else:
        return unidades

maze = ((1,1,1,1,1),(1,0,0,0,1),(1,0,0,0,1),(1,0,0,0,1),(1,0,0,0,1),(1,0,0,0,1),(1,1,1,1,1))
unidades = ((2,1),(4,3))
print(mapa_str(maze,unidades))