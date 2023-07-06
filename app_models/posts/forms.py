from django import forms
from django.forms import  Form ,ModelForm
from model_setup . models import Post,Profile,Comment

class AddPost(ModelForm):
    class Meta:
        model=Post
        fields=['user', 'caption', 'image_or_video_content']


# class Profile(ModelForm):
#     class Meta:
#         model=Profile
#         fields='__all__'

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class ProfileForms(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['gender', 'bio', 'website', 'location']