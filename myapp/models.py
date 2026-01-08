from django.db import models
from django.contrib.auth.models import User



class Lugat(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    word=models.CharField(max_length=50)
    definition=models.TextField(blank=True,null=True)
    meaning=models.CharField(max_length=100)

    class Meta:
        app_label='myapp'
        db_table="Lugat"
        ordering=["word"]

    def __str__(self):
        return self.word
    
