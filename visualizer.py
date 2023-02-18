from constants import *
from environment import *
import sys
import matplotlib.pyplot as plt 
from matplotlib import style
style.use("ggplot")


def initMap():
	plt.figure("Visualizer")
	plt.scatter(env.xs, env.ys)
	plt.xlim(-plotSize, plotSize)
	plt.ylim(-plotSize, plotSize)

	for i in range(dataPoints):
		plt.annotate(i, # this is the text
					(env.xs[i], env.ys[i]), # this is the point to label
					textcoords="offset points", # how to position the text
					xytext=(env.xs[i]*10, env.ys[i]*10), # distance from text to points (x,y)
					ha='center') # horizontal alignment can be left, right or center
	plt.show(block = False)


def drawBestRoute():
	person = env.population[0]
	px = [env.xs[i] for i in person.dna + person.dna[:1]]
	py = [env.ys[i] for i in person.dna + person.dna[:1]]
	plt.plot(px, py, color = 'b')
	plt.show(block = False)


def main():

	generationIdx = 0
	fitnessTrend = []

	while generationIdx < noOfGenerations:

		env.sortPopulation()
		fitnessTrend.append(env.bestFitness())
		# print("Generation: {}\t{}".format(generationIdx, fitnessTrend[-1]))

		if showFitnessPlot:
			plt.figure("Fitness Trend")
			plt.plot( list(range(generationIdx + 1)), fitnessTrend )
			plt.show(block = False)

			# evolution plot 
			initMap()
			drawBestRoute()
			plt.show(block = False)
			plt.pause(0.001)

			if generationIdx == noOfGenerations-1:
				plt.show(block = True)
				break
			else:
				plt.clf()

		env.population = env.newPopulation()
		generationIdx += 1


if __name__ == "__main__":
	env = Env(populationSize, survivalRate, matingRate, dnaLength, mutationRate, dataPoints, radius)
	main()
