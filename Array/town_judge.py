N = 4
trust = [[1,2],[3,2],[4,2]]
count = [0] * N
for i, j in trust:
	count[i-1] -= 1
	count[j-1] += 1
for i in range(N) :
	if count[i] == N-1:
		print(i+1)