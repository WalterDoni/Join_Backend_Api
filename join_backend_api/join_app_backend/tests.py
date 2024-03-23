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
        user = User.objects.create_user('test_user', password='test_user')
        self.client.login(username='test_user', password='test_user')

        # Create subtask
        subtask = SubtaskModel.objects.create(titleFromSub="Test Subtask")

        # Create contact
        contact = ContactModel.objects.create(
            name="Test Contact",
            email="test@example.com",
            phonenumber="0123456",
            short="TC",
            iconColor="#FFFFFF",
            author=user
        )

        # Create task
        task = TaskModel.objects.create(
            category="Media",
            categoryColor="FFC701",
            title="Test",
            description="Test 12345",
            priority="urgent",
            section="taskCategoryInProgress",
            date="2024-04-07",
            author=user
        )

        # Add the subtask to the task
        task.subtask.add(subtask)

        # Add the contact to the task
        task.assignedTo.add(contact)

    
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
        
        # Create subtask
        subtask = SubtaskModel.objects.create(titleFromSub="Test Subtask")
        
        # Create contact
        contact = ContactModel.objects.create(
            name="Test Contact",
            email="test@example.com",
            phonenumber="0123456",
            short="TC",
            iconColor="#FFFFFF",
            author=user
        )
        
        # Create task
        task = TaskModel.objects.create(
            category="Media",
            categoryColor="FFC701",
            title="Test",
            description="Test 12345",
            priority="urgent",
            section="taskCategoryInProgress",
            date="2024-04-07",
            author=user
        )
        
        # Add the subtask to the task
        task.subtask.add(subtask)
        
        # Add the contact to the task
        task.assignedTo.add(contact)
        
    def test_create_task(self):
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)
    
    def test_get_task(self):
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)
