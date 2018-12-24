"""

Want to find resulting polymer after a set of reductions.
Reductions follow the single recursive rule that any
time two of the same letter wtih different capitalizations
(A and a, b and B, etc.) are adjacent are eliminated

Want to return length of resulting polymer

Method:
1. Run through polymer removing all patterns following the rule,
keeping track of how many reductions are made. If the end of the
string is reached without making a single reduction, then do
not move to step 2.
2. Repeat (1) on the resulting string.

Return the length of the final polymer string

"""

polymer = open('input5.txt').read().strip()

# Test input
# polymer = 'dabAcCaCBAcCcaDA'

made_change = True

while made_change:

	made_change = False

	i = 0
	while i < len(polymer) - 1:
		# using ASCII values, the differene between the ASCII value
		# of a capitalized and a lowercase of the same letter is exactly
		# 32 for every alphabet character (a through z)
		if abs(ord(polymer[i]) - ord(polymer[i+1])) == 32:
			# i + 2 can be out of range, but in Python
			# array slices out of range return empty string
			polymer = polymer[:i] + polymer[i+2:]
			made_change = True
			# character at index i in updated polymer is unprocessed
			# because the characters at index i and i + 1 in the
			# original polymer were deleted, so the string was shifted
			# left by 2
		else:
			i = i + 1

print(len(polymer))