# Generated by Django 3.2.6 on 2021-10-16 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GetEasyApp', '0003_general_image_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='general',
            name='email',
            field=models.EmailField(default=1, max_length=254, verbose_name='Company official email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='general',
            name='phone',
            field=models.CharField(default=1, max_length=20, verbose_name='Company official Mobile/ Phone number'),
            preserve_default=False,
        ),
    ]
