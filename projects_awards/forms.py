from .models import Projects, Profile, Comments
from django import forms

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ['profile','date', 'poster_id']


class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'userId']


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['project_id', 'user']