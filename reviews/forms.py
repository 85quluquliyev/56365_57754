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
