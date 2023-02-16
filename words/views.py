from django.shortcuts import render

from .forms import AlphabetForm
from .tools import get_valid_combos_sort_by_score


def process_alphabets(request):
    result = None
    form = AlphabetForm(request.POST or None)
    if form.is_valid():
        alphabets = form.cleaned_data['alpha'].split(' ')
        alphabets = list(map(lambda a: a.strip(), alphabets))
        result = get_valid_combos_sort_by_score(alphabets)
    return render(request, 'index.html', {'form': form, 'result': result})
