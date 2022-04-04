class PseudoRNG:
    
    def __init__(self,a,c,val,m = 2147483647):
        self.m = m
        self.a = a
        self.c = c
        self.val = val

    def nextInt(self):
        self.val = (self.val*self.a+self.c) % self.m
    
    def randInt(self,inf,sup):
        x = self.val
        self.nextInt()
        return inf + int(x/self.m * (sup-inf))

