lines = [line.rstrip('\n') for line in open('input2.txt')]

# Test input
#lines = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']

"""
Questions:
1. Is there gauranteed to be a single pair of such strings?
"""

n = len(lines)

one_char_apart = []

# O(n^2 * m) algorithm
# n is number of strings
# m is the length of the largest string

for i in range(0, n - 1):
	for j in range(i + 1, n):

		# length must match
		if len(lines[i]) != len(lines[j]):
			continue

		k = 0
		l = len(lines[i])
		# match beginning of string
		while k < l and lines[i][k] == lines[j][k]:
			k = k + 1
		# one mistake tolerated
		k = k + 1
		# match rest of string
		while k < l and lines[i][k] == lines[j][k]:
			k = k + 1
		if k == len(lines[i]) and k == len(lines[j]):
			one_char_apart.extend([lines[i], lines[j]])

# print common characters
if len(one_char_apart) == 2:
	common = []
	k = 0
	l = len(one_char_apart[0])
	while k < l:
		if one_char_apart[0][k] == one_char_apart[1][k]:
			common.append(one_char_apart[0][k])
		k = k + 1
	print('Result: ' + ''.join(common))
else:
	print('No matched found')