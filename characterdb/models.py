from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Skill(models.Model):
    def __unicode__(self):
       return self.skill_name
    skill_name = models.CharField(primary_key=True,max_length=200)
    skill_iq_min = models.IntegerField(default=10)
    skill_memory = models.IntegerField(default=1)
    skill_description = models.TextField()
    non_class_multiplier = models.IntegerField(default=2)


class Spell(models.Model):
    def __unicode__(self):
       return self.spell_name
    spell_name = models.CharField(primary_key=True,max_length=200)
    spell_iq_min = models.IntegerField(default=10)
    spell_memory = models.IntegerField(default=1)
    non_class_multiplier = models.IntegerField(default=3)
    spell_description = models.TextField()


class Item(models.Model):
    def __unicode__(self):
       return self.item_name
    item_name = models.CharField(primary_key=True,max_length=200)
    item_price = models.FloatField()
    item_encumbrance = models.FloatField()
    item_description = models.TextField()
    item_enchantment = models.TextField()
    item_dx_mod = models.IntegerField(default=0)
    item_st_mod = models.IntegerField(default=0)
    item_iq_mod = models.IntegerField(default=0)
    item_roll_mod = models.IntegerField(default=0)


class Weapon(models.Model):
    def __unicode__(self):
       return self.weapon_name
    weapon_name = models.CharField(primary_key=True,max_length=200)
    weapon_dx_mod = models.IntegerField(default=0)
    weapon_st_mod = models.IntegerField(default=0)
    weapon_iq_mod = models.IntegerField(default=0)
    weapon_roll_mod = models.IntegerField(default=0)
    weapon_damage_dice = models.IntegerField()
    weapon_damage_mod = models.IntegerField()
    weapon_enchantment = models.TextField()
    weapon_price = models.FloatField()
    weapon_description = models.TextField()


class Armor(models.Model):
    def __unicode__(self):
       return self.armor_name
    armor_name = models.CharField(primary_key=True,max_length=200)
    armor_description = models.TextField()
    armor_damage_reduction = models.IntegerField()
    armor_dx_mod = models.IntegerField()
    armor_st_mod = models.IntegerField(default=0)
    armor_iq_mod = models.IntegerField(default=0)
    armor_roll_mod = models.IntegerField(default=0)
    armor_enchantment = models.TextField()
    armor_price = models.FloatField()


class PlayedCharacter(models.Model):
    def __unicode__(self):
       return "{0} played by: {1}".format(self.char_name, self.player_name)
    char_name = models.CharField(primary_key=True,max_length=200)
    player_name = models.CharField(max_length=200)
    char_race = models.CharField(max_length=200)
    char_class = models.CharField(max_length=200)
    char_base_st = models.IntegerField()
    char_current_health = models.IntegerField()
    char_base_dx = models.IntegerField()
    char_adj_dx = models.IntegerField()
    char_base_iq = models.IntegerField()
    char_base_fst = models.IntegerField()
    char_current_fst = models.IntegerField()
    char_base_miq = models.IntegerField()
    char_age = models.IntegerField()
    char_sex = models.CharField(max_length=1)
    char_exp = models.IntegerField(default=0)
    char_background = models.TextField()
    char_description = models.TextField()
    char_advantage = models.TextField()
    char_disadvantage = models.TextField()


class char_skill_list(models.Model):
    def __unicode__(self):
       return "{0} Skill: {1}".format(self.char_name, self.skill_name)
    char_name = models.CharField(max_length=200)
    skill_name = models.CharField(max_length=200)
    study = models.BooleanField(default=False)


class char_spell_list(models.Model):
    def __unicode__(self):
       return "{0} Spell: {1}".format(self.char_name, self.spell_name)
    char_name = models.CharField(max_length=200)
    spell_name = models.CharField(max_length=200)
    study = models.BooleanField(default=False)


class char_item_list(models.Model):
    def __unicode__(self):
       return "{0} Item: {1}".format(self.char_name, self.item_name)
    char_name = models.CharField(max_length=200)
    item_name = models.CharField(max_length=200)
    count = models.IntegerField(default=1)


class char_weapon_list(models.Model):
    def __unicode__(self):
       return "{0} Weapon: {1}".format(self.char_name, self.weapon_name)
    char_name = models.CharField(max_length=200)
    weapon_name = models.CharField(max_length=200)
    count = models.IntegerField(default=1)
    is_equipped = models.BooleanField(default=False)


class char_armor_list(models.Model):
    def __unicode__(self):
       return "{0} Armor: {1}".format(self.char_name, self.armor_name)
    char_name = models.CharField(max_length=200)
    armor_name = models.CharField(max_length=200)
    count = models.IntegerField(default=1)
    is_equipped = models.BooleanField(default=False)
