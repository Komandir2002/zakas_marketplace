from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    GENDER_TYPE = (("Male", "Male"), ("Female", "Female"), ("Other", "Other"))
    gender = models.CharField(choices=GENDER_TYPE, max_length=100)
    phone_number = models.CharField(max_length=100)
    birth_day = models.DateField(null=True)