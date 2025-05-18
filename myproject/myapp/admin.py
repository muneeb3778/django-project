from django.contrib import admin

# Register your models here.

from .models import *             # isme models me jitni bhi class he jab agai

admin.site.register(Course)       # isse database ko register kar sakte he

admin.site.register(Lesson)

admin.site.register(Department)

admin.site.register(Employee)


admin.site.register(Singer)

class SingerAdmin(admin.ModelAdmin):
    list_display=["id","name","gender"]

admin.site.register(Song)

class SongAdmin(admin.ModelAdmin):
    list_display=["id","title","singer"]



