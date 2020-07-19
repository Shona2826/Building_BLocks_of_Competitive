class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        children,pars=collections.defaultdict(set),collections.defaultdict(set)
        for child,par in prerequisites:
	        children[par].add(child)
	        pars[child].add(par)

        q=[x for x in range(numCourses) if x not in pars]
        out=[]
        while q:
	        cur=q.pop()
	        out.append(cur)
	        for child in children[cur]:
		        pars[child].remove(cur)
		        if not pars[child]:q.append(child)


        return out if len(out)==numCourses else []