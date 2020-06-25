class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        n =1 
        while self.stack:
            val,num = self.stack[-1]
            if price < val:
                self.stack.append((price,n))
                return n
            else:
                n += num
                self.stack.pop()
        self.stack.append((price,n))
        
        return n
        
        