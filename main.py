from Population_class import Population
from config import POPULATION_SIZE, GENERATIONS
import plot 


pop = Population(POPULATION_SIZE)
pop.simulate(GENERATIONS)
plot.plt.ioff()
plot.plt.draw()
plot.plt.show()