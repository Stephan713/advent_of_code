def overlap(a, b, c, d):
	return not (a > d or b < c)

print(overlap(81,95,37,52))