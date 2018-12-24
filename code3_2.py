import re
import numpy as np

# 1000 x 1000 grid
size = 1000
fabric = np.zeros((size, size))
pattern = r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)'

lines = [line.rstrip('\n') for line in open('input3.txt')]

# Test input
# lines = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']

# Create grid counts
for line in lines:
	matches = re.match(pattern, line)
	ticket_id, left_edge, top_edge, width, height = map(int, matches.groups())

	# update count on grid
	for i in range(top_edge, top_edge + height):
		for j in range(left_edge, left_edge + width):
			fabric[i,j] = fabric[i,j] + 1

# find a rectange on grid with a single count
for line in lines:
	matches = re.match(pattern, line)
	ticket_id, left_edge, top_edge, width, height = map(int, matches.groups())

	only_single = True
	# update count on grid
	for i in range(top_edge, top_edge + height):
		for j in range(left_edge, left_edge + width):
			if fabric[i,j] > 1:
				only_single = False

	if only_single:
		print(ticket_id)