from django.db import models
from super_types.models import Super_Types
# Create your models here.
class Supers(models.Model):
    name = models.CharField(max_length = 200)
    alter_ego = models.CharField(max_length = 200)
    primary_ability = models.CharField(max_length = 200)
    secondary_ability = models.CharField(max_length = 200)
    catchphrase = models.CharField(max_length = 200)
    type = models.ForeignKey(Super_Types, on_delete=models.CASCADE)

