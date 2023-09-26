from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Tasks(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='task')
    title=models.CharField(max_length=100)
    description=models.TextField(null=True,blank=True)
    complete=models.BooleanField(max_length=255,default=False)
    date=models.DateField(auto_now_add=True)
    

    TASK_PENDING='P'
    TASK_COMPLETE='C'
    TASK_INPROGRESS='IP'

    TASK_CHOICE=[
        (TASK_PENDING,"PENDING"),
        (TASK_INPROGRESS,'IN PROGESS'),
        (TASK_COMPLETE,'COMPLETED'),
    ]
    status=models.CharField(max_length=255,choices=TASK_CHOICE,default=TASK_PENDING, blank=True, null=True)

    def __str__(self) -> str:
        return self.title





