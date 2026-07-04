from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from core.models.base_model import BaseModel


class Project(BaseModel):
    title = models.CharField(verbose_name=_("Title"), max_length=100)
    slug = models.SlugField(
        verbose_name=_("Slug"), max_length=120, unique=True, blank=True
    )
    description = models.CharField(verbose_name=_("Description"), max_length=500)
    repository = models.URLField(verbose_name=_("Repository"))
    icon = models.CharField(
        verbose_name=_("Icon"),
        max_length=50,
        default="code",
        help_text=_("Material symbol outline icon name"),
    )
    stacks = models.ManyToManyField(
        "portfolio.Stack", related_name="projects", blank=True
    )

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
