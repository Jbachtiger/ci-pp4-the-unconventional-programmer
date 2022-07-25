''' Imports'''
from django.test import TestCase
from .forms import PostForm, EditForm, CommentForm


class TestForms(TestCase):
    '''
    Class to perform various automated tests on the
    PostForm, EditForm and CommentForm
    '''

    def test_fields_post(self):
        form = PostForm()
        self.assertEqual(form.Meta.fields, (
            'title',
            'title_tag',
            'summary',
            'author',
            'body',
            'topic'))

    def test_title_post(self):
        form = PostForm({'title': 'The Unconventional Programmer'})
        self.assertTrue(form.is_valid)

    def test_fields_edit(self):
        form = EditForm()
        self.assertEqual(form.Meta.fields, (
            'title',
            'title_tag',
            'summary',
            'body',
            'topic'))

    def test_fields_comment(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body',))
