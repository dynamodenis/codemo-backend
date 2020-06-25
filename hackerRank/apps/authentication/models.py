import jwt
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, username, email, password):
        if username is None:
            raise TypeError('Users must have a name.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

    def create_student(self, username, email, password=None):
        if email is None:
            raise TypeError('Users must have an email address.')
        student = self.create_user(username, email, password)
        student.set_password(password)
        student.is_student = True
        student.save()
        return student

    def create_mentor(self, username, email, password=None):
        if email is None:
            raise TypeError('Users must have an email address.')
        mentor = self.create_user(username, email, password)
        mentor.set_password(password)
        mentor.is_mentor = True
        mentor.save()
        return mentor


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_mentor = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email
  
    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def _generate_jwt_token(self):
 
        token = jwt.encode({
            'id': self.pk, 
            'email':self.email, 
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')
