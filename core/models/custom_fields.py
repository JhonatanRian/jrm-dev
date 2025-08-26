from django.db import models
from encrypted_model_fields.fields import EncryptedCharField as custom_EncryptedCharField

class EncryptedCharField(custom_EncryptedCharField, models.CharField):
    pass
