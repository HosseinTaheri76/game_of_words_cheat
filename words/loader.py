import csv

from .models import Word


def dump_data():
    with open('words/dictionary.csv', 'r', encoding='utf-8-sig') as f:
        data = csv.DictReader(f)
        Word.objects.bulk_create(Word(**row) for row in data)
