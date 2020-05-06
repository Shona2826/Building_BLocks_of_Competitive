prices = [7,6,4,3,1]

left = 0
maxp = 0
for right in range(left + 1, len(prices)):
	while prices[left] > prices[right]:
		left +=1
		if right == len(prices)-1:
			break

	if prices[right] - prices[left]>maxp:
		maxp = prices[right] - prices[left] 
	else:
		maxp = maxp
print(maxp)
