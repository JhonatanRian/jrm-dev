from django import forms

from portfolio.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "repository"]