import copy
import random
import time

NUM_GENERATIONS = 1000
POPULATION_SIZE = 100
TABLE_SIZE = 8
MUTATION_RATE = 0.20

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
		# x = int(TABLE_SIZE * random.random())
		# y = int(TABLE_SIZE * random.random())
		# self.position = (x, y)
		self.position = (0, 0)
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

	def printTables(self):
		print("\nPriority Table")
		self.printPriorityTable()

		print("\nTable")
		self.printTable()

	def __add__(self, other):
		g = copy.deepcopy(self)
		lines = int(random.random() * TABLE_SIZE)
		for i in range(lines):
			for j in range(TABLE_SIZE):
				g.priority_table[i][j] = other.priority_table[i][j]

		g.play()
		return g

class Population():
	def __init__(self):
		self.games = []
		self.bestGames = []
		self.worstGames = []
		self.generation = 0

		for i in range(POPULATION_SIZE):
			g = Game()
			self.games.append(g)

	def play(self):
		for game in self.games:
			game.play()

		self.bestGames.append(self.getBestGame()) 
		self.worstGames.append(self.getWorstGame())
		self.generation += 1

	def getBestGame(self):
		bestGame = self.games[0]
		for game in self.games:
			if game.moves > bestGame.moves:
				bestGame = game

		return bestGame

	def getWorstGame(self):
		worstGame = self.games[0]
		for game in self.games:
			if game.moves < worstGame.moves:
				worstGame = game

		return worstGame

	def nextGeneration(self):
		new_generation = []
		HALF_POPULATION = int(POPULATION_SIZE/2)

		# SELECTION
		for i in range(HALF_POPULATION):
			j = i
			k = i + HALF_POPULATION

			if self.games[j].moves > self.games[k].moves:
				new_generation.append(self.games[j])
			else:
				new_generation.append(self.games[k])

		# CROSSOVER
		for i in range(HALF_POPULATION):
			j = random.randint(0, HALF_POPULATION-1)
			k = random.randint(0, HALF_POPULATION-1)

			self.games[i] = new_generation[j] + new_generation[k]
			self.games[i + HALF_POPULATION] = new_generation[k] + new_generation[j]

		# MUTATION
		for i in range(POPULATION_SIZE):
			if random.random() < MUTATION_RATE:
				self.games[i].mutation()

		self.games[0] = self.bestGames[-1]

	def printBestGame(self):
		print("#{0} ({1}, {2})".format(self.generation, self.bestGames[-1].moves, self.worstGames[-1].moves))

	def goalAchieved(self):
		if not p.bestGames:
			return False

		if p.bestGames[-1].moves == TABLE_SIZE * TABLE_SIZE - 1:
			return True
		else:
			return False


if __name__ == '__main__':
	# start = time.time()
	
	p = Population()

	for i in range(NUM_GENERATIONS):
		p.play()
		p.nextGeneration()
		p.printBestGame()

		if p.goalAchieved():
			break
    
	x = [i for i in range(NUM_GENERATIONS)]
	y = []
	z = []

	for game in p.bestGames:
		y.append(game.moves)

	for game in p.worstGames:
		z.append(game.moves)

	# end = time.time()
	# print(end - start)

# print('\nGenerations')
# print(x)
# print('\nBest Game')
# print(y)
# print('\nWorst Game')
# print(z)


p.bestGames[-1].printTables()