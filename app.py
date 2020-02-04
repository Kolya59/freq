import collections
import pymorphy2
import nltk


def save(output, tag):
    output.write('{0} {1}\n'.format(tag[0], tag[1]))


if __name__ == '__main__':
    # Read text
    f = open('./data/input.txt', 'r')
    source = f.read()
    # Tokenize text
    tokens = nltk.wordpunct_tokenize(source)
    # Analyze each word
    morph = pymorphy2.MorphAnalyzer()
    tags = [morph.parse(i) for i in tokens]
    # Calculate frequencies of words
    ordered = collections.OrderedDict(
        sorted(
            collections.Counter([t[0].normal_form for t in tags]).items(),
            key=lambda t2: t2[1],
            reverse=True
        )
    )

    # Save result
    out = open('./data/output.txt', 'w')
    for v in ordered:
        save(out, (v, ordered[v]))
    f.close()
    out.close()
