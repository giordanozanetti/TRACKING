from config import TAMANHO_FROTA, LOCATION_COUNT, MAJOR_MUTATION_RATE, MINOR_MUTATION_RATE, EXCLUSIVE_CROSS, EXCLUSIVE_MAJOR
import numpy as np # pyright: ignore[reportMissingImports]
import random

class Solution:
    def __init__(self, parent1= None, parent2= None):
        self.routes = np.zeros(LOCATION_COUNT+TAMANHO_FROTA-2, dtype=int)
        if parent2 == None :
            if parent1 == None:
                self.routes = np.arange(1, LOCATION_COUNT+TAMANHO_FROTA-1)

                for i in range(len(self.routes) - 1, 0, -1):
                    j = random.randint(0, i-1)
                    temp = self.routes[j]
                    self.routes[j] = self.routes[i]
                    self.routes[i] = temp
                
                
            else:
                self.routes = parent1.routes.copy()
                self.mutate()
        else:
            self.routes = np.full(len(parent1.routes), -1)

            #MENOS 2 PORQUE O RANDIINT INCLUI O ULTIMO
            inicio_segmento = random.randint(0,len(parent1.routes)-2)
            final_segmento = random.randint(0,len(parent1.routes)-1-inicio_segmento)+inicio_segmento
            self.routes[inicio_segmento:final_segmento+1] = parent1.routes[inicio_segmento: final_segmento+1].copy()

            #ARRAY DE BOLEANOS PARA SER MIAS RAPIDA A PROCURA POR QUAIS ESTÃO NO ARRAY
            parent2_contem = np.zeros(len(parent2.routes), bool)
            for i in self.routes:
                if i > -1: parent2_contem[i - 1] = True

            #COMECA NO FINAL DO SEGMENTO
            parent2_index = final_segmento
            #OX
            for i in range(len(self.routes)):
                if i >= inicio_segmento and i < final_segmento+1: continue
                while self.routes[i] == -1:
                    local = parent2.routes[parent2_index]

                    if not(parent2_contem[local-1]):
                        self.routes[i] = parent2.routes[parent2_index]
                    #SE CHEGOU NO FINAL VOLTA PRO COMEÇO, ASSIM ELE PERCORRE DIRETO
                    if parent2_index >= len(self.routes) - 1: parent2_index = 0
                    else: parent2_index += 1

            if not EXCLUSIVE_CROSS: self.mutate()
                
            


    def mutate(self):
        if MAJOR_MUTATION_RATE > random.random():
            self.inverseMutation()
            if (EXCLUSIVE_MAJOR): return

        if MINOR_MUTATION_RATE > random.random():
            if random.randint(0, 1):
                self.shiftMutation()
            else:
                self.swapMutation()
    def inverseMutation(self):
        min = 2
        a = random.randint(0, len(self.routes)-min)
        b = random.randint(0, len(self.routes)-min)
        span = abs(a - b)+min
        start = random.randint(0, len(self.routes)-span)
        
        self.routes[start:start+span] = self.routes[start:start+span][::-1]
            
    def shiftMutation(self):
        _from = random.randint(0, len(self.routes)-1)
        to = random.randint(0, len(self.routes)-1)
        value = self.routes[_from]

        temp = np.zeros(len(self.routes)-1, dtype=int)
        for i in range(len(temp)):
            temp[i] = self.routes[i+(i >= _from)]

        for i in range(len(self.routes)):
            if i < to:
                self.routes[i] = temp[i]
            elif i > to:
                self.routes[i] = temp[i - 1]
            else:
                self.routes[i] = value

    def swapMutation(self):
        a = random.randint(0, len(self.routes)-1)
        b = random.randint(0, len(self.routes)-1)

        temp = self.routes[a]
        self.routes[a] = self.routes[b]
        self.routes[b] = temp



            


        






































