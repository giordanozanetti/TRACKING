from config import  DEPOSITO_CENTRO
import numpy as np # pyright: ignore[reportMissingImports]
import math



class LocationMap:
    def __init__(self, quantidade_pontos):
        #gera ele ja com pontos aleatorios
        self.locations = np.random.randint(0, 500, size=(quantidade_pontos, 2)).astype(np.float32)

        #se o deposito e no meio
        if DEPOSITO_CENTRO:
            self.locations[0] = [250,250]
        # print(self.locations)
        # print(len(self.locations))

    def distance(self, ponto1, ponto2):
        return math.hypot(ponto1[0]-ponto2[0], ponto1[1]-ponto2[1])

    def fitness(self, solution):
        ultimo = self.locations[0]
        distancia_segmento = 0
        
        total = 0

        for i in range(len(solution.routes)):
            if i == len(solution.routes) or solution.routes[i] >= len(self.locations):
                distancia_segmento += self.distance(self.locations[0], ultimo)
                total += distancia_segmento**2
                distancia_segmento = 0
                last = self.locations[0]
            else:
                ponto_atual = self.locations[solution.routes[i]]
                distancia_segmento += self.distance(ponto_atual, ultimo)
                ultimo = ponto_atual
        # print(total)
        return total
    
    
