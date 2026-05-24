# pyrefly: ignore [untyped-import]
from django.db import models
# pyrefly: ignore [untyped-import]
from django.utils.translation import gettext_lazy as _

from core.models.base_model import BaseModel


class SectionHero(BaseModel):
    title = models.CharField(verbose_name=_("Title"), max_length=100)
    subtitle = models.CharField(verbose_name=_("Subtitle"), max_length=50)
    description = models.CharField(verbose_name=_("Description"), max_length=500)

    class Meta:
        verbose_name = _("Section Hero")
        verbose_name_plural = _("Sections Heroes")

    def __str__(self):
        return self.title
