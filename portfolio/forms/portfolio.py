from django import forms
from django_select2.forms import Select2MultipleWidget

from portfolio.models import GroupStack, Portfolio, Project


class PortfolioForm(forms.ModelForm):
    groups_stacks = forms.ModelMultipleChoiceField(
        queryset=GroupStack.objects.all(),
        widget=Select2MultipleWidget(attrs={"class": "w-full"}),
        label="Seções Stack (Groups Stacks)",
        required=False,
    )
    projects = forms.ModelMultipleChoiceField(
        queryset=Project.objects.all(),
        widget=Select2MultipleWidget(attrs={"class": "w-full"}),
        label="Projetos",
        required=False,
    )

    class Meta:
        model = Portfolio
        fields = [
            "about",
            "groups_stacks",
            "projects",
            "linkedin",
            "github",
            "contact_email",
            "active",
        ]
