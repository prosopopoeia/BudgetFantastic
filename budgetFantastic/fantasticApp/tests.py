from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from fantasticApp.models import Category, User, Overall, Entry


class BasicTests(TestCase):

    #user can visit index
    
    def test_index_exists(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'fantasticApp/index.html')
        #self.assertRedirects(response, '/fantasticApp/', status_code=301)
    
    def test_can_save_category(self):
        self.client.post('/fantasticApp/setup/', data={'item_text': 'cat1'})        
        self.assertEqual(Category.objects.count(), 1)
        current_cat = Category.objects.first()
        self.assertEqual(current_cat.category_name, 'cat1')
       
    def test_can_get_and_save_username(self):
        response =  self.client.post('/fantasticApp/getname/', data={'item_text': 'kimbal'})
        this_users_name = User.objects.first()
        self.assertEqual(this_users_name.user_name, 'kimbal')
        
        
    def test_can_create_category(self):   
         self.clent.post('/fantasticApp/newcat