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
The following table shows the performance of the current best model (the first row), which is in use, and compares it against other models. The test set is from the same corpus and is roughly 780,000 characters long (excluding syllable and sentence delimiters).

| Model  | Features                   | Window Size                       | F1 (SL) | Precision (SL) | Recall (SL) | F1 (CL) | Precision (CL) | Recall (CL) |
|--------|----------------------------|-----------------------------------|---------|----------------|-------------|---------|---------------|-------------|
| CRF    | IndivChar + Sliding Window | 4 (IndivChar), 4 (Sliding Window) | 0.9854  | 0.9876         | 0.9832      | 0.9935  | 0.9958        | 0.9854      |
| CRF    | IndivChar + Ngram\*        | 4 (IndivChar), 3 (Ngram\*)        | 0.9809  | 0.9848         | 0.9771      | 0.9917  | 0.9956        | 0.9878      |
| CRF    | IndivChar + Sliding Window | 3 (IndivChar), 3 (Sliding Window) | 0.9804  | 0.9831         | 0.9778      | 0.9909  | 0.9936        | 0.9882      |
| MaxEnt | IndivChar + Sliding Window | 4 (IndivChar), 4 (Sliding Window) | 0.9772  | 0.9819         | 0.9725      | 0.9899  | 0.9946        | 0.9852      |
| MaxEnt | Sliding Window             | 4                                 | 0.9731  | 0.9822         | 0.9642      | 0.9871  | 0.9963        | 0.9780      |

\*Ngram features are not sliding window features but refer only to sequences of 3 characters on the left and right sides of a given character.

\*\*SL = Syllable level, CL = Character level
