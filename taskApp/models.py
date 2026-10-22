from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


#custom user model
class CustomUser(AbstractUser):
    profile_picture=models.ImageField(upload_to='profile_pics', blank=True,null=True)
    bio=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.username



# Task Model (CRUD Operations-এর জন্য)
class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in-progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title