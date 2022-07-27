''' Imports '''
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment


class TestModels(TestCase):
    ''' Class to test models'''

    def setUp(self):
        self.test_user = User.objects.create(
            password='test123', username='testuser'
        )

    def test_post_model_str(self):
        post = Post.objects.create(title="title", author=self.test_user)
        self.assertEqual((str(post.title)), 'title')
        self.assertEqual((str(post.author)), 'testuser')

    def test_comment_model_str(self):
        post = Post.objects.create(title="title", author=self.test_user)
        comment = Comment.objects.create(
            post=post,
            user=self.test_user,
            body='testuser'
            )
        self.assertEqual(str(comment), 'testuser')
