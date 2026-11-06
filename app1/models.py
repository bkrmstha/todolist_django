from django.db import models

# Create your models here.
class TodoList(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField()
    is_completed = models.BooleanField(default=False)
    create_date = models.DateField(auto_now=True)
    complete_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.title