from pyhearst import PyHearst

ph = PyHearst()


for test in ph.tests:
    print(test)
    print(ph.extract_patterns(test), '\n')
