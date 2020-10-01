import os
import pycrfsuite

from .featurizer import Featurizer

TAGGER = pycrfsuite.Tagger()
TAGGER.open("%s/artifacts/crf3_mix.crfsuite2" % os.path.dirname(__file__))

DUMMY_TOKEN = "<SSG_SPECIAL>"

N = 3
FEATURIZER = Featurizer(N=N)

def decode(txt:list, tag:list):
    res = []
    for c, t in zip(list(txt), tag):
        if t == "1": 
            res.append(DUMMY_TOKEN)
        res.append(c)
    return "".join(res).split(DUMMY_TOKEN)

def syllable_tokenize(txt:str, sep:str="~"):
    feature = FEATURIZER.featurize(
        txt, return_type='list', padding=True, indiv_char=True
    )

    tag = TAGGER.tag(feature['X'])

    return decode(txt, tag)