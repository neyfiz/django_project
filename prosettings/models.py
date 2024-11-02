from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='teams/', blank=True, null=True)

    def __str__(self):
        return self.name or 'Unknown Organization'

class Game(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    logo = models.ImageField(upload_to='games/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name or 'Unknown Game'

    @property
    def player_count(self):
        return self.players.count()

    @property
    def team_count(self):
        return self.team_games.count()


class Team(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    organization = models.ForeignKey(Organization, related_name='teams', on_delete=models.CASCADE, blank=True, null=True)
    game = models.ForeignKey(Game, related_name='team_games', on_delete=models.SET_NULL, blank=True, null=True)
    logo = models.ImageField(upload_to='teams/', blank=True, null=True)

    def __str__(self):
        return self.name or 'Unknown Team'

class Player(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    team = models.ForeignKey(Team, related_name='players', on_delete=models.SET_NULL, blank=True, null=True)
    game = models.ManyToManyField(Game, related_name='players', blank=True)

    def __str__(self):
        return self.nickname or 'Unknown Player'
