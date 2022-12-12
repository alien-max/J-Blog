from django.db import models
from django.utils.translation import gettext_lazy as _


class Ads(models.Model):

    class Meta:
        verbose_name        = 'تبلیغ'
        verbose_name_plural = 'تبلیغات'

    title = models.CharField(_("عنوان"), max_length=256)
    link = models.CharField(_("لینک تبلیغ"), max_length=256, default="---")
    picture = models.ImageField(_("بنر"), blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

