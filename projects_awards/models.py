from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to = 'images/', blank = True)
    user = models.ForeignKey(User,on_delete = models.CASCADE,null = True)
    bio = models.TextField(max_length = 100)
    userId =models.IntegerField(default = 0)
    email = models.EmailField()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()   

    def update_bio(self,bio):
        self.bio = bio
        self.save()

    @classmethod
    def find_user(cls, profile_id):
        profile = cls.objects.get(id=profile_id)
        return profile

    @classmethod
    def update_profile(cls,profile,update):
         updated = cls.objects.filter(Image_name=profile).update(name=update)
         return updated

    def __str__(self):
        return self.bio

class Projects(models.Model):
    title = models.CharField(max_length = 30)
    project_image = models.ImageField(upload_to = 'images/')
    description = models.TextField(blank= True)
    profile = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    url = models.URLField(blank=True)
    date = models.DateField(auto_now_add=True)
    poster_id = models.IntegerField(default=0)

    def save_project(self):
        self.save()

    def delete_project(self):
        Projects.objects.filter().delete()
    
    @classmethod
    def get_projects(cls):
        projects = Projects.objects.all()
        return projects

    @classmethod
    def get_project(cls, project_id):
        single_project = cls.objects.get(id=project_id)
        return single_project

    @classmethod
    def search_by_title(cls,search_term):
        project = cls.objects.filter(title__icontains=search_term)
        return project

    class Meta:
        ordering = ['-id']

class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField(max_length=150)
    project_id=models.IntegerField(default=0)

