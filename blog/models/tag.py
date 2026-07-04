from django.db import models
from django.utils.text import slugify

from core.models.base_model import BaseModel


class Tag(BaseModel):
    name = models.CharField("Nome", max_length=100, unique=True)
    slug = models.SlugField(
        "Slug", max_length=100, unique=True, db_index=True, blank=True
    )

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
