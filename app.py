import collections
import pymorphy2
import nltk

def save(f:file):

if __name__ == '__main__':
    f = open('./data/input.txt')
    # Read text
    source = f.read()
    # Tokenize text
    tokens = nltk.wordpunct_tokenize(source)
    # Calculate frequencies of words
    counter = collections.Counter(tokens)
    #ordered = collections.OrderedDict(sorted(counter.items(),key= lambda x: x[1]))
    # Analyze each word
    morph = pymorphy2.MorphAnalyzer()
    tags = [morph.parse(i) for i in counter]

    # map(lambda x: , sorted(tags, ))
    f.close()

