import matplotlib # type: ignore
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt # type: ignore
import numpy as np #pyright: ignore[reportMissingImports]

#FAZENDO OS ESQUEMA DO MATPLOT INTERATIVO

plt.ion()
fig, (axGrafo, axMedia, axMelhor, axPior) = plt.subplots(4, 1)
axPior.set_title('Pior individuo')
#NAO TEM O DO GRAFO PQ TIVE QUE FAZER ELE A CADA LOOP
axMedia.set_title('Media dos individuos')
axMelhor.set_title('Melhor individuo')  

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
    axGrafo.scatter(array_dos_x, array_dos_y)

    percurso_final = np.concatenate([[0], np.where(percurso < len(pontos), percurso, 0), [0]])
    array_dos_x = pontos[percurso_final, 0]
    array_dos_y = pontos[percurso_final, 1]

    #PLOTS
    axMedia.plot(medias, color='red')
    axMelhor.plot(melhores, color='green')
    axPior.plot(piores, color='yellow')

    axGrafo.plot(array_dos_x, array_dos_y)

    axGrafo.scatter(pontos[0][0], pontos[0][1], color="red")
    
    plt.show()
    plt.pause(0.01)

