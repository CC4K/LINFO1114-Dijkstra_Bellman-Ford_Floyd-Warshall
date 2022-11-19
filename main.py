#===========================================================#
# Mathématiques Discrètes - Projet Plus_Court_Chemin        #
# Auteurs - Huet Anatole, Kheirallah Cédric, Laraki Narjis  #
#===========================================================#
import numpy as np
import csv

def Dijkstra(C):
    """
    Trouve les plus courts chemins par l'algorithme de Dijkstra
    :param C : Une matrice numpy n × n de coûts d’un graphe non dirigé, pondéré et connecté G
    :return : Une matrice n × n D contenant les distances des plus courts chemins entre toutes les paires de nœuds du graphe G
    """
    return C

def Bellman_Ford(C):
    """
    Trouve les plus courts chemins par l'algorithme de Bellman_Ford
    :param C : Une matrice numpy n × n de coûts d’un graphe non dirigé, pondéré et connecté G
    :return : Une matrice n × n D contenant les distances des plus courts chemins entre toutes les paires de nœuds du graphe G
    """
    return C

def Floyd_Warshall(C):
    """
    Trouve les plus courts chemins par l'algorithme de Floyd_Warshall
    :param C : Une matrice numpy n × n de coûts d’un graphe non dirigé, pondéré et connecté G
    :return : Une matrice n × n D contenant les distances des plus courts chemins entre toutes les paires de nœuds du graphe G
    """
    return C

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

    print(Dijkstra(C))
    print(Bellman_Ford(C))
    print(Floyd_Warshall(C))
