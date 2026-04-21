import matplotlib 
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 
import numpy as np #pyright: ignore[reportMissingImports]


#FAZENDO OS ESQUEMA DO MATPLOT INTERATIVO
# plt.ion()
fig, (axGrafo) = plt.subplots(1, 1)
axGrafo.set_title('Melhor percurso')  

def plotar(percurso,pontos):
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

    axGrafo.plot(array_dos_x, array_dos_y)

    axGrafo.scatter(pontos[0][0], pontos[0][1], color="red")

    plt.show()
    plt.pause(0.01)