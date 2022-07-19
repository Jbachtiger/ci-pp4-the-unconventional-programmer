''' Imports for post and comment models '''
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField

# Post model to display post details when a post is created

class Post(models.Model):
    ''' Model for Posts '''
    title = models.CharField(max_length=255, unique=True)
    title_tag = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    hero_image = CloudinaryField('image', default='placeholder')
    publish_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    body = RichTextField(blank=True, null=True)
    topic = models.CharField(max_length=255)

    class Meta:
        ''' To order created posts by descending order '''
        ordering = ['-publish_date']

    def __str__(self):
        return self.title + ' | ' + str(self.author)
     
    def get_absolute_url(self):
        ''' Redirects to post-detail page on post creation '''
        return reverse("post-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        ''' A method to save url slug in database '''  
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def number_of_likes(self):
        ''' Helper method to return total number of likes on a post '''
        return self.likes.count()


class Comment (models.Model):
    ''' Model for Comment '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.user.username