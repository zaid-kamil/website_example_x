from django.db import models
from django.db.models.fields import CharField, TextField

# Create your models here.
# step 1
class HR(models.Model):
    name = CharField(max_length=30)
    detail = TextField()


    class Meta:
        verbose_name = 'Human resource'
        verbose_name_plural = 'Human resources'

    def __str__(self):
        return self.name
