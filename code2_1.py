lines = [line.rstrip('\n') for line in open('input2.txt')]
two_cnt = 0
three_cnt = 0

# Test input
# lines = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']

for line in lines:

	has_two = 0
	has_three = 0

	chars = list(line)
	cmap = {}

	for char in chars:
		if char in cmap:
			cmap[char] = cmap[char] + 1
		else:
			cmap[char] = 1

	for cnt in cmap.itervalues():
		if cnt == 3:
			has_three = 1
		elif cnt == 2:
			has_two = 1

	two_cnt = two_cnt + has_two
	three_cnt = three_cnt + has_three

print(str(two_cnt * three_cnt))