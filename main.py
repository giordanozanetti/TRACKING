from Population_class import Population
from config import POPULATION_SIZE, GENERATIONS
import plot 
import time


pop = Population(POPULATION_SIZE)
start = time.time()
pop.simulate(GENERATIONS)
end = time.time()
print(f'Tempo: {end-start:.2f}')
plot.plt.ioff()
plot.plt.draw()
plot.plt.show()
print(pop.map.locations)
