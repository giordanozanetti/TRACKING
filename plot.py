import matplotlib 
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 
import numpy as np #pyright: ignore[reportMissingImports]
import matplotlib 
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 
from config import GENERATIONS

#FAZENDO OS ESQUEMA DO MATPLOT INTERATIVO

plt.ion()
fig, (axGrafo, axMedia, axMelhor, axPior) = plt.subplots(4, 1)
axPior.set_title('Pior individuo')
#NAO TEM O DO GRAFO PQ TIVE QUE FAZER ELE A CADA LOOP
axMedia.set_title('Media dos individuos')
axMelhor.set_title('Melhor individuo')  

def plotar(percurso,pontos,medias,melhores,piores,i,interativo=False):
     
    # array_dos_x = np.full(len(percurso)+2, 0)
    # arraY_dos_y = np.full(len(percurso)+2, 0)

    # print("separando")
    # print(percurso, pontos)
    array_dos_x = pontos[:, 0]
    array_dos_y = pontos[:, 1]
    
    #PLOTS
   

    percurso_final = np.concatenate([[0], np.where(percurso < len(pontos), percurso, 0), [0]])
    array_dos_x = pontos[percurso_final, 0]
    array_dos_y = pontos[percurso_final, 1]

    if interativo:
    #PLOTS
        axGrafo.clear()
        axGrafo.scatter(array_dos_x, array_dos_y)
        axGrafo.set_title('Melhor percurso')   
        axMedia.plot(medias, color='red')
        axMelhor.plot(melhores, color='green')
        axPior.plot(piores, color='yellow')

        axGrafo.plot(array_dos_x, array_dos_y)

        axGrafo.scatter(pontos[0][0], pontos[0][1], color="red")
        plt.pause(0.01)
    else:
        if i == GENERATIONS:
            axGrafo.scatter(array_dos_x, array_dos_y)
            axGrafo.set_title('Melhor percurso')   
            axMedia.plot(medias, color='red')
            axMelhor.plot(melhores, color='green')
            axPior.plot(piores, color='yellow')

            axGrafo.plot(array_dos_x, array_dos_y)
            
            axGrafo.scatter(pontos[0][0], pontos[0][1], color="red")
        