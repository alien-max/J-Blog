from django.db import models
from django.utils.translation import gettext_lazy as _


class Categories(models.Model):

    class Meta:
        verbose_name        = 'دسته'
        verbose_name_plural = 'دسته ها'

    name = models.CharField(_("نام دسته"), max_length=256, null=True)

    def __str__(self):
        return f'{self.name}'

