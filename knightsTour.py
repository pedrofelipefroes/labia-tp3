import random
import copy
from pprint import pprint

import matplotlib.pyplot as plt

NUM_GENERATIONS = 10
POPULATION_SIZE = 30
TABLE_SIZE = 16

def createTable(rows=TABLE_SIZE, columns=TABLE_SIZE, zeroes=True):
	if zeroes:
		return [[0 for i in range(columns)] for j in range(rows)]
	else:
		return [[random.randint(0,10) for i in range(columns)] for j in range(rows)]

class Game():
	def __init__(self):
		self.priority_table = createTable(zeroes=False)
		self.setDefault()

	def setDefault(self):
		self.moves = 0
		self.path = []
		self.table = createTable()
		self.position = (0,0)
		self.table[0][0] = 1

	def nextMoves(self):
		moves = []
		knight_moves = [(2, -1), (2, 1), (-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
		x, y = self.position
		for (dx, dy) in knight_moves:
			if x + dx < 0 or y + dy < 0:
				continue
			try:
				if self.table[x+dx][y+dy] == 0:
					moves.append((x+dx, y+dy))
			except IndexError:
				continue

		return moves

	def getBestMove(self, moves):
		bestValue = float('-inf')
		bestMove = self.position
		for (x, y) in moves:
			if self.priority_table[x][y] > bestValue:
				bestValue = self.priority_table[x][y]
				bestMove = (x,y)

		return bestMove

	def moveTo(self, position):
		x, y = position
		self.path.append(position)
		self.position = position
		self.moves += 1
		self.table[x][y] = self.moves + 1

	def play(self):
		self.setDefault()
		while self.nextMoves():
			moves = self.nextMoves()
			bestMove = self.getBestMove(moves)
			self.moveTo(bestMove)

	def mutation(self):
		x = random.randint(0,TABLE_SIZE-1)
		y = random.randint(0,TABLE_SIZE-1)
		self.priority_table[x][y] = random.randint(0,10)
		self.play()

	def printTable(self):
		for i in range(0, TABLE_SIZE):
			for j in range(0, TABLE_SIZE):
				print(repr(self.table[i][j]).rjust(3), end=' ')
			print()

	def printPriorityTable(self):
		for i in range(0, TABLE_SIZE):
			for j in range(0, TABLE_SIZE):
				print(repr(self.priority_table[i][j]).rjust(3), end=' ')
			print()

	def __add__(self, other):
		g = copy.deepcopy(self)
		for i in range(0, int(TABLE_SIZE/2)):
			for j in range(0, TABLE_SIZE):
				g.priority_table[i][j] = other.priority_table[i][j]

		g.play()
		return g

class Population():
	def __init__(self):
		self.games = []
		self.bestGames = []
		self.worseGames = []

		for i in range(POPULATION_SIZE):
			g = Game()
			self.games.append(g)

	def play(self):
		for game in self.games:
			game.play()

		self.bestGames.append(self.getBestGame()) 
		self.worseGames.append(self.getWorseGame()) 

		print("({0}, {1})".format(self.bestGames[-1].moves, self.worseGames[-1].moves))

	def getBestGame(self):
		bestGame = self.games[0]
		for game in self.games:
			if game.moves > bestGame.moves:
				bestGame = game

		return bestGame

	def getWorseGame(self):
		worseGame = self.games[0]
		for game in self.games:
			if game.moves < worseGame.moves:
				worseGame = game

		return worseGame

	def cross(self):
		pass

	def nextGeneration(self):
		new_generation = []
		for i in range(POPULATION_SIZE):
			i = random.randint(0,POPULATION_SIZE-1)
			j = random.randint(0,POPULATION_SIZE-1)

			new_generation.append(self.games[i] + self.games[j])
			new_generation.append(self.games[j] + self.games[i])

			new_generation[-1].mutation()

		self.games = new_generation
		self.games[0] = self.bestGames[-1]

if __name__ == '__main__':
	p = Population()

	for i in range(NUM_GENERATIONS):
		p.play()
		p.nextGeneration()

	y = []

	for game in p.bestGames:
		y.append(game.moves)

	x = [i for i in range(NUM_GENERATIONS)]

	print('Generations')
	print(x)
	print('Best Game')
	print(y)


	bestGame = p.bestGames[-1]
	print("\nPriority Table")
	bestGame.printPriorityTable()
	print("\nTable")
	bestGame.printTable()