from django.db import models

# Create your models here.
class Games(models.Model):
    name = models.CharField(max_length = 200)
    developer = models.CharField(max_length = 300)
    publisher = models.CharField(max_length = 300)
    description = models.CharField(max_length = 2000)
    releaseyear = models.SmallIntegerField()
    cover = models.ImageField(upload_to="myapp/static/covers/", blank=True)
    genres = models.ManyToManyField("Genres")
    # platforms = models.ManyToManyField("Platforms")
    # series = models.ManyToManyField("Series")
    def __str__(self):
        return self.name

class Genres(models.Model):
    name = models.CharField(max_length = 200)
    #games = models.ManyToManyField(Games)
    def __str__(self):
        return self.name

class Names(models.Model):
    name = models.CharField(max_length = 200)
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Platforms(models.Model):
    name = models.CharField(max_length = 200)
    games = models.ManyToManyField(Games)
    def __str__(self):
        return self.name

class Series(models.Model):
    name = models.CharField(max_length = 200)
    games = models.ManyToManyField(
        Games,
        through="GameSeries",
        through_fields=("series", "game"),
    )
    def __str__(self):
        return self.name

class GameSeries(models.Model):
    game = models.ForeignKey(Games,on_delete=models.CASCADE)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    number = models.IntegerField()
