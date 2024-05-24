from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.user.username


class Category(models.Model):
     name = models.CharField(max_length=255)
     description = models.TextField()

     def __str__(self):
          return self.name

class Tag(models.Model):
     name = models.CharField(max_length=255)
     slug = models.SlugField( blank=True)

     def __str__(self):
          return self.name
     
     def save(self, *args, **kwargs):
          self.slug = slugify(self.name, allow_unicode=True)
          super().save(*args, **kwargs)

class Post(models.Model):
     title = models.CharField(max_length=255)
     content = models.TextField()
     author = models.ForeignKey(Author, on_delete=models.CASCADE)
     categories = models.ManyToManyField(Category)
     tags = models.ManyToManyField(Tag)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     published = models.BooleanField(default=False)

     class Meta:
             ordering = ['-created_at']

     def __str__(self):
          return self.title
     
     

class Comment(models.Model):
     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
     author = models.CharField(max_length=255)
     content = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)

     class Meta:
             ordering = ['created_at']
             
     def __str__(self):
          return f'Comment by {self.author} on {self.post}'
     

    

