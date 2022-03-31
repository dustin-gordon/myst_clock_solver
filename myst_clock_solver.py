'''
	*********************
	* MYST CLOCK SOLVER *
	*********************

This program generates a solution to a puzzle within the game Myst, found in the clock tower.
The puzzle requires the player to enter the digits 2,2,1 into a system of 3 gears.
Each gear displays a digit between 1 and 3 and all start at position 3. 
A lever on the left side will rotate the middle and bottom gears.
A lever on the right side will rotate the top and middle gears.
Either rotation will increment the gear's digit, or set it to 1 if previously a 3.
A maximum of 9 lever rotations are allowed. 
This program generates a random sequence of lever inputs and checks if 2-2-1 is achieved.
The program will continuously generate new sequences until a valid solution is found.

# Random brute force sequence generation method fails to find a solution, even if given copious runtime. 
# Only 9 revolutions permitted per sequence, but 3**3 = 27 digit positions possible... 
# Also tested ordered permutation set incrementally (2**9 = 512 potential sequences) but still no solution found. 
# Conclusion is that the puzzle is mathematically impossible to solve.
# Puzzle must be rigged or requires additional hidden mechanism to manipulate gears in alternate ways...
# SPOILER ALERT:
# It turns out that there is in fact a gimick to this puzzle. The only way to get the gears to display 2,2,1 is to 
# click and HOLD the left lever, and after a brief pause, the middle gear will display 2. Typical Myst shenanigans...

	- Dustin Gordon

'''

import random

class Puzzle:
	combination = []
	iteration = 0
	revolutions = 0
	solution_found = False

	def lever_left(self):   # rotate middle & bottom gears
		self.combination[1] = self.tumble(self.combination[1])
		self.combination[2] = self.tumble(self.combination[2])

	def lever_right(self):  # rotate top & middle gears
		self.combination[0] = self.tumble(self.combination[0])
		self.combination[1] = self.tumble(self.combination[1])

	def tumble(self, digit): # rotate a single gear
		if  digit == 3:
			digit = 1
		else:
			digit += 1
		return digit

	def print_digits(self):
		print ('      ' + str(self.combination[0]))
		print ('      ' + str(self.combination[1]))
		print ('      ' + str(self.combination[2]))

	def check(self):
		if self.combination[0] == 2: 		# 2, 2, 1 is the necessary combination
			if self.combination[1] == 2:
				if self.combination[2] == 1:
					return True
		else:
			return False

	'''
	def generate_sequence(self): # Sequence Generator (Randomized Implementation)
		sequence = [None]*9
		for index in range(0, len(sequence)):      
			sequence[index] = random.randint(0, 3) # 0 = left turn, 1 = right turn
		#print ('generated sequence: ')
		#print (sequence)
		return sequence
	'''
	
	def generate_sequence(self): # Sequence Generator (Incremental Implementation)
		sequence = [None]*9
		for index in range(0, len(sequence)):
			sequence[index] = (self.iteration >> index) & 0x1
		return sequence

	def print_sequence(self, sequence):
		for direction in sequence:
			if direction == 0:
				print ('Left')
			if direction == 1:
				print ('Right')
		print ('Revolutions = ' + str(revolutions))

	def solve(self, sequence):
		print ('Starting new sequence:')
		print (str(sequence) + ' --> (0 = Left, 1 = Right)')
		for direction in sequence:
			if self.revolutions <= len(sequence):  # max of 9 revolutions permitted
				print ('  Revolution # ' + str(self.revolutions))
			if direction == 0:
				print ('    Rotating left...')
				self.lever_left()
			if direction == 1:
				print ('    Rotating right...')
				self.lever_right()
			self.revolutions += 1
			self.print_digits()
			if self.check():
				return True
		return False

#########################################

def main():
	solver = Puzzle()
	while solver.solution_found == False:
		if solver.iteration > 2**9:
			print ('Maximum potential sequences tested. Solution NOT found. Terminating program.')
			break
		print ('\nIteration # ' + str(solver.iteration))
		random_sequence = solver.generate_sequence()
		solver.combination = [3, 3, 3] # reset to default
		solver.revolutions = 1         # reset to default
		if solver.solve(random_sequence) == True:
			print ('SOLUTION FOUND!')
			print ('Sequence: ')
			solver.print_sequence()
			solver.solution_found = True
		solver.iteration += 1

if __name__ == '__main__':
	main()
