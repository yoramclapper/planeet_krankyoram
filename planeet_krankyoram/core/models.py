from django.db import models


class AppsLib(models.Model):
    app_name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    show = models.BooleanField()

    class Meta:
        verbose_name = 'Apps lib'
        verbose_name_plural = 'Apps lib'

    def __str__(self):
        return self.display_name
