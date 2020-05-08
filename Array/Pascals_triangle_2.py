rowIndex = 3
data, index = [], 0
while index <= rowIndex:
    if index == 0:
        data.append([1])
    
    elif index>1:
        p,j = [1],1
        while j< index-1:
            k = data[index-1][j-1] + data[index-1][j]
            ##print(k)
            p.append(k)
            j = j+1
        p.append(1)
        data.append(p)
    elif index == 1:
        data.append([1,1])
    ##print(index)            
    index +=1
    print(data)