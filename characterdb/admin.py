from django.contrib import admin

# Register your models here.

from .models import Skill, Spell, Item, Weapon, Armor, PlayedCharacter, char_armor_list, char_item_list, char_skill_list
from .models import char_spell_list, char_weapon_list

admin.site.register(Skill)
admin.site.register(Spell)
admin.site.register(Item)
admin.site.register(Weapon)
admin.site.register(Armor)
admin.site.register(PlayedCharacter)
admin.site.register(char_armor_list)
admin.site.register(char_item_list)
admin.site.register(char_skill_list)
admin.site.register(char_spell_list)
admin.site.register(char_weapon_list)