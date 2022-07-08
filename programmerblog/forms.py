from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'title_tag', 'body', 'topic')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of post for SEO purposes'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Get creative and write your content here'}),
            'topic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Coding, Imposter Syndrome, Jobs'})
        }