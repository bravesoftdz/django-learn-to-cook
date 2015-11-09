from django.contrib import admin

from recipes.models import Person
from recipes.models import Skill

# Register your models here.

admin.site.register(Person)
admin.site.register(Skill)
