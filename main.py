import itertools


def get_alphabets():
    alphabets = []


scope = ['آ', 'س', 'ا', 'ب', 'ی', 'غ', 'ژ', 'ر']
length = len(scope)
chain = itertools.chain.from_iterable((itertools.permutations(scope, r=i) for i in range(3, 7)))
map_chain = map(lambda x: ''.join(x), chain)
