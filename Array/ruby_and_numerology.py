n = int(input())
l = [] 
for i in range(n):
    l.append(int(input()))
#print(l)
b = []
d = l[:]
# print(d)
d.sort(reverse=True)
# print(d)
#print(sorted(l))
if l == d or l == sorted(l):
    print("Yes")
    b = [-1 for i in range(len(l))]
else:
    b = []
    for i in range(len(l)):
        c = []
        # print("cbjbvhj",b)
        for j in range(i+1,len(l)):
            if len(c) == 0 and l[i] < l[j]:
                c.append(l[j])
            if len(c) == 1 and l[j]<c[0]:
                # print("bdchdgeh",b)
                b.append(l[j])
                # print("yesss",b)
                c.pop()
                break
        if len(b)!= i+1:
            b.append(-1)
for i in b:
    print(i,end=" ")