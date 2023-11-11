from django.db import models

# Create your models here.
class Games(models.Model):
    name = models.CharField(max_length = 200)
    developer = models.CharField(max_length = 300)
    publisher = models.CharField(max_length = 300)
    description = models.CharField(max_length = 2000)
    releaseyear = models.SmallIntegerField()
    # cover = ImageField(upload_to="covers/", height_field=None, width_field=None, max_length=100)
    # genres = models.ManyToManyField("Genres")
    # platforms = models.ManyToManyField("Platforms")
    # series = models.ManyToManyField("Series")

class Genres(models.Model):
    name = models.CharField(max_length = 200)
    games = models.ManyToManyField(Games)

class Names(models.Model):
    name = models.CharField(max_length = 200)
    game = models.ForeignKey(Games, on_delete=models.CASCADE)

class Platforms(models.Model):
    name = models.CharField(max_length = 200)
    games = models.ManyToManyField(Games)

class Series(models.Model):
    name = models.CharField(max_length = 200)
    games = models.ManyToManyField(
        Games,
        through="GameSeries",
        through_fields=("series", "game"),
    )

class GameSeries(models.Model):
    game = models.ForeignKey(Games,on_delete=models.CASCADE)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    number = models.IntegerField()
