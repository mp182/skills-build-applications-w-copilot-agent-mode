from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100)
    def __str__(self):
        return self.username

class Activity(models.Model):
    user = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)
    duration = models.IntegerField()
    def __str__(self):
        return f"{self.user} - {self.activity}"

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    score = models.IntegerField()
    def __str__(self):
        return f"{self.user}: {self.score}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    suggested_for = models.JSONField(default=list)
    def __str__(self):
        return self.name
