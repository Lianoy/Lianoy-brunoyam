from django.db import models

# Create your models here.

class genre(models.Model):
    name = models.CharField(max_length=200, verbose_name = "жанр")
    def __str__(self):
        return self.name

class alt_name(models.Model):
    name = models.CharField(max_length=200, verbose_name = "название")
    game = models.ForeignKey("game", on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class series(models.Model):
    name = models.CharField(max_length = 200)
    def __str__(self):
        return self.name

class gameseries(models.Model):
    game = models.ForeignKey("game",on_delete=models.CASCADE)
    series = models.ForeignKey(series, on_delete=models.CASCADE)
    number = models.IntegerField()
    
class platform(models.Model):
    name = models.CharField(max_length=200, verbose_name = "название")
    def __str__(self):
        return self.name
    
class creator(models.Model):
    name = models.CharField(max_length=200, verbose_name = "имя")
    description = models.CharField(max_length=2000, verbose_name = "краткая биография",blank = True)
    def __str__(self):
        return self.name
    
class role(models.Model):
    name = models.CharField(max_length=200, verbose_name = "должность")
    def __str__(self):
        return self.name

class gamecreators(models.Model):
    game = models.ForeignKey("game",on_delete=models.CASCADE)
    creator = models.ForeignKey(creator, on_delete=models.CASCADE)
    role = models.ForeignKey(role, on_delete=models.CASCADE)

class screenshot(models.Model):
    image = models.ImageField(upload_to="gdb/static/screens/", blank=True)
    game = models.ForeignKey("game", on_delete=models.CASCADE)

class game(models.Model):
    name = models.CharField(max_length=200, verbose_name = "название")
    releaseyear = models.SmallIntegerField()
    developer = models.CharField(max_length = 300)
    publisher = models.CharField(max_length = 300)
    cover = models.ImageField(upload_to="gdb/static/covers/", blank=True)
    description = models.CharField(max_length=2000, verbose_name = "описание")
    genre = models.ManyToManyField(genre)
    series = models.ManyToManyField(
        series,
        through=gameseries,
        through_fields=("game","series"),
    )
    creators = models.ManyToManyField(
        creator,
        through=gamecreators,
        through_fields=("game","creator"),
    )
    platform = models.ManyToManyField(platform)
    def __str__(self):
        return self.name