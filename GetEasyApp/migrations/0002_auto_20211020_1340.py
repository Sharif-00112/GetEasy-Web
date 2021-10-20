# Generated by Django 3.2.6 on 2021-10-20 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GetEasyApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='general',
            name='facebook_link',
            field=models.CharField(help_text="remove 'http://' before your web address, Example: example.com", max_length=300, verbose_name='Facebook Link '),
        ),
        migrations.AlterField(
            model_name='general',
            name='instagram_link',
            field=models.CharField(help_text="remove 'http://' before your web address, Example: example.com", max_length=300, verbose_name='Instagram Link'),
        ),
        migrations.AlterField(
            model_name='general',
            name='linkedin_link',
            field=models.CharField(help_text="remove 'http://' before your web address, Example: example.com", max_length=300, verbose_name='Linkedin Link'),
        ),
        migrations.AlterField(
            model_name='general',
            name='skype_link',
            field=models.CharField(help_text="remove 'http://' before your web address, Example: example.com", max_length=300, verbose_name='Skype Link'),
        ),
        migrations.AlterField(
            model_name='general',
            name='whatsapp_link',
            field=models.CharField(max_length=300, verbose_name='Whatsapp Link/Mobile number'),
        ),
    ]