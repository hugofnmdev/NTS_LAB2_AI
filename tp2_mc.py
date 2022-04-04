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
        pass
        
                    
    def generate(self):
        """
        Generates randomly a sentence)
        @return a string
        """
        pass


MINLEN = 4    
SEED = 23456
generator = MarkovChain(SEED)
#generator.train(getText('corpus/asoiaf1.txt',MINLEN))
#generator.train(getText('corpus/asoiaf2.txt',MINLEN))
#generator.train(getText('corpus/asoiaf3.txt',MINLEN))

#print(generator.generate())
