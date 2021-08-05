import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from fertilizers.constants.enum import ProfessionChoices


class User(AbstractUser):

    profession_choices = [
        (profession_choice.value, profession_choice.value)
        for profession_choice in ProfessionChoices
    ]

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=100, unique=True)
    profile_pic_url = models.TextField(default="https://res.cloudinary.com/daus5ne3i/image/upload/v1622777649/download_zrhznu.jpg")
    profession = models.CharField(
        max_length=50, choices=profession_choices, default=ProfessionChoices.FARMER.value
    )


class FarmerRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_request")
    plant_part = models.CharField(max_length=200)
    pest_image_url = models.TextField()
    crop_in_acres = models.IntegerField(default=0)
