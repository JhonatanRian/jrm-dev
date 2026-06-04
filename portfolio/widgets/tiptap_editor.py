from django import forms


class TipTapEditorWidget(forms.Widget):
    template_name = "widgets/tiptap_editor.html"

    class Media:
        # Include TipTap assets if any are needed as separate files
        pass

    def __init__(self, attrs=None):
        default_attrs = {"class": "tiptap-hidden-textarea hidden"}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)
