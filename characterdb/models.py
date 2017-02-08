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
    pc_char_name = models.CharField(primary_key=True,max_length=200)
    player_name = models.CharField(max_length=200)
    pc_char_race = models.CharField(max_length=200)
    pc_char_class = models.CharField(max_length=200)
    pc_base_st = models.IntegerField()
    pc_base_dx = models.IntegerField()
    pc_base_iq = models.IntegerField()
    pc_base_fst = models.IntegerField()
    pc_base_miq = models.IntegerField()
    pc_age = models.IntegerField()
    pc_sex = models.CharField(max_length=1)
    pc_exp = models.IntegerField(default=0)
    pc_background = models.TextField()
    pc_description = models.TextField()
    #pc_skill_list = TODO figure out how to make a list of objects elsewhere and link them here with relationship
    #pc_item_list
    #pc_armor_list
    #pc_weapon_list
    #pc_active_weapon
    #pc_active_armor
    #pc_active_shield
    #pc_spell_list
    #pc_studies_list
    #pc_advantages_list
    #pc_disadvantages_list



class GMCharacter(models.Model):
    gm_character_name = models.CharField(primary_key=True,max_length=200)