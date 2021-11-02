from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.
class Profile(models.Model):
    profile_image = models.ImageField(upload_to = 'pictures/')
    bio= models.CharField(max_length=30)
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    def save_profile(self):
        self.save()
    @classmethod
    def search_by_name(cls,search_term):
        project = cls.objects.filter(name__icontains=search_term)
        return project
class Project(models.Model):
    image_path = models.ImageField(upload_to = 'pictures/')
    title= models.CharField(max_length=30)  
    description = models.CharField(max_length=200)
    link = models.URLField(max_length=128, db_index=True, unique=True, null=True)
    design = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    usability = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    content = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    vote_submissions = models.IntegerField(default=0)
    def __str__(self):
        return self.title

    def save_project(self):
        self.save() 

    def delete_project(self):
        self.delete()          
    
    @classmethod
    def search_by_title(cls,title):
        title = cls.objects.filter(title__icontains=title)
        return  title