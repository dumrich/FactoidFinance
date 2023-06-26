from django.contrib.auth import get_user_model
from django import forms


class CheckboxForm(forms.Form):
    OPTIONS = [
        ('healthcare', 'Healthcare'),
        ('financial-services', 'Financial Services'),
        ('consumer-discretionary', 'Consumer'),
        ('information-technology', 'Health'),
        ('consumer-defensive', 'Defensive'),
        ('energy', 'Energy'),
        ('communication-services', 'Communication'),
        ('basic-materials', 'Materials'),
        ('industrials', 'Industrials'),
        ('basic-materials', 'Materials'),
    ]

    options = forms.MultipleChoiceField(
        choices=OPTIONS,
        widget=forms.CheckboxSelectMultiple(
            attrs={'class': 'form-check-input'}),
    )
