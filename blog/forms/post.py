from django import forms
from django_select2.forms import Select2MultipleWidget

from blog.models import Post, Tag
from portfolio.widgets import TipTapEditorWidget


class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=Select2MultipleWidget(attrs={"class": "w-full"}),
        label="Tags",
        required=False,
    )

    class Meta:
        model = Post
        fields = ["title", "content", "featured_image", "tags"]
        widgets = {
            "content": TipTapEditorWidget(),
        }
