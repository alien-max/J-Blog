from django.db import models
from ckeditor.fields import RichTextField
from categories.models import Categories
from django.utils.translation import gettext_lazy as _
import datetime


class Blogs(models.Model):

    class Meta:
        verbose_name        = 'نوشته'
        verbose_name_plural = 'نوشته ها'

    title = models.CharField(_("عنوان"), max_length=256, null=True)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, name="دسته")
    timestamp = models.DateTimeField(_("تاریخ و زمان"), default=datetime.datetime.now())
    status = models.BooleanField(_("انتشار/پیشنویس"), default=True)
    thumbnail = models.ImageField(_("تصویر شاخص"), upload_to='thumbnails/', default='thumbnail.png')
    remark = RichTextField(_("نوشته"), null=True)

    def __str__(self):
        return f'{self.title}'
