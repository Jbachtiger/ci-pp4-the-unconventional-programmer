''' Imports '''
from django.test import TestCase


class TestViews(TestCase):
    '''Class to perform various automated tests on the views'''

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_create_post_page(self):
        response = self.client.get("/create-post/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "create_post.html")

