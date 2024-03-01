from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import *

class LoginTest(TestCase):
    def test_login(self):
        self.client = Client()
        self.user = User.objects.create_user('test_user', password='test_user')
        self.client.login(username='test_user', password='test_user')
        self.assertTrue('_auth_user_id' in self.client.session)  # Überprüfen ob der Benutzer erfolgreich eingeloggt ist
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)
        
        
class ContactTest(TestCase):
    def setUp(self):
        self.client = Client()
        user = User.objects.create_user('test_user', password='test_password')
        self.contact = ContactModel.objects.create(
        name="Test Case",
        email="Tesct@Case.at",
        phonenumber="0123456",
        short="TC",
        iconColor= "#FFFFFF",
        author= user
        )
    
    def test_create_contact(self):
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)
  
    def test_get_contact(self):  
        response = self.client.get('/contacts/')
        self.assertEqual(response.status_code, 200) 
        
        
class TaskTest(TestCase):
    def setUp(self):
        self.client = Client()
        user = User.objects.create_user('test_user', password='test_user')
        self.client.login(username='test_user', password='test_user')
        task = TaskModel.objects.create(
         title="Test",
         description="Empty description",
         priority= "to-do",
         category="Max Mustermann",
         subtask="nothing",
         author= user
        )
        contact = ContactModel.objects.create(
         name="Test Contact",
         email="test@example.com",
         phonenumber="0123456",
         short="TC",
         iconColor="#FFFFFF",
         author=user
        )
        task.assigned_to.add(contact)
        
    def test_create_task(self):
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)
    
    def test_get_task(self):
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)