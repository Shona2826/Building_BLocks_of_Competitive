prices = [7,1,5,3,6,4]

buy = 0
sell = 0
maxp = 0
count = 0
i = 0
while i<len(prices)
#for i in range(len(prices) - 1):

	#print(i)
	while i<len(prices)-1 and prices[i] >= prices[i+1]:
		i += 1
		count +=1
	buy = prices[i]
	#print(buy)
	while i<len(prices)-1 and prices[i] <= prices[i+1]:
		i +=1
		count += 1
	sell = prices[i]
	#print(sell)
	maxp += sell - buy
	print(maxp)
	#print(i)