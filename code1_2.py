lines = [int(line.rstrip('\n')) for line in open('input1.txt')]
seen = set([])
curr_freq = 0
i = 0

while True:

	curr_freq = curr_freq + lines[i]
	if curr_freq in seen:
		print(curr_freq)
		break
	seen.add(curr_freq)

	i = i + 1
	if i >= len(lines): i = 0
