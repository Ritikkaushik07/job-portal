from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User=get_user_model()

class Datas(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    age=models.CharField(blank=True,max_length=200, null=True)
    qualification=models.CharField(blank=True,max_length=200,null=True)
    exp=models.CharField(blank=True,max_length=200,null=True)
    skills=models.CharField(blank=True,max_length=200,null=True)
    phone=models.CharField(blank=True,max_length=15, unique=True,null=True)
        
    def __str__(self) :
        return f"{self.user.username}'s profile"
    

class Jobs(models.Model):
    name=models.CharField(max_length=200)
    type=models.CharField(max_length=200)
    desc=models.TextField(max_length=100)
    address=models.TextField()
    phone=models.IntegerField()
    dead=models.DateField()

    def __str__(self) :
        return self.name
    
class ApplyJob (models.Model):
    status_choices=(
        ('Accepted', 'Accepted'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected')
    )
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    job=models.ForeignKey(Jobs, on_delete=models.CASCADE )
    status=models.CharField(max_length=20 , choices=status_choices)



    