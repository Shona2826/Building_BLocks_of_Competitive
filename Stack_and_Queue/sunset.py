def sunset(sequence):
	bwh = collections.namedtuple('bwh',('id','heigth'))
	candidates = []
	for b,bh in enumerate(sequence):
		while candidates and bh >= candidates[-1].height:
			candidates.pop()
		candidates.append(bwh(b,bh))
	return [candidates.id for candidates in reversed(candidates)]