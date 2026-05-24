# pyrefly: ignore [untyped-import]
from django.db import models
# pyrefly: ignore [untyped-import]
from django.utils.translation import gettext_lazy as _

from core.models.base_model import BaseModel


class Stack(BaseModel):
    name = models.CharField(verbose_name=_("Name"), max_length=100)

    class Meta:
        verbose_name = _("Stack")
        verbose_name_plural = _("Stacks")

    def __str__(self):
        return self.name


class GroupStack(BaseModel):
    title = models.CharField(verbose_name=_("Title"), max_length=100)
    stacks = models.ManyToManyField(Stack, verbose_name=_("Stacks"))

    class Meta:
        verbose_name = _("Section Stack")
        verbose_name_plural = _("Sections Stacks")

    def __str__(self):
        return self.title
