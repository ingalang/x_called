import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()
import re
import argparse




def get_lines(filepath):
    with open(filepath, 'r') as infile:
        for line in infile:
            yield line.strip('\n\r')


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--infile', required=True, type=str)
    parser.add_argument('--outfile', required=True, type=str)

    args = parser.parse_args()
    infile, outfile = args.infile, args.outfile

    url_reg = re.compile('(http [\s\W]*|www [\s\W]*)\S+|<p>|[@]+\w*|^\s+')
    whitespace_reg = re.compile('\s+')

    NERs = set(())

    for line in get_lines(infile):
        cleaned_line = re.sub(whitespace_reg, ' ', re.sub(url_reg, '', line))
        processed_line = nlp(cleaned_line)
        NERs.update([(X.text, X.label_) for X in processed_line.ents])

    print(NERs)

    with open(outfile, 'w') as outfile:
        for n in NERs:
            outfile.write(str(n) + "\n")


if __name__ == '__main__':
    main()

