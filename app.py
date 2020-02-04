import collections
import pymorphy2
import nltk


def save(output, tag):
    output.write('{0} {1}\n'.format(tag[0][0].normal_form, tag[1]))


if __name__ == '__main__':
    f = open('./data/input.txt', 'r')
    # Read text
    source = f.read()
    # Tokenize text
    tokens = nltk.wordpunct_tokenize(source)
    # Calculate frequencies of words
    ordered = collections.OrderedDict(sorted(collections.Counter(tokens).items(), key=lambda x: x[1], reverse=True))
    # Analyze each word
    morph = pymorphy2.MorphAnalyzer()
    tags = [(morph.parse(i), ordered[i]) for i in ordered]

    # Save result
    out = open('./data/output.txt', 'w')
    for x in tags:
        save(out, x)
    f.close()
    out.close()
