from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.base_model import BaseModel

from .stack import Stack


class GroupStack(BaseModel):
    title = models.CharField(verbose_name=_("Title"), max_length=100)
    stacks = models.ManyToManyField(Stack, verbose_name=_("Stacks"))

    class Meta:
        verbose_name = _("Section Stack")
        verbose_name_plural = _("Sections Stacks")

    def __str__(self):
        return self.title
