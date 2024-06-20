from django import forms
from .models import Domain, Review

class DomainForm(forms.ModelForm):
    class Meta:
        model = Domain
        fields = ['name']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['domain', 'review_text']

class SearchForm(forms.Form):
    name = forms.CharField(max_length=255, label='Search Domain')
