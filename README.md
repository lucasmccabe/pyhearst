# pyhearst

`pyhearst` is a Python implementation of the Hearst patterns for identifying hypernym-hyponym pairs.

In progress.

## Table of contents
* [Setup](#setup)
* [Usage](#usage)
* [References](#references)
* [License](#license)

## Setup
pip later. For now, stick pyhearst.py locally and run:

```python
from pyhearst import PyHearst
```

## Usage
To extract pairs from a text string:

```python
ph = PyHearst()
text = 'works by such individuals as Marti A. Hearst, P. J. Proudhon, and Esther Duflo'
for pair in ph.extract_patterns(text): print(pair)
```

## References
-Automatic Acquisition of Hyponyms from Large Text Corpora [(Hearst 1992)](https://www.aclweb.org/anthology/C92-2082/).

## License
[MIT](https://choosealicense.com/licenses/mit/)
