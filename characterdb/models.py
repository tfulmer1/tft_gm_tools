from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Skill(models.Model):
    skill_name = models.CharField(max_length=200)
    skill_iq_min = models.IntegerField(default=10)
    skill_memory = models.IntegerField(default=1)
    skill_description = models.CharField(max_length=5000)
