from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(username='testuser', email='test@example.com', team='marvel')
        self.assertEqual(user.username, 'testuser')
    def test_team_creation(self):
        team = Team.objects.create(name='avengers')
        self.assertEqual(team.name, 'avengers')
    def test_activity_creation(self):
        activity = Activity.objects.create(user='testuser', activity='run', duration=30)
        self.assertEqual(activity.activity, 'run')
    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(user='testuser', score=99)
        self.assertEqual(lb.score, 99)
    def test_workout_creation(self):
        workout = Workout.objects.create(name='cardio', suggested_for=['testuser'])
        self.assertIn('testuser', workout.suggested_for)
