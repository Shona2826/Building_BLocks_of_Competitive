a = [[1,2],[2,2],[3,4],[4,5],[5,6],[6,7]]
def checkStraightLine(coordinates) -> bool:
    if len(coordinates) == 2:
        return True
    else:
        p1,p2 = coordinates[0], coordinates[1]
        if p2[0] == p1[0]:
            for i in range(3, len(coordinates)):
                if coordinates[i][0] != p2[0]:
                    return False
        else:
            m = (p2[1] - p1[1]) / (p2[0] - p1[0])
            c = p2[1] - m * p2[0]

            for i in range(3, len(coordinates)):
                if coordinates[i][1] != m * coordinates[i][0] + c:
                    return False
        return True

print(checkStraightLine(a))	