# Generated by Django 3.2.6 on 2021-09-24 11:37

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GetEasyApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='general',
            name='about',
            field=ckeditor.fields.RichTextField(verbose_name='Site About'),
        ),
        migrations.AlterField(
            model_name='general',
            name='policy',
            field=ckeditor.fields.RichTextField(verbose_name='Enter policy'),
        ),
        migrations.AlterField(
            model_name='general',
            name='terms',
            field=ckeditor.fields.RichTextField(verbose_name='Enter terms and conditions'),
        ),
        migrations.AlterField(
            model_name='getservice',
            name='message',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Enter your message (if any)'),
        ),
        migrations.AlterField(
            model_name='services',
            name='details',
            field=ckeditor.fields.RichTextField(verbose_name='Enter a details of your service'),
        ),
        migrations.AlterField(
            model_name='services',
            name='packages',
            field=ckeditor.fields.RichTextField(verbose_name='Service Packages'),
        ),
        migrations.AlterField(
            model_name='services',
            name='required_doc',
            field=ckeditor.fields.RichTextField(verbose_name='Required Documents Information of this service'),
        ),
        migrations.AlterField(
            model_name='services',
            name='short_desc',
            field=ckeditor.fields.RichTextField(verbose_name='Short Description'),
        ),
    ]