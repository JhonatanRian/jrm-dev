from django import forms

from portfolio.models import Stack


class StackForm(forms.ModelForm):
    class Meta:
        model = Stack
        fields = ["name"]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name:
            qs = Stack.objects.filter(name__iexact=name)
            if self.instance and self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                self.add_error("name", "Já existe uma stack cadastrada com este nome.")
        return name
