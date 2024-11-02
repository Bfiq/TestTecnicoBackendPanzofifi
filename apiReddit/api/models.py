from django.db import models

# Create your models here.
class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    username = models.TextField() #Tabla de usuarios necesaria?
    comment = models.TextField()
    parent_comment = models.ForeignKey('self', null= True, blank=True, related_name='response', on_delete=models.CASCADE)
    level = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)