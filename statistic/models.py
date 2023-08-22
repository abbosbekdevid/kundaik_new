from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class SubjectModel(models.Model):
    name = models.CharField(max_length=67,default='')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'subject'

class AttendanceModel(models.Model):
    student = models.ForeignKey('account.StudentModel',on_delete=models.CASCADE)
    subject = models.ForeignKey(SubjectModel,on_delete=models.SET_NULL,null=True)
    teacher = models.ForeignKey('account.TeacherModel',on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.student.name

    class Meta:
        db_table = 'attendance'

class GradeModel(models.Model):
    student = models.ForeignKey('account.StudentModel',on_delete=models.CASCADE)
    subject = models.ForeignKey(SubjectModel,on_delete=models.SET_NULL,null=True)
    teacher = models.ForeignKey('account.TeacherModel',on_delete=models.SET_NULL,null=True)
    mark = models.PositiveSmallIntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(5)])
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.student.name

    class Meta:
        db_table = 'grade'
