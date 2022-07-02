from dal import autocomplete
from django import forms
from django.http import HttpRequest

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy


def get_choice_list():
    return ['France', 'Fiji', 'Finland', 'Switzerland']


class CountryForm(forms.Form):
    country = autocomplete.Select2ListChoiceField(
        choice_list=get_choice_list,
        widget=autocomplete.ListSelect2(
            url=reverse_lazy('country-list-autocomplete'),
            attrs={'data-minimum-input-length': 0, 'data-theme': 'bootstrap-5', 'data-allow-clear': True}
        )
    )


class CountryAutocompleteFromList(autocomplete.Select2ListView):
    def get_list(self):
        return get_choice_list()


def home(request: HttpRequest):
    return render(request, 'home.html', {'form': CountryForm()})
