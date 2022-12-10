# ===========================================================#
# Mathématiques Discrètes - Projet Plus_Court_Chemin         #
# Auteurs - Huet Anatole, Kheirallah Cédric, Laraki Narjis   #
# ===========================================================#
import numpy as np
import csv

inf = 1.e+12

def Dijkstra(C):
    """
    Trouve les plus courts chemins par l'algorithme de Dijkstra
    :param C : Une matrice numpy n × n de coûts d’un graphe non dirigé, pondéré et connecté G
    :return D : Une matrice n × n D contenant les distances des plus courts chemins entre toutes les paires de nœuds du graphe G
    """
    global inf
    D = np.zeros((len(C), len(C))) # matrice de retour
    for i in range(len(C)):
        # initialiser distances[i] et array visited
        distances = [inf]*len(C)
        distances[i] = 0
        visited = [False]*len(C)

        n = 0
        # itère sur les nœuds/lignes
        while (n < len(C)):
            # trouver la distance min et son index
            min_dist = inf
            min_index = 0
            for x in range(len(C)):
                if (distances[x] < min_dist) and not (visited[x]):
                    min_dist = distances[x]
                    min_index = x
            # marquer le passage
            visited[min_index] = True

            for j in range(len(C)):
                if (C[min_index][j] > 0) and ((distances[min_index] + C[min_index][j]) < distances[j]) and not (visited[j]):
                    distances[j] = distances[min_index] + C[min_index][j]
            n += 1

        # attribuer nouvelle ligne à matrice de retour
        D[i] = distances

    return D

def Bellman_Ford(C):
    """
    Trouve les plus courts chemins par l'algorithme de Bellman_Ford
    :param C : Une matrice numpy n × n de coûts d’un graphe non dirigé, pondéré et connecté G
    :return D : Une matrice n × n D contenant les distances des plus courts chemins entre toutes les paires de nœuds du graphe G
    """
    D = C
    return D

def Floyd_Warshall(C):
    """
    Trouve les plus courts chemins par l'algorithme de Floyd_Warshall
    :param C : Une matrice numpy n × n de coûts d’un graphe non dirigé, pondéré et connecté G
    :return D : Une matrice n × n D contenant les distances des plus courts chemins entre toutes les paires de nœuds du graphe G
    """
    D = C
    return D

def is_symmetrical(C):
    """
    Fonction auxiliaire pour vérifier qu'une matrice est bien égale à sa transposée
    :param C : Une matrice numpy n x n
    :return : Un booléen
    """
    return (np.transpose(C) == C).all()

def print_inf(C):
    """
    Fonction utilitaire pour print les matrices avec 'inf' au lieu de '1.e+12'
    :param C : Une matrice numpy n x n
    """
    P = C.copy()
    for i in range(len(P)):
        for j in range(len(P[i])):
            if (P[i][j] == 1.e+12): P[i][j] = "inf"
    print(P)

if __name__ == '__main__':
    # Lecture de la matrice de coûts C à partir d'un fichier .csv
    file = open('costs_matrix_C.csv')
    csvreader = csv.reader(file)
    C = np.zeros((10, 10))
    index = 0
    for row in csvreader:
        if index == 0: row[0] = row[0][-1]
        C[index] = row
        index += 1
    file.close()

    # prints
    print_inf(Dijkstra(C.copy()))
    print(is_symmetrical(Dijkstra(C.copy())), end="\n\n")
    print_inf(Bellman_Ford(C.copy()))
    print(is_symmetrical(Bellman_Ford(C.copy())), end="\n\n")
    print_inf(Floyd_Warshall(C.copy()))
    print(is_symmetrical(Floyd_Warshall(C.copy())), end="\n\n")
