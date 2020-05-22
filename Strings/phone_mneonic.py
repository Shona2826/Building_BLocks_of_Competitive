MAPPIG = ('0','1','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ')
def phone_memonic(p_number):
	def phone_memonic_helper(digit):
		if digit == len(p_number):
			mnemonics.append(''.join(partial_mnemonic))
		else:
			for c in MAPPIG[int(p_number[digit])]:
				partial_mnemonic[digit] = c
				phone_memonic_helper(digit+1)
	mnemonics,partial_mnemonic = [] , [0]*len(p_number)
	phone_memonic_helper(0)
	return mnemonics

print(phone_memonic('2276696'))

