from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Skill(models.Model):
    skill_name = models.CharField(primary_key=True,max_length=200)
    skill_iq_min = models.IntegerField(default=10)
    skill_memory = models.IntegerField(default=1)
    skill_description = models.TextField()
    non_class_multiplier = models.IntegerField(default=2)

class Spell(models.Model):
    spell_name = models.CharField(primary_key=True,max_length=200)
    spell_iq_min = models.IntegerField(default=10)
    spell_memory = models.IntegerField(default=1)
    non_class_multiplier = models.IntegerField(default=3)
    spell_description = models.TextField()

class Item(models.Model):



class Weapon(models.Model):


class