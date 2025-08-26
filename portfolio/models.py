from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.base_model import BaseModel


class SectionHero(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    class Meta:
        verbose_name = _("Section Hero")
        verbose_name_plural = _("Sections Heroes")

    def __str__(self):
        return self.title


class Stack(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("Stack")
        verbose_name_plural = _("Stacks")

    def __str__(self):
        return self.name


class GroupStack(models.Model):
    title = models.CharField(max_length=100)
    stacks = models.ManyToManyField(Stack)

    class Meta:
        verbose_name = _("Section Stack")
        verbose_name_plural = _("Sections Stacks")

    def __str__(self):
        return self.title


class Project(BaseModel):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    repository = models.URLField()

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return self.title


class Portfolio(BaseModel):
    section_hero = models.OneToOneField(
        SectionHero, on_delete=models.CASCADE, null=False
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
