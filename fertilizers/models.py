import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=100, unique=True)
    profile_pic_url = models.TextField(default="https://res.cloudinary.com/daus5ne3i/image/upload/v1622777649/download_zrhznu.jpg")
