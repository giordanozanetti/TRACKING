from config import ELITISM, SEX_CHANCE, LOCATION_COUNT
from plot import plotar
from LocationMap_class import LocationMap
from Solution_class import Solution
import numpy as np # pyright: ignore[reportMissingImports]
import random

class Population:
    def __init__(self, size):
        self.size = size
        self.solutions = [Solution() for x in range(size)]
        self.map = LocationMap(LOCATION_COUNT)
        self.mean = 0.0
        self.min = 0.0
        self.genartion = 0
        

    def nextGeneration(self):
        self.genartion += 1

        del self.solutions[ELITISM:self.size]
        parents_validos = len(self.solutions)
        while(len(self.solutions) < self.size):
            parent1 = self.solutions[random.randint(0, parents_validos-1)]
            if SEX_CHANCE < random.random():
                parent2 = self.solutions[random.randint(0, parents_validos-1)]
                self.solutions.append(Solution(parent1,parent2))
            else:
                self.solutions.append(Solution(parent1))
        self.sortSolutions()
        print(self.solutions[0].routes, (self.map.fitness(self.solutions[0])/150)**0.5)
        # plotar(self.solutions[0].routes,self.map.locations)

    def simulate(self, count):
        for i in range(count):
            self.nextGeneration()
        self.computeStats()

    def sortSolutions(self):
        evals = {s:self.map.fitness(s) for s in self.solutions}
        self.solutions.sort(key=lambda s: evals[s])

    def computeStats(self):
        total = 0
        self.min = float('inf')

        for s in self.solutions:
            eval = self.map.fitness(s)
            self.min = min(self.min, eval)
            total += eval

        self.mean = total / self.size
        
