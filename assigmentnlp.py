import re
import nltk
from nltk.corpus import brown
nltk.download('brown')

learned_sents = brown.sents(categories='learned')

# text_file = open("data.txt", "w")
#
# for sents in learned_sents:
#     text_file.write(" ".join(sents))
#     text_file.write("\n")
#
# text_file.close()


def trigram(corpus, str):
    dict = {}
    len_of_str = len(str)
    for s in corpus:
        if len(s) > 2:
            for i in range(0, len(s)):
                if i == len(s) - 2:
                    break
                if s[i].lower() == str[len_of_str - 2].lower() and s[i + 1].lower() == str[len_of_str - 1].lower():
                    dict[s[i + 2]] = dict.get(s[i + 2], 0) + 1

    list_of_words = sorted(dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)

    if len(list_of_words) > 4:
        return list_of_words[0:5]
    else:
        return list_of_words


def output(x):
    x = " ".join(x.split())
    list_of_seq = trigram(learned_sents, re.split("\\W+", x))

    out = ''
    for tuble in list_of_seq:
        out += x + ' ' + tuble[0] + '\n'

    return out

