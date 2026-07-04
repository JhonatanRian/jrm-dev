from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.base_model import BaseModel

from .group_stack import GroupStack
from .project import Project


class Portfolio(BaseModel):
    section_hero = models.OneToOneField(
        "portfolio.SectionHero", on_delete=models.CASCADE, null=False
    )
    about = models.TextField()
    groups_stacks = models.ManyToManyField(GroupStack)
    projects = models.ManyToManyField(Project)
    linkedin = models.URLField(null=False)
    github = models.URLField(null=False)
    active = models.BooleanField(default=True)
    contact_email = models.EmailField()

    class Meta:
        verbose_name = _("Portfolio")
        verbose_name_plural = _("Portfolios")

    def __str__(self):
        return f"Portfolio - {self.contact_email}"

    def clean(self):
        if self.active:
            qs = Portfolio.objects.filter(active=True)
            if self.pk:
                qs = qs.exclude(pk=self.pk)
            if qs.exists():
                raise ValidationError(_("Only one portfolio can be active at a time."))

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
