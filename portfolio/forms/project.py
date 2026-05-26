from django import forms
from django_select2.forms import Select2MultipleWidget

from portfolio.models import Project, Stack


class ProjectForm(forms.ModelForm):
    stacks = forms.ModelMultipleChoiceField(
        queryset=Stack.objects.all(),
        widget=Select2MultipleWidget(attrs={"class": "w-full"}),
        label="Stacks",
        required=False,
    )

    class Meta:
        model = Project
        fields = ["title", "description", "repository", "icon", "stacks"]
