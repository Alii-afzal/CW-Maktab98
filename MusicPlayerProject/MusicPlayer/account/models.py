from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ACCOUNT_CHOICES = ( 
        ('N', 'Normal'),
        ('V', 'VIP'),
    )

    account_type = models.CharField(max_length=10, choices=ACCOUNT_CHOICES)
    user_info = models.TextField()
    image = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.username
    