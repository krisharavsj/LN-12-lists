from collections import Counter
test_dict = {'ide': 3, 'Gfg': 3, 'code': 2}
frequency = Counter(test_dict.values())
print(dict(frequency))
