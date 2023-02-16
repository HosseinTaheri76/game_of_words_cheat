import itertools


alpha_score = {
    'آ': 4,
    'ا': 1,
    'ب': 0,
    'پ': 0,
    'ت': 0,
    'ث': 0,
    'ج': 0,
    'چ': 0,
    'ح': 0,
    'خ': 0,
    'د': 0,
    'ذ': 0,
    'ر': 0,
    'ز': 0,
    'ژ': 0,
    'س': 0,
    'ش': 0,
    'ص': 0,
    'ض': 0,
    'ط': 0,
    'ظ': 0,
    'ع': 0,
    'غ': 0,
    'ف': 0,
    'ق': 0,
    'ک': 0,
    'گ': 0,
    'ل': 0,
    'م': 0,
    'ن': 0,
    'و': 0,
    'ه': 0,
    'ی': 0
}


def get_combinations(char_list):
    list_len = len(char_list)
    if list_len < 3:
        raise ValueError('length of words must be greater than 3.')
    actual_length = list_len if list_len < 7 else 7
    chain = itertools.chain.from_iterable((itertools.permutations(char_list, r=i) for i in range(3, actual_length)))
    return map(lambda x: ''.join(x), chain)
