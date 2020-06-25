from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

client = Client()


class UserManagerTestClass(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='test User', email='test@gmail.com', password='test@pass')
        self.assertEqual(user.email, 'test@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            'admin', 'admin@gmail.com', 'admin@123')
        self.assertEqual(admin_user.email, 'admin@gmail.com')
        self.assertTrue(admin_user.is_staff)

    def test_create_studentuser(self):
        User = get_user_model()
        student_user = User.objects.create_student(
            'student1', 'student@gmail.com', 'student@123')
        self.assertEqual(student_user.email, 'student@gmail.com')
        self.assertTrue(student_user.is_student)

    def test_create_mentoruser(self):
        User = get_user_model()
        mentor_user = User.objects.create_mentor(
            'mentor1', 'mentor@gmail.com', 'mentor@123')
        self.assertEqual(mentor_user.email, 'mentor@gmail.com')
        self.assertTrue(mentor_user.is_mentor)



