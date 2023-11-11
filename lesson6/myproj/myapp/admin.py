from django.contrib import admin
from myapp.models import Games, Genres, Platforms, Series, Names

# Register your models here.
admin.site.register(Games)
admin.site.register(Genres)
admin.site.register(Platforms)
admin.site.register(Series)
admin.site.register(Names)
