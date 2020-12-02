ar = [float(i) for i in input().split()]
ar_sq = []
for i in range(len(ar)):
	ar_sq.append(ar[i]**2)
ar_sq = sorted(ar_sq)
print(ar_sq[0], end = ' ')
for i in range(1, len(ar_sq)):
	if ar_sq[i] != ar_sq[i-1]:
		print(ar_sq[i], end = ' ')
