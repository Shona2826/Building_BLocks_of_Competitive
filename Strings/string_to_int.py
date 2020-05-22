a = "123"
import functools
def string_to_int(a):
	return functools.reduce(lambda running_sum,c: running_sum * 10 + string.digits.index(c),a[a[0] == '-'],0) * (-1 if a[0] == '-' else 1)
print(string_to_int(a))