from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOISES = (
        ('a','admin'),
        ('s','student'),
        ('t','teacher'),
        ('p','parent')
    )
    roles = models.CharField(max_length=1,choices=ROLE_CHOISES)

class PersonModel(models.Model):
    name = models.CharField(max_length=65,default='')
    fname = models.CharField(max_length=65,default='')
    date_of_birth =models.DateField(default=datetime.now)
    address = models.TextField()
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,default=None,null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        abstract = True

class ParentsModel(PersonModel):

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'parent'

class StudentModel(PersonModel):
    school = models.ForeignKey('school.SchoolModel',on_delete=models.CASCADE)
    clasS = models.ForeignKey('school.ClassModel',on_delete=models.SET_NULL,null=True)
    parents = models.ForeignKey(ParentsModel,default='',on_delete=models.SET_NULL,null=True)
    avtive = models.BooleanField(default=True)
    phone = models.CharField(max_length=13,default='')

    def __str__(self):
        return f"{self.name} {self.fname}"

    class Meta:
        db_table = 'student'


class TeacherModel(PersonModel):
    subject = models.ForeignKey('statistic.SubjectModel',on_delete=models.CASCADE)
    TOIFA_TEACHER = (
        ("OM","Oliy Ma'lumot"),
        ("OR","O'rta Ma'lumot"),
        ("OP","O'qituvchi Pedagok"),
    )
    toifa = models.CharField(max_length=2,choices=TOIFA_TEACHER,default='')
    salary = models.PositiveIntegerField(default=1)
    school = models.ManyToManyField('school.SchoolModel')

    def __str__(self):
        return f"{self.name} {self.fname}"

    class Meta:
        db_table = 'teacher'
