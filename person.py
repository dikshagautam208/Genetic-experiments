import random


class Person:
	def __init__(self, dnaLength, mutationRate, dna, random=False):
		self.dnaLength = dnaLength
		self.mutationRate = mutationRate
		self.dna = dna if (not random) else self.randomDna()

	# create a random sequence of cities' indices
	def randomDna(self):
		dna = list(range(self.dnaLength))
		random.shuffle(dna)
		return dna

	# cross-breeding this person with the mate
	def crossover(self, mate):
		firstDna = random.sample([self, mate], 1)[0].dna
		secondDna = self.dna if ( firstDna == mate.dna) else mate.dna

		# copy first half of one parent, add rest from second parent
		offspring = firstDna[:self.dnaLength//2]
		offspring += [x for x in secondDna if x not in offspring]

		# introduce mutations
		randIdx = random.sample( list(range(self.dnaLength)), int(self.dnaLength*self.mutationRate) )

		for i in range(len(randIdx)//2):
			iSwap = -i-1
			offspring[randIdx[i]], offspring[randIdx[iSwap]] = offspring[randIdx[iSwap]], offspring[randIdx[i]]

		return Person(self.dnaLength, self.mutationRate, offspring)