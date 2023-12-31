from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255)
    def  __str__(self):
        return self.name
    
    def get_absolute_url(self):
        # return reverse('PostView', args=(str(self.id)))
        return reverse('Home')

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, default='blogonit')
    snippet = models.CharField(max_length=255)
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="blog_post")
    
    def  __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        # return reverse('PostView', args=(str(self.id)))
        return reverse('Home')
    
    def total_likes(self):
        return self.likes.count()
    
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profilePic/")
    website = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    github = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)
    
    def  __str__(self):
        return str(self.user)
    
