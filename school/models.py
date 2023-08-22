from django.db import models

# Create your models here.
class SchoolModel(models.Model):
    number = models.PositiveSmallIntegerField(default=1)
    address = models.TextField(max_length=200,default='')
    info = models.JSONField()

    def __str__(self):
        return f"{self.number}"

    class Meta:
        db_table = 'school'

class ClassModel(models.Model):
    name = models.CharField(max_length=4,default='')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'class'
