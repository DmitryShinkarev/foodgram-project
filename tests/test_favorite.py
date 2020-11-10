import re

import pytest
from django.test import Client, TestCase

from recipes.models import Recipe
from users.models import User


class TestFavorite(TestCase):
    '''Проверка добавления рецепта в избранное.'''

    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(
            username='user1', email='user1@user1.com', password='1234567'
        )
        self.user2 = User.objects.create_user(
            username='user2', email='user2@user2.com', password='123456'
        )
        self.recipe1 = Recipe.objects.create(
            author=self.user1, duration=10, title='title1', text='text1'
            )
        self.recipe2 = Recipe.objects.create(
            author=self.user2, duration=10, title='title2', text='text2'
            )

    def test_follow_favorite(self):
        response = self.client.post("/api/favorites/", {"id": 1})
        assert response.status_code == 403, \
        self.client.login(username='user1', password='1234567')
        response = self.client.post("/api/favorites/", {"id": 2})
        assert response.status_code == 200, \
            'Залогиненный пользователь может добавить не свой рецепт в избранное'
        assert response.data == {'success': True}, \
            'В ответе должен быть True при успешном добавлении'
        response = self.client.post("/api/favorites/", {"id": 2})
        assert response.status_code == 200, \
            'ЗАлогиненный пользователь может добавить не свой рецепт в избранное'
        assert response.data == {'success': False}, \
            'Пользователь не может добавить рецепт в избранное второй раз'
        response = self.client.post("/api/favorites/", {"id": 1})
        assert response.data == {'success': False}, \
            'Пользователь не может добавить в избранное свой рецепт'

    def test_unfollow_favorite(self):
        self.client.login(username='user1', password='1234567')
        self.client.post('/api/favorites/', {'id': 2})
        assert self.user1.favorites.count() == 1, \
        self.client.delete('/api/favorites/2/')
        assert self.user1.favorites.count() == 0, \

