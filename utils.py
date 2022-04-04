

def getText(filename,minlen):
    """
    @param filename : string containing relative path to file
    @param minlen : int, ignores sentences with less than minlen words
    
    @return a list of list of words, that is a list of sentences
    "cleanses" the text by removing punctuation, putting everything is lowercase...
    """
    
    f = open(filename,'r')
    res = []
    for line in f:
        res1 = []
        for word in line.split():
            if word.__contains__("."):
                res1.append(word.replace(".","").lower())
                if len(res1) >= minlen:
                    res.append(res1)
                    res1 = []
                else :
                    res1 = []
            else:
                res1.append(word.lower())
    return res