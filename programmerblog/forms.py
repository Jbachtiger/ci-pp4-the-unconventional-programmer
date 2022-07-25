''' Forms for Posts, Edit and Comments '''
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post, Comment


class PostForm(forms.ModelForm):
    ''' Django form that is used to create posts '''
    class Meta:
        '''Get post model and choose which fields to display '''
        model = Post
        fields = ('title', 'title_tag', 'summary', 'author', 'body', 'topic',)

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'}),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'value': '',
                'id': 'author_field',
                'type': 'hidden'}),
            'title_tag': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title of post for SEO purposes'}),
            'body': SummernoteWidget(attrs={
                'class': 'form-control',
                'placeholder': 'Get creative and write your content here'}),
            'topic': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Coding, Imposter Syndrome, Jobs'}),
            'summary': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Brief overview of your post'})
        }


class EditForm(forms.ModelForm):
    ''' Django form that controls what fields can be edited '''
    class Meta:
        ''' Get edit form model and choose which fields to display '''
        model = Post
        fields = ('title', 'title_tag', 'summary', 'body', 'topic', )

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'}),
            'title_tag': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title of post for SEO purposes'}),
            'body': SummernoteWidget(attrs={
                'class': 'form-control',
                'placeholder': 'Get creative and write your content here'}),
            'topic': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Coding, Imposter Syndrome, Jobs'}),
            'summary': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Brief overview of your post'})
        }


class CommentForm(forms.ModelForm):
    ''' Comment form '''
    body = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Type your comment here.',
        'rows': '4',
    }))

    class Meta:
        ''' Get comment model and choose which fields to display '''
        model = Comment
        fields = ('body', )
