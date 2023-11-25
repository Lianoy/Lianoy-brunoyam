from django.contrib import admin
from gdb.models import game,genre,creator,platform,role,series,alt_name,gameseries,gamecreators,screenshot

# Register your models here.
admin.site.register(game)
admin.site.register(alt_name)
admin.site.register(screenshot)
admin.site.register(series)
admin.site.register(gameseries)
admin.site.register(creator)
admin.site.register(gamecreators)
admin.site.register(genre)
admin.site.register(platform)
admin.site.register(role)