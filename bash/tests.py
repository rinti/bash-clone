import json

from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User

from .models import Quote


class QuoteTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test')
        self.quote = Quote.objects.create(user=self.user, quote='Lorem ipsum', voters=['0.0.0.0', '0.1.2.3'], score=0)
        self.c = Client()

    def test_invalid_votes(self):
        response = self.c.post('/vote/{}/'.format(self.quote.id), {'vote': 0})
        self.assertEqual(response.status_code, 403)

        response = self.c.post('/vote/{}/'.format(self.quote.id), {'vote': -2})
        self.assertEqual(response.status_code, 403)

        response = self.c.post('/vote/{}/'.format(self.quote.id), {'vote': 2})
        self.assertEqual(response.status_code, 403)

    def test_valid_votes(self):
        response = self.c.post('/vote/{}/'.format(self.quote.id), {'vote': 1})
        self.assertEqual(response.status_code, 200)

        response = self.c.post('/vote/{}/'.format(self.quote.id), {'vote': -1}, REMOTE_ADDR='0.0.1.1')
        self.assertEqual(response.status_code, 200)

    def test_user_cannot_vote_twice(self):
        response = self.c.post('/vote/{}/'.format(self.quote.id), {'vote': -1}, REMOTE_ADDR='1.1.1.1')
        self.assertEqual(response.status_code, 200)

        response = self.c.post('/vote/{}/'.format(self.quote.id), {'vote': -1}, REMOTE_ADDR='1.1.1.1')
        self.assertEqual(response.status_code, 403)

    def test_voting_affects_score(self):
        self.assertEqual(self.quote.score, 0)

        response = self.c.post('/vote/{}/'.format(self.quote.id), {'vote': -1}, REMOTE_ADDR='12.2.6.8')
        score = json.loads(response.content.decode('utf-8'))['score']
        self.assertEqual(score, -1)

        response = self.c.post('/vote/{}/'.format(self.quote.id), {'vote': 1})
        score = json.loads(response.content.decode('utf-8'))['score']
        self.assertEqual(score, 0)


class QuoteManagerTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='user1')
        user2 = User.objects.create_user(username='user2', password='user2')
        User.objects.create_user(username='user3', password='user3')

        Quote.objects.create(user=self.user, quote='Lorem ipsum')
        Quote.objects.create(user=self.user, quote='Lorem ipsum 2')
        Quote.objects.create(user=user2, quote='Lorem ipsum 3')

    def test_from_user(self):
        self.assertEqual(Quote.objects.from_user(self.user).count(), 2)
        self.assertEqual(Quote.objects.from_user('user2').count(), 1)
        self.assertEqual(Quote.objects.from_user(3).count(), 0)

    def test_from_user_chainability(self):
        self.assertEqual(Quote.objects.from_user(self.user).from_user('user2').count(), 0)
        self.assertEqual(Quote.objects.from_user('user2').filter(quote__contains='ipsum').count(), 1)
