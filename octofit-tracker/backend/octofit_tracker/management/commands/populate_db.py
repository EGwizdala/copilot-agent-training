
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write('Deleting old data...')
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        self.stdout.write('Creating teams...')
        Team.objects.create(name='Marvel')
        Team.objects.create(name='DC')

        self.stdout.write('Creating users...')
        users = [
            {'email': 'ironman@marvel.com', 'name': 'Iron Man', 'team_name': 'Marvel'},
            {'email': 'captain@marvel.com', 'name': 'Captain America', 'team_name': 'Marvel'},
            {'email': 'spiderman@marvel.com', 'name': 'Spider-Man', 'team_name': 'Marvel'},
            {'email': 'batman@dc.com', 'name': 'Batman', 'team_name': 'DC'},
            {'email': 'superman@dc.com', 'name': 'Superman', 'team_name': 'DC'},
            {'email': 'wonderwoman@dc.com', 'name': 'Wonder Woman', 'team_name': 'DC'},
        ]
        for u in users:
            User.objects.create(**u)

        self.stdout.write('Creating activities...')
        Activity.objects.create(user_email='ironman@marvel.com', type='run', duration=30, date='2024-01-01')
        Activity.objects.create(user_email='captain@marvel.com', type='cycle', duration=45, date='2024-01-02')
        Activity.objects.create(user_email='spiderman@marvel.com', type='swim', duration=25, date='2024-01-03')
        Activity.objects.create(user_email='batman@dc.com', type='run', duration=40, date='2024-01-01')
        Activity.objects.create(user_email='superman@dc.com', type='cycle', duration=50, date='2024-01-02')
        Activity.objects.create(user_email='wonderwoman@dc.com', type='swim', duration=35, date='2024-01-03')

        self.stdout.write('Creating workouts...')
        Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='Marvel')
        Workout.objects.create(name='Situps', description='Do 30 situps', suggested_for='DC')

        self.stdout.write('Creating leaderboard...')
        Leaderboard.objects.create(team_name='Marvel', points=120)
        Leaderboard.objects.create(team_name='DC', points=110)

        self.stdout.write('Ensuring unique index on email...')
        with connection.cursor() as cursor:
            cursor.execute('db.users.createIndex({"email": 1}, {"unique": true})')

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
