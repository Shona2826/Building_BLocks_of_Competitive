rain = [3,0,0,2,0,4]
a = rain[0]
b = rain[-1]
c = min(a,b)
total_rain = 0
for i in range(len(rain)):
	total_rain += (c-rain[i])
total_rain += abs(a-b)
print(total_rain)