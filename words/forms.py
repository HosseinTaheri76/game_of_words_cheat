from django import forms


class AlphabetForm(forms.Form):
    alpha = forms.CharField()
