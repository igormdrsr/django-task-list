from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200) #Charfield for short text
    description = models.TextField() #TextField for long text
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100, blank=True, null=True) #New field for category

    def __str__(self):
        #This method is used to return a string representation of the object. In this case, it returns the title of the task. 
        #It defines how the object will be displayed in the Django admin interface and other places where the object is represented as a string.
        return self.title
    
# Criar model para unificar as demandas em uma lista
# Criar model para categorias