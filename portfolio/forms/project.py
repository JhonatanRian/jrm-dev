from django import forms
from portfolio.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "repository"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update(
                {
                    "class": "w-full p-2 border-2 border-black rounded-lg focus:outline-none focus:ring-2 focus:ring-neo-yellow text-black"
                }
            )
