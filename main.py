#===========================================================#
# Mathématiques Discrètes - Projet Plus_Court_Chemin        #
# Auteurs - Huet Anatole, Kheirallah Cédric, Laraki Narjis  #
#===========================================================#
import numpy as np

def Dijkstra(C):
    return C

def Bellman_Ford(C):
    return C

def Floyd_Warshall(C):
    return C

if __name__ == '__main__':
    C = np.matrix([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

    print(Dijkstra(C))
    print(Bellman_Ford(C))
    print(Floyd_Warshall(C))
