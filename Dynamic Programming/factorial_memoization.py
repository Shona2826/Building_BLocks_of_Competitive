dp = [-1]*10
def solve(x):
	if x == 0:
		return 1
	if dp[x] != -1:
		return dp[x]
	else:
		dp[x] = x*solve(x-1)

print(solve(6))
