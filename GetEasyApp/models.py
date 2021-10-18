import datetime
from urllib import request

from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models


# Create your models here.


class General(models.Model):
    main_title = models.CharField(max_length=300, verbose_name="Advertisement Title")
    about = RichTextField(verbose_name="Site About")
    last_edited = datetime.datetime.now()
    terms = RichTextField(verbose_name="Enter terms and conditions")
    policy = RichTextField(verbose_name="Enter policy")
    image_field = models.FileField(verbose_name="Home Background hero image", upload_to='services_images',
                                   help_text="Only PNG, JPG, JPEG format supported",
                                   validators=[FileExtensionValidator(
                                       allowed_extensions=['png', 'jpg', 'jpeg'])])
    last_author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    phone = models.CharField(max_length=20, verbose_name="Company official Mobile/ Phone number")
    email = models.EmailField(verbose_name="Company official email")

    def save(self, **kwargs):
        self.pk = self.id = 1
        if ('request') in kwargs and self.last_author is None:
            request = kwargs.pop('request')
            self.last_author = request.user
        super(General, self).save(**kwargs)

    def __str__(self):
        return self.main_title


HOME_CHOICES = (
    ("yes", "Yes"),
    ("no", "No")
)


class Services(models.Model):
    title = models.CharField(max_length=300, verbose_name="Enter a service title")
    subtitle = models.CharField(max_length=300, verbose_name="Short Title")
    short_desc = models.TextField(max_length=300, verbose_name="Short Description",
                                  help_text="Not more than 300 character")
    details = RichTextField(verbose_name="Enter a details of your service")
    required_doc = RichTextField(verbose_name="Required Documents Information of this service")
    created_time = datetime.datetime.now()
    packages = RichTextField(verbose_name="Service Packages")
    image = models.FileField(verbose_name="Service image", upload_to='services_images',
                             help_text="Only PNG, JPG, JPEG format supported",
                             validators=[FileExtensionValidator(
                                 allowed_extensions=['png', 'jpg', 'jpeg'])])
    home_shown = models.CharField(max_length=100, verbose_name="Is shown in home?", choices=HOME_CHOICES)
    service_sequence = models.IntegerField("Services ordering integer", unique=True)

    def __str__(self):
        return str(self.service_sequence) + " " + self.title


class GetService(models.Model):
    service = models.ForeignKey(Services, on_delete=models.DO_NOTHING, verbose_name="Select Service")
    client_name = models.CharField(max_length=300, verbose_name="Enter Your name")
    phone_no = models.CharField(max_length=300, verbose_name="Enter your phone number")
    district = models.CharField(max_length=300, verbose_name="Enter your district")
    message = RichTextField(verbose_name="Enter your message (if any)", null=True, blank=True)

    def __str__(self):
        return self.service.title + " --> " + self.client_name


class Contact(models.Model):
    pass
