''' Imports '''
from django.test import TestCase
from .forms import UpdateProfileForm, UpdateUserForm


class TestProfileForms(TestCase):
    '''
    Class to perform various automated tests on the
    UpdateProfileForm and UpdateUserForm
    '''

    def test_fields_profile(self):
        form = UpdateProfileForm()
        self.assertEqual(form.Meta.fields, ['bio', 'profile_image'])

    def test_fields_user(self):
        form = UpdateUserForm()
        self.assertEqual(form.Meta.fields, ['username', 'email'])
