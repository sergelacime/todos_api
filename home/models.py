from django.db import models
from django.contrib.auth.models import User


class task(models.Model):
    items = (
        ('w','white'),
        ('b','blue'),
        ('r','red'),
        ('g','green'),
        ('y','yellow'),
    )
    title = models.CharField(max_length=300)
    content = models.TextField(max_length=2500)
    date_created = models.DateTimeField()
    date_finished = models.DateTimeField()
    state = models.BooleanField(default=True)
    flag = models.CharField(choices=items, max_length=20)
    owner = models.ForeignKey("taskList", on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.owner != None:
            super().save(*args, **kwargs)
            self.owner.tasks.add(self)
            self.owner.save()
        else:
            pass
        


class taskList(models.Model):
    date = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tasks = models.ManyToManyField(task, blank=True)
    
    def __str__(self):
        return self.user.username


class podcastCategory(models.Model):
    date = models.DateTimeField(auto_now=True)
    libelle = models.CharField(max_length=100)
    
    def __str__(self):
        return self.libelle
    

class podcast(models.Model):
    date = models.DateTimeField(auto_now=True)
    libelle = models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    category = models.ForeignKey(podcastCategory, on_delete=models.CASCADE)


class userPodcastPool(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category_pool = models.ManyToManyField(podcastCategory)
