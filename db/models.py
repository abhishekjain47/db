from django.db import models
from django.contrib.auth.models import user
class post(models.model):
    post = models.CharField(max_length=20)
    user = models.ForeignKey(user)
