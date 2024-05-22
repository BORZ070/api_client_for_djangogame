from django.db import models

class ApiGames(models.Model):
    game_name = models.CharField(max_length=100)
    game_publisher = models.CharField(max_length=100)
    game_image = models.URLField()
