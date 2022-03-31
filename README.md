# myst_clock_solver
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
