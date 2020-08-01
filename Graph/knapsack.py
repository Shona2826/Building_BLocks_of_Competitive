def knapsack(p,w,m,n):
	dp = [[0 for i in range(m+1)] for j in range(n+1)]
	#print(dp)
	for i in range(n+1):
		for j in range(m+1):
			if i == 0 or j == 0:
				dp[i][j] += 0
			elif w[i] <= j:
				dp[i][j] = max(dp[i-1][j],p[i]+dp[i-1][j-w[i]])

			else:
				dp[i][j] = dp[i-1][j]
	#print(dp)
	i = n
	j = m
	while i > 0 and j >= 0:
		if dp[i][j]== dp[i-1][j]:
			print(i," = 0")
			
		else:
			print(i," = 1")
			j = j-w[i]
		i = i-1
		#print(i,j)

p = [0,1,2,5,6]
w = [0,2,3,4,5]
knapsack(p,w,8,4)
