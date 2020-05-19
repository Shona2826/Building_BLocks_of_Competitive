s = "moim"
def is_palindromic(s):
	return all(s[i] == s[~i] for i in range(len(s)//2))

print(is_palindromic(s))