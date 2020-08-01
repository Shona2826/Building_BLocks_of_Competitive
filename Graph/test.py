def check_max(three_stones):
	return max(three_stones, key=three_stones.count)

def solution(n, stones):
	i = 0
	temp = list()
	while True:
		three_stones = stones[i:i+3]

		# IF all are same
		if len(set(three_stones)) == 1: 
			if len(stones) == 3:
				return "N"
			temp.append(stones.pop(0))

		# IF all not same
		else:
			letter = check_max(three_stones)
			stones = stones[i+2:]
			stones[0] = letter
			# stones = temp + stones
			if len(stones) == 1:
				return "Y"

t = int(input())
c = 1
while t:
	no_stones = int(input())
	stones = str(input())
	stones = [x for x in stones]
	print(f"Case #{c}: {solution(no_stones,stones)}")

	c+= 1
	t-= 1
