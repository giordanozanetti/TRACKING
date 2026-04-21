import matplotlib 
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 
import numpy as np #pyright: ignore[reportMissingImports]


#FAZENDO OS ESQUEMA DO MATPLOT INTERATIVO
plt.ion()
fig, (axGrafo) = plt.subplots(1, 1)
axGrafo.set_title('Melhor percurso')  

def plotar(percurso,pontos):
    axGrafo.clear()
    axGrafo.set_title('Melhor percurso')    
    array_dos_x = np.full(len(percurso)+2, 0)
    arraY_dos_y = np.full(len(percurso)+2, 0)

   
    #PLOTS
    axGrafo.plot(array_dos_x, arraY_dos_y)

    plt.draw()
    plt.pause(0.0001)