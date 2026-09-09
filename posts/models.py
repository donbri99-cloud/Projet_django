from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=150)
    statut = models.CharField(default='brouillon')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title   
    
   
        
# Create your models here.
