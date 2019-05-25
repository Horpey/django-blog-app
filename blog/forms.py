from django import forms
from .models import Comment

# Create Form Class
class commentForm(forms.ModelForm):

    class Meta: 
        model = Comment
        fields = ('author', 'body')