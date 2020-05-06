J = "z"
S = "ZZZZZZz"

count = 0
for c in range(len(S)):
    for v in range(len(J)):
        if S[c] == J[v]:
            count += 1
            break
print(count)