from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models
from uuid import uuid4
import os


def get_filename_ext(filepath):
    basename = os.path.basename(filepath)
    name, ext = os.path.splitext(basename)
    return name, ext


def upload_user_pic(instance, file):
    name, ext = get_filename_ext(file)
    random_str = str(uuid4()).split("-")[0]
    final_name = f"profile_pictures/{instance.username}/{random_str}{ext}"
    return final_name


def validate_image_size(img):
    file_size = img.size
    limit_mb = 5

    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError(_(f"File size is larger than allowed ({limit_mb} mb)."))


# Create your models here.

class User(AbstractUser):
    pass
