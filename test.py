from pyhearst import PyHearst

ph = PyHearst()

for test in ph.tests:
    print(ph.annotate_sentence(test))
