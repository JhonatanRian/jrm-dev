from django import forms
from django_select2.forms import Select2MultipleWidget

from portfolio.models import GroupStack, Stack


class GroupStackForm(forms.ModelForm):
    stacks = forms.ModelMultipleChoiceField(
        queryset=Stack.objects.all(),
        widget=Select2MultipleWidget(attrs={"class": "w-full"}),
        label="Stacks",
        required=False,
    )

    class Meta:
        model = GroupStack
        fields = ["title", "stacks"]
