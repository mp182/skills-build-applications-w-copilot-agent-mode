from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models as djongo_models
from django.conf import settings
from pymongo import MongoClient

# Sample data
USERS = [
    {"username": "superman", "email": "superman@dc.com", "team": "dc"},
    {"username": "batman", "email": "batman@dc.com", "team": "dc"},
    {"username": "wonderwoman", "email": "wonderwoman@dc.com", "team": "dc"},
    {"username": "ironman", "email": "ironman@marvel.com", "team": "marvel"},
    {"username": "spiderman", "email": "spiderman@marvel.com", "team": "marvel"},
    {"username": "captainmarvel", "email": "captainmarvel@marvel.com", "team": "marvel"},
]
TEAMS = [
    {"name": "marvel"},
    {"name": "dc"},
]
ACTIVITIES = [
    {"user": "superman", "activity": "flight", "duration": 60},
    {"user": "batman", "activity": "martial arts", "duration": 45},
    {"user": "ironman", "activity": "flying suit", "duration": 50},
]
LEADERBOARD = [
    {"user": "superman", "score": 100},
    {"user": "ironman", "score": 90},
    {"user": "batman", "score": 80},
]
WORKOUTS = [
    {"name": "strength", "suggested_for": ["superman", "batman"]},
    {"name": "agility", "suggested_for": ["spiderman", "wonderwoman"]},
]

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop collections if they exist
        for col in ['users', 'teams', 'activities', 'leaderboard', 'workouts']:
            db[col].drop()

        # Insert test data
        db['users'].insert_many(USERS)
        db['teams'].insert_many(TEAMS)
        db['activities'].insert_many(ACTIVITIES)
        db['leaderboard'].insert_many(LEADERBOARD)
        db['workouts'].insert_many(WORKOUTS)

        # Create unique index on email for users
        db['users'].create_index([('email', 1)], unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
