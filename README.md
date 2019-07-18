# CRF syllable segmenter for Thai

## Model
The model is stored in `ssg/artifacts/crf3_mix.crfsuite2`.

### Data
Trained on a human-annotated subcorpus of the [Thai National Corpus](http://www.arts.chula.ac.th/~ling/tnc3/)
using [python-crfsuite](https://pypi.org/project/python-crfsuite/)

### Parameters
- L1 penalty: `1.0` 
- L2 penalty: `1e-3`
- Includes possible transitions that are not observed (`features.possible_transitions` is set to `True`)

## Features
- Sliding window features (all possible character trigrams on both sides of a given character 
up to a radius of 4 on both sides)
- Individual character features
