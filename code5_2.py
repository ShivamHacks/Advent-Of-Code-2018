"""

Want to find the length of the polymer that is smallest
after removing all instances of a specific character, regardless
of case (capital or lower).

Method:
Reduce the polymer, then for all 26 characters in the English
alphabet (case-insensitive) in the string create a copy of the
polymer with those characters removed, reduce the polymer and
calculate the length of this new polymer. Keep track of the
smallest length encountered. Return the smallest length.

"""

import re

polymer = open('input5.txt').read().strip()

# Test input
# polymer = 'dabAcCaCBAcCcaDA'

# code to calculate length of reduced polymer
def reduced(polymer):
	made_change = True
	while made_change:
		made_change = False
		i = 0
		while i < len(polymer) - 1:
			if abs(ord(polymer[i]) - ord(polymer[i+1])) == 32:
				polymer = polymer[:i] + polymer[i+2:]
				made_change = True
			else:
				i = i + 1
	return polymer

# get smallest polymer length
polymer = reduced(polymer)
print('Reduced polymer')
smallest = len(polymer)

for c_upper in set(polymer.upper()):
	c_lower = c_upper.lower()
	polymer_new = re.sub(r'{}|{}'.format(c_upper, c_lower), '', polymer)
	len_new = len(reduced(polymer_new))
	if len_new < smallest:
		smallest = len_new
	print('Completed: ', c_upper)

# result
print('Result: ', smallest)
