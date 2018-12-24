lines = [line.rstrip('\n') for line in open('input1.txt')]
result = reduce(lambda a,b: int(a) + int(b), lines, 0)
print(result)