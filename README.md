# CRF syllable segmenter for Thai
[![Build Status](https://www.travis-ci.com/ponrawee/ssg.svg?branch=master)](https://www.travis-ci.com/ponrawee/ssg)

`ssg` is a syllable segmenter for Thai using Conditional Random Fields. This is part of work from [Natural Language Processing Lab @Chula](https://attapol.github.io/lab.html), under the supervision of Dr. Attapol Thamrongrattanarit.

## Installation
```console
foo@bar~$: pip install ssg
```

## Usage
To use,

```python
from ssg import syllable_tokenize
syllable_tokenize('ทดสอบ') # returns ['ทด', 'สอบ']
```

`ssg` also comes with its own CLI. 

```console
foo@bar~$: ssg-cli PATH_TO_INPUT PATH_TO_OUTPUT
```

## Model
The model itself is stored in `ssg/artifacts/crf3_mix.crfsuite2`. 

### Data
The dataset used for training is a 5,600,000-character human-annotated subcorpus of the [Thai National Corpus](http://www.arts.chula.ac.th/~ling/tnc3/), trained using [python-crfsuite](https://pypi.org/project/python-crfsuite/)

### Parameters
- L1 penalty: `1.0` 
- L2 penalty: `1e-3`
- Includes possible transitions that are not observed (`features.possible_transitions` is set to `True`)

## Features
- Sliding window features (all possible character (N-1)-gram on both sides of a potential boundary 
up to a radius of N on both sides)
- Individual character features (each of the characters surrounding a potential boundary within the window of size N)

## Performance
--- to be updated ---
