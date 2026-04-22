from Population_class import Population
from config import POPULATION_SIZE, GENERATIONS
import plot 


pop = Population(POPULATION_SIZE)
pop.simulate(GENERATIONS)
plot.plt.ioff()

# plot.plotar(pop.solutions[0].routes,pop.map.locations,pop.medias,pop.melhores,pop.piores,False)

plot.plt.draw()
plot.plt.show()