import itertools

from .models import Word

alpha_score = {
    'آ': 4,
    'ا': 1,
    'ب': 2,
    'پ': 5,
    'ت': 2,
    'ث': 6,
    'ج': 4,
    'چ': 5,
    'ح': 4,
    'خ': 4,
    'د': 2,
    'ذ': 6,
    'ر': 2,
    'ز': 3,
    'ژ': 6,
    'س': 3,
    'ش': 3,
    'ص': 5,
    'ض': 5,
    'ط': 5,
    'ظ': 6,
    'ع': 4,
    'غ': 6,
    'ف': 4,
    'ق': 4,
    'ک': 3,
    'گ': 4,
    'ل': 3,
    'م': 1,
    'ن': 1,
    'و': 1,
    'ه': 2,
    'ی': 1
}


def get_combinations(char_list):
    list_len = len(char_list)
    if list_len < 3:
        raise ValueError('length of words must be greater than 3.')
    if '*' in char_list:
        char_list.remove('*')
        char_list.extend(alpha_score.keys())
    actual_length = list_len if list_len < 7 else 7
    chain = itertools.chain.from_iterable((itertools.permutations(char_list, r=i) for i in range(3, actual_length + 1)))
    return map(lambda x: ''.join(x), chain)


def calculate_score(word):
    return len(word) + sum(alpha_score[a] for a in word)


def get_valid_combos_sort_by_score(alpha_list):
    combos = get_combinations(alpha_list)
    valid_combos = list(Word.objects.filter(name__in=combos))
    valid_combos.sort(key=lambda w: calculate_score(w.name), reverse=True)
    return valid_combos

