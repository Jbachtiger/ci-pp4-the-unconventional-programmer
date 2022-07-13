from django import forms
from .models import Post, Comment

# Django form that is used to create posts
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'title_tag', 'body', 'topic')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'author_field', 'type': 'hidden'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of post for SEO purposes'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Get creative and write your content here'}),
            'topic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Coding, Imposter Syndrome, Jobs'})
        }

# Django form that controls what fields can be edited
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'topic')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of post for SEO purposes'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Get creative and write your content here'}),
            'topic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Coding, Imposter Syndrome, Jobs'})
        }


# Comment form
class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Type your comment here.',
        'rows': '4',
    }))
    class Meta:
        model = Comment
        fields = ('body', )
