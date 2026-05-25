from django import forms

from portfolio.models import Stack


class StackForm(forms.ModelForm):
    class Meta:
        model = Stack
        fields = ["name"]
