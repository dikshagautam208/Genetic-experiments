import random
from math import sqrt, sin, cos, pi
from person import *


class Env:


	def __init__(self, populationSize, survivalRate, matingRate, dnaLength, mutationRate, dataPoints, radius):
		self.populationSize = populationSize
		self.survivalRate = survivalRate
		self.matingRate = matingRate
		self.dnaLength = dnaLength
		self.mutationRate = mutationRate
		self.initRandomPopulation()

		self.dataPoints = dataPoints
		self.radius = radius
		self.createMap()


	def initRandomPopulation(self):
		self.population = [Person(self.dnaLength, self.mutationRate, [], random=True) for _ in range(self.populationSize)]


	def createMap(self):
		# # coordinates for circular graph
		# coords = [[self.radius*cos(2*pi*i/self.dataPoints) , self.radius*sin(2*pi*i/self.dataPoints)] for i in range(self.dataPoints)]
		
		# coordinates for random graph
		coords = [[random.uniform(-1, 1) , random.uniform(-1, 1)] for _ in range(self.dataPoints)]
		self.xs, self.ys = map(list, zip(*coords))


	def calcFitness(self, dna):
		fitness = 0
		for i in range(-1, len(dna) - 1):
			fitness += sqrt( (self.xs[dna[i]] - self.xs[dna[i+1]])**2 + (self.ys[dna[i]] - self.ys[dna[i+1]])**2 )
		return fitness


	def compareFitness(self, person):
		return self.calcFitness(person.dna)


	def sortPopulation(self):
		self.population.sort(key = self.compareFitness)


	def bestFitness(self):
		return self.calcFitness(self.population[0].dna)


	def newPopulation(self):
		# top 10% of the fittest survive
		fitParents = self.population[:int(self.populationSize * self.survivalRate)]

		# rest 90% by mating top 50% of the fittest
		firstParents = random.choices( self.population[:int(self.populationSize * self.matingRate)], k=int(self.populationSize * (1-self.survivalRate)) )
		secondParents = random.choices( self.population[:int(self.populationSize * self.matingRate)], k=int(self.populationSize * (1-self.survivalRate)) )
		offsprings = [ firstParents[i].crossover(secondParents[i]) for i in range(int(self.populationSize * (1-self.survivalRate))) ]

		fitParents.extend(offsprings)
		return fitParents