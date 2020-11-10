from django.test import Client, TestCase

from users.models import User


class TestSubscribe(TestCase):
    '''Проверка правильности работы системы подписок.'''

    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(
            username='user1', email='user1@user1.com', password='1234567'
        )
        self.user2 = User.objects.create_user(
            username='user2', email='user2@user2.com', password='123456'
        )

    def test_follow_author(self):
        response = self.client.post('/api/subscriptions/', {'id': 2})
        assert response.status_code == 403, \
            'Незалогиненный пользователь не может подписаться на авторов'
        self.client.login(username='user1', password='1234567')
        response = self.client.post('/api/subscriptions/', {'id': 2})
        assert response.status_code == 200, \
            'Залогиненный пользователь может подписаться на авторов'
        assert response.data == {'success': True}, \
            'В ответе должен быть True при успешной подписке'
        response = self.client.post('/api/subscriptions/', {'id': 2})
        assert response.status_code == 200, \
            'Залогиненный пользователь может подписаться на авторов'
        assert response.data == {'success': False}, \
            'Пользователь не может подписаться второй раз на себя'
        response = self.client.post('/api/subscriptions/', {'id': 1})
        assert response.data == {'success': False}, \
            'Пользователь не может подписаться на себя'

    def test_unfollow_author(self):
        self.client.login(username='user1', password='1234567')
        self.client.post('/api/subscriptions/', {'id': 2})
        assert self.user1.follower.count() == 1, \
        self.client.delete('/api/subscriptions/2/')
        assert self.user1.follower.count() == 0, \
