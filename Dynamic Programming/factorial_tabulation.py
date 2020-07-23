dp = []
dp.append(1)
def solve(x):
	for i in range(1,x):
		dp.append(dp[i-1]*i)
	return dp

print(solve(5))