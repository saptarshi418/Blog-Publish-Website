from django import forms 
from textwriter.models import Textwriter

class BlogForm(forms.ModelForm):
   class Meta:
        model = Textwriter  # Specify the model here
        fields = ['Book_category','title', 'author', 'coverImage','body']  # Add the necessary fields
