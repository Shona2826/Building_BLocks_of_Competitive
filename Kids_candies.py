candies = [2,3,5,1,3]
extraCandies = 1
maxp = max(candies)
res = []
for i in range(len(candies)):
    if candies[i] + extraCandies >= maxp:
       	res.append("true")
    else:
        res.append("false")
print(res)
        