import numpy as np
import random 
parent1 = np.array([1,2,3,4,5,6,7])
parent2 = np.array([7,6,5,4,3,2,1])
import time

start = time.time()
def ox ():
    routes = np.full(len(parent1), -1)

    #MENOS 2 PORQUE O RANDIINT INCLUI O ULTIMO
    inicio_segmento = random.randint(0,len(parent1)-2)
    final_segmento = random.randint(0,len(parent1)-1-inicio_segmento)+inicio_segmento
    routes[inicio_segmento:final_segmento+1] = parent1[inicio_segmento: final_segmento+1].copy()

    #ARRAY DE BOLEANOS PARA SER MIAS RAPIDA A PROCURA POR QUAIS ESTÃO NO ARRAY
    parent2_contem = np.zeros(len(parent2), bool)
    for i in routes:
        if i > -1: parent2_contem[i - 1] = True

    #COMECA NO FINAL DO SEGMENTO
    parent2_index = final_segmento
    #OX
    for i in range(len(routes)):
        if i >= inicio_segmento and i < final_segmento: continue
        while routes[i] == -1:
            local = parent2[parent2_index]

            if not(parent2_contem[local-1]):
                routes[i] = parent2[parent2_index]
            #SE CHEGOU NO FINAL VOLTA PRO COMEÇO, ASSIM ELE PERCORRE DIRETO
            if parent2_index >= len(routes) - 1: parent2_index = 0
            else: parent2_index += 1

    # print(inicio_segmento, final_segmento)
    # print(routes)

i=0
while i < 50:
    ox()
    i+=1
end = time.time()

# print(end-start)