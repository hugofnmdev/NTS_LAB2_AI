from rng import *
from utils import *

class MarkovChain:
    def __init__(self,seed):
        self.mc = dict()
        self.rng = PseudoRNG(48271,0,seed)
        
    def train(self, text):
        """
        @param text list of list of words
        Builds the Markov Chain by creating a dictionary word -> list of possible successors, 
        with a special token for starting and ending a sentence
        """
        l = text
        nextword = {}        
        nextword["Start"] = []
        for i in range(len(l)):
            s = l[i]
            nextword["Start"].append(s[0])
            for j in range(len(s)):
                key = s[j]
                if not key in nextword:
                    nextword[key] = []
                if j+1 < len(s):
                    nextword[key].append(s[j+1])
                if j+1 == len(s):
                    nextword[key].append("End")
        self.mc = nextword
        
                    
    def generate(self):
        """
        Generates randomly a sentence
        @return a string
        """
        key = "Start"
        output = ""
        nextword = self.mc
        while key != "End":
            n = self.rng.randInt(0,len(nextword[key]))
            key = nextword[key][n]
            if key != "End":
                output += " " + key
        return output


MINLEN = 4    
SEED = 23456
generator = MarkovChain(SEED)
#generator.train(getText('corpus/asoiaf1.txt',MINLEN))
#generator.train(getText('corpus/asoiaf2.txt',MINLEN))
#generator.train(getText('corpus/asoiaf3.txt',MINLEN))

#print(generator.generate())
