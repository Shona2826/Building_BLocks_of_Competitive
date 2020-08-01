INF = 999
G = [[0, 9, 75, 0, 0],
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]

def prim(G):
	selected = [0] * (len(G))
	no_edge = 0
	selected[0] = True
	while (no_edge < len(G)-1):
		minimum = INF
		x,y = 0,0
		for i in range(len(G)):
			if selected[i]:
				for j in range(len(G)):
					if not selected[j] and G[i][j]:
						if minimum > G[i][j]:
							minimum = G[i][j]
							x = i
							y = j

		print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
		selected[y] = True
		no_edge += 1

prim(G)