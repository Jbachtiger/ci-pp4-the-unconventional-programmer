from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
from cloudinary.models import CloudinaryField

# Post model to display post details when a post is created

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    title_tag = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    hero_image = CloudinaryField('image', default='placeholder')
    publish_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    body = models.TextField()
    topic = models.CharField(max_length=255)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
# Redirects to post-detail page on post creation
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"slug": self.slug})

# A method to save url slug in database
    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    
    def number_of_likes(self):
        return self.likes.count()


