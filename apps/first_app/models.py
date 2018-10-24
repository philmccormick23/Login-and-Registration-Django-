from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name cannot be blank"
        elif not postData['first_name'].isalpha():
            errors['first_alpha'] = "First name cannot contain numbers"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name cannot be blank"
        elif not postData['last_name'].isalpha():
            errors['last_alpha'] = "Last name cannot contain numbers"
        if len(postData['email']) < 1:
            errors['emails'] = "Emails cannot be blank"
        elif not EMAIL_REGEX.match(postData['email']):
            errors['regex'] = "Not a valid email format"
        if len(postData['password']) < 8:
            errors['password'] = "Password cannot be blank"
        if postData['password'] != postData['confirm']:
            errors['confirm'] = "Password does not match confirmation"    
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()