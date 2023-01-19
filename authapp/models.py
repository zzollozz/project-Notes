from django.db import models

from django.db import models

from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=254, null=False, verbose_name="электронная почта")

