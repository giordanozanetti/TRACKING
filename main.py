from Population_class import Population
from config import POPULATION_SIZE, GENERATIONS
from plot import plotar


pop = Population(POPULATION_SIZE)
pop.simulate(GENERATIONS)

plotar(pop.solutions[0].routes,pop.map.locations)