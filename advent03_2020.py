import math

with open("input03.txt") as f:
	lines = [x.rstrip() for x in f.readlines()]

	tree = '#'

	# All different slopes to loop over
	slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

	# List of all tree_count from each slope. Used for part 2 answer.
	mult = []

	for slope in slopes:
		tree_count = 0

		# Position for horizontal position
		pos = 0

		# Assigns slope tuple to appropriate variables names
		right_step, down = slope

		# Only loops over the lines that are included in the "downward"-step
		for line in lines[0::down]:
			
			# Tree collision
			if line[pos] == tree:
				tree_count += 1

			# Modulo to restart horizontal position for when (pos + right_step) steps out of index.
			pos = (pos + right_step) % len(line)

		print("Slope " + str(slope) + " gives: " + str(tree_count))
		mult.append(tree_count)

	print("Part 2: " + str(math.prod(mult)))