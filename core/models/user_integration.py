from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.base_model import BaseModel
from core.models.custom_fields import EncryptedCharField


class UserIntegration(BaseModel):
    user = models.OneToOneField("accounts.User", on_delete=models.CASCADE)
    token_jira = EncryptedCharField(
        verbose_name=_("API Key Jira"), max_length=255, null=False, blank=False
    )
    token_gemini = EncryptedCharField(
        verbose_name=_("API Key Gemini"), max_length=255, null=False, blank=False
    )

    class Meta:
        verbose_name = _("User Integration")
        verbose_name_plural = _("User Integrations")
