from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest


class BasicTests(TestCase):

    #user can visit index
    
    def test_index_exists(self):
        response = self.client.get('/fantasticApp')
        expected_text = 'Fantastic.'
        self.assertRedirects(response, '/fantasticApp/', status_code=301)
        