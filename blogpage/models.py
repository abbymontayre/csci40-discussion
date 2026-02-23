from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import *

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    year_level = models.IntegerField()
    course = models.CharField(max_length=63)

class TaskGroup(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
        #Assignment due on 2026-02-10

    def get_absolute_url(self):
        return reverse('task_detail', args=[str(self.name)])
    
    class Meta:
        ordering = ['name']
        verbose_name = 'task group'
        verbose_name_plural = 'task groups'

class Task(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateTimeField(null=False)
    taskgroup = models.ForeignKey(
        TaskGroup, 
        on_delete=models.CASCADE, 
        related_name='students'
    ) #if taskgroup gets deleted, the task mismo gets deleted too
    def __str__(self):
        return '{}: due on {} unit(s)'.format(self.name, self.due_date)
        #Assignment due on 2026-02-10

    def get_absolute_url(self):
        return reverse('blogpage:task_detail', args=[self.pk]) #reverse looks for name in path in urlpaths, then returns 1st argument.

    @property
    def is_due(self):
        return datetime.now() >= self.due_date
    
    class Meta:
        ordering = ['due_date'] #if we want it to be descending order add '-'
        unique_together = ['due_date', 'name'] #ensures no 2 tasks cant have the same name & due date
        verbose_name = 'task' #how would the model be displayed on all interfaces?
        verbose_name_plural = 'tasks' #how would the display name be plural?
# implicit Numerical ID system, Django Integer Unique 