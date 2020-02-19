import collections
import string
import pymorphy2
import nltk
from langdetect import detect
from nltk.corpus import stopwords


# Write tag's fields to the output
def save(output, tag):
    output.write('{0} {1}\n'.format(tag[0], tag[1]))


if __name__ == '__main__':
    # Read text
    f = open('./data/input.txt', 'r')
    source = f.read()
    # Create stopwords dictionary from nltk
    stop_words = set(stopwords.words('english'))

    # Tokenize text
    tokens = nltk.wordpunct_tokenize(source)
    # Filter stop words
    tokens = [i for i in tokens if (i not in string.punctuation and i.lower() not in stop_words)]

    # Analyze each word
    morph = pymorphy2.MorphAnalyzer()
    # Convert tokens to tags
    tags = [morph.parse(i) for i in tokens]
    # Create ordered dict key=tag, value=freq
    ordered = collections.OrderedDict(
        sorted(
            # Convert each token to normal form and count frequency
            collections.Counter([t[0].normal_form for t in tags]).items(),
            # Compare each element by frequency
            key=lambda t2: t2[1],
            # Order by desc
            reverse=True
        )
    )

    # Save result
    out = open('./data/output.txt', 'w')
    for v in ordered:
        save(out, (v, ordered[v]))
    out.close()

    # Create stremmer
    stemmer_en = nltk.SnowballStemmer('english')

    # Stem each token
    singles = [stemmer_en.stem(plural_en) for plural_en in tokens]
    # Create ordered dict key=single, value=freq
    ordered_stem = collections.OrderedDict(
        sorted(
            # Convert singles to the ordered dict frequency
            collections.Counter([t for t in singles]).items(),
            # Compare each element by frequency
            key=lambda t2: t2[1],
            # Order by desc
            reverse=True
        )
    )
    out = open('./data/output_stem.txt', 'w')
    for v in ordered_stem:
        save(out, (v, ordered_stem[v]))
    out.close()
    f.close()
