from django import forms
from django_select2.forms import Select2MultipleWidget
from portfolio.models import GroupStack, Stack


class GroupStackForm(forms.ModelForm):
    stacks = forms.ModelMultipleChoiceField(
        queryset=Stack.objects.all(),
        widget=Select2MultipleWidget(
            attrs={
                "class": "w-full p-2 border-2 border-black rounded-lg focus:outline-none focus:ring-2 focus:ring-neo-yellow text-black"
            }
        ),
        label="Stacks",
        required=False,
    )

    class Meta:
        model = GroupStack
        fields = ["title", "stacks"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update(
            {
                "class": "w-full p-2 border-2 border-black rounded-lg focus:outline-none focus:ring-2 focus:ring-neo-yellow text-black"
            }
        )
