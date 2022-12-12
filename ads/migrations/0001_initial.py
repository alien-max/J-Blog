# Generated by Django 4.1.4 on 2022-12-12 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='عنوان')),
                ('link', models.CharField(default='---', max_length=256, verbose_name='لینک تبلیغ')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='', verbose_name='بنر')),
            ],
            options={
                'verbose_name': 'تبلیغ',
                'verbose_name_plural': 'تبلیغات',
            },
        ),
    ]
