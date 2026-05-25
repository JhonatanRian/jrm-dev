from django import forms
from django_select2.forms import Select2MultipleWidget
from portfolio.models import Portfolio, GroupStack, Project


class PortfolioForm(forms.ModelForm):
    groups_stacks = forms.ModelMultipleChoiceField(
        queryset=GroupStack.objects.all(),
        widget=Select2MultipleWidget(
            attrs={
                "class": "w-full p-2 border-2 border-black rounded-lg focus:outline-none focus:ring-2 focus:ring-neo-yellow text-black"
            }
        ),
        label="Seções Stack (Groups Stacks)",
        required=False,
    )
    projects = forms.ModelMultipleChoiceField(
        queryset=Project.objects.all(),
        widget=Select2MultipleWidget(
            attrs={
                "class": "w-full p-2 border-2 border-black rounded-lg focus:outline-none focus:ring-2 focus:ring-neo-yellow text-black"
            }
        ),
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name not in ["groups_stacks", "projects", "active"]:
                field.widget.attrs.update(
                    {
                        "class": "w-full p-2 border-2 border-black rounded-lg focus:outline-none focus:ring-2 focus:ring-neo-yellow text-black"
                    }
                )
            elif name == "active":
                field.widget.attrs.update(
                    {
                        "class": "w-6 h-6 border-2 border-black rounded focus:ring-0 focus:ring-offset-0 text-black accent-black cursor-pointer"
                    }
                )
