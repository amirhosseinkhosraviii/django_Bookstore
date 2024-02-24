from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):  # username => firstname , lastname , email , password , +...+  age
    # nat_id  => id
    # gender => male female
    age = models.PositiveIntegerField(null=True, blank=True)



