
from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        db_table = 'teams'
    def __str__(self):
        return self.name

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team_name = models.CharField(max_length=100)  # Referencja przez nazwę zespołu
    class Meta:
        db_table = 'users'
    def __str__(self):
        return self.email

class Activity(models.Model):
    user_email = models.EmailField()  # Referencja przez email użytkownika
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateField()
    class Meta:
        db_table = 'activities'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.CharField(max_length=100)  # Nazwa zespołu
    class Meta:
        db_table = 'workouts'

class Leaderboard(models.Model):
    team_name = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        db_table = 'leaderboard'
