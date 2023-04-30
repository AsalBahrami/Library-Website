from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Setup2Form(ModelForm):
    class Meta:
        model = Setup2
        fields = '__all__'

class CreateFormForUser(UserCreationForm):
    class Meta:
        model= User
        fields=['username','email',"password1","password2"]


class ManipulationForm(ModelForm):
    class Meta:
        model= Setup2
        fields='__all__'

class AdvanceF2(ModelForm):
    class Meta:
        model= Setup2
        fields=['author']


class BorrowingForm(ModelForm):
    class Meta:
        model= Setup2
        fields=['entleiher','entleiher_bem']

