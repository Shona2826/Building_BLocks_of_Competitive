
import functools
s = "ZZ"
def decode(s):
	return functools.reduce(lambda result,c: result * 26 + ord(c) - ord('A') + 1,s,0)

print(decode(s))