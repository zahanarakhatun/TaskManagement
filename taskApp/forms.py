from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Task

#  (Custom User Model)
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'profile_picture', 'bio']


# (Task Create and Update)
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'status']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }