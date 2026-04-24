import matplotlib # type: ignore
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt # type: ignore
import numpy as np #pyright: ignore[reportMissingImports]
from config import TAMANHO_FROTA
import random    

#FAZENDO OS ESQUEMA DO MATPLOT INTERATIVO

plt.ion()
fig, (axGrafo, axMedia, axMelhor, axPior) = plt.subplots(4, 1)
axPior.set_title('Pior individuo')
#NAO TEM O DO GRAFO PQ TIVE QUE FAZER ELE A CADA LOOP
axMedia.set_title('Media dos individuos')
axMelhor.set_title('Melhor individuo')  
cores = np.array(["red", "green", "blue", "yellow", "brown"])

def plotar(percurso,pontos,medias,melhores,piores):
    axGrafo.clear()
    axGrafo.set_title('Melhor percurso')    
    # array_dos_x = np.full(len(percurso)+2, 0)
    # arraY_dos_y = np.full(len(percurso)+2, 0)

    # print("separando")
    # print(percurso, pontos)
    array_dos_x = pontos[:, 0]
    array_dos_y = pontos[:, 1]
    
    #PLOTS
    axGrafo.scatter(array_dos_x, array_dos_y, s=3, c="b")

    percurso_final = np.concatenate([[0], np.where(percurso < len(pontos), percurso, 0), [0]])
    print(percurso_final)
    separadores = np.where(percurso_final == 0)[0]

    for i in range(len(separadores)-1):
        array_dos_x = pontos[percurso_final[separadores[i]:separadores[i+1]+1], 0]
        array_dos_y = pontos[percurso_final[separadores[i]:separadores[i+1]+1], 1]
        axGrafo.plot(array_dos_x, array_dos_y, lw=1, c=cores[i])
    
    # array_dos_x = pontos[percurso_final[i0:i1+1], 0]
    # array_dos_y = pontos[percurso_final[i0:i1+1], 1]

    # array_dos_x1 = pontos[percurso_final[i1:i2+1], 0]
    # array_dos_y1 = pontos[percurso_final[i1:i2+1], 1]

    # array_dos_x2 = pontos[percurso_final[i2:], 0]
    # array_dos_y2 = pontos[percurso_final[i2:], 1]

    #PLOTS
    axMedia.plot(medias, color='red')
    axMelhor.plot(melhores, color='green')
    axPior.plot(piores, color='yellow')

    # axGrafo.plot(array_dos_x0, array_dos_y0, lw=1, c="r")
    # axGrafo.plot(array_dos_x1, array_dos_y1, lw=1, c="g")
    # axGrafo.plot(array_dos_x2, array_dos_y2, lw=1, c="b")

    axGrafo.scatter(pontos[0][0], pontos[0][1], color="red")
    
    plt.show()
    plt.pause(0.01)

