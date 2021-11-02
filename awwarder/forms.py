from .models import Profile,Project
from django import forms
from django.forms import ModelForm
class NewpostForm(forms.ModelForm):
    class Meta:
        model =Project
        exclude = [' project_title']
class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user'] 
class VoteForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('design','usability','content')