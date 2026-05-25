from django.contrib.auth.mixins import LoginRequiredMixin

from django.forms import Form, fields, widgets

from django.views.generic import TemplateView

from portfolio.models import Project, Stack


class FormExample(Form):
    name = fields.CharField(label="Name", max_length=100, help_text="Enter your name")
    email = fields.EmailField(
        label="Email", max_length=100, help_text="Enter your email"
    )
    email = fields.EmailField(
        label="Email", max_length=100, help_text="Enter your email"
    )
    link = fields.URLField(label="Link", max_length=200, help_text="Enter a URL")
    active = fields.BooleanField(label="Active", required=False, help_text="Is active?")
    qtd = fields.IntegerField(
        label="Quantity", min_value=0, max_value=1000, help_text="Enter a quantity"
    )
    percent = fields.FloatField(
        label="Percent", min_value=0.0, max_value=100.0, help_text="Enter a percentage"
    )
    total = fields.DecimalField(
        label="Total", max_digits=10, decimal_places=2, help_text="Enter a total amount"
    )
    date = fields.DateField(
        label="Date and Time",
        help_text="Enter date and time",
        widget=widgets.DateInput(attrs={"type": "date"}),
    )
    date_time = fields.DateTimeField(label="Date and Time", help_text="Enter date")
    duration = fields.DurationField(label="Duration", help_text="Enter duration")
    file = fields.FileField(label="File", help_text="Upload a file")
    choice = fields.ChoiceField(
        label="Choices", choices=((1, "1"), (0, "0")), help_text="Select a choice"
    )
    multiple_choice = fields.MultipleChoiceField(
        label="Multiple Choices",
        choices=((1, "1"), (0, "0"), (2, "2")),
        help_text="Select multiple choices",
    )


class PainelView(LoginRequiredMixin, TemplateView):
    template_name = "core/painel/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_example"] = FormExample()
        context["stack_count"] = Stack.objects.count()
        context["project_count"] = Project.objects.count()
        return context
