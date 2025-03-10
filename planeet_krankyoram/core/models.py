from django.db import models
from .utils import get_my_apps
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


def validate_url(value):
    if value[0] + value[-1] != '//':
        raise ValidationError("URL should start and end with '/'")
    else:
        return value


class AppsLib(models.Model):
    app_name = models.CharField(max_length=255, choices=get_my_apps())
    display_name = models.CharField(max_length=255)
    url = models.CharField(
        max_length=255,
        validators=[
            validate_url,
            RegexValidator(
                regex=r'[^A-Za-z0-9_/]',
                message=f"URL contains invalid characters not in '[A-Za-z0-9_/]'",
                inverse_match=True
            )
        ]
    )
    show = models.BooleanField()

    class Meta:
        verbose_name = 'Apps lib'
        verbose_name_plural = 'Apps lib'

    def __str__(self):
        return self.display_name
