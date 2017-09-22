from __future__ import unicode_literals

from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.

class userManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'Invalid name please try again'
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Invalid name please try again'
        if len(postData['email']) < 2:
            errors['email'] = 'Invalid email please try again'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid email please try again'

        return errors

class users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = userManager()