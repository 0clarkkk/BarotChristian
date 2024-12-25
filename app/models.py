from django.db import models
from django.contrib.auth.models import User

class SUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, null=True)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=10, null=True)
    type = models.CharField(max_length=15, null=True)
    
    def __str__(self):
        return self.user.username
    
class Recruiter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, null=True)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=10, null=True)
    company = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=20, null=True)
    status = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return self.user.username
     
class Job(models.Model):
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=100)
    salary = models.CharField(max_length=20)
    image = models.FileField(null=True)
    description = models.CharField(max_length=300)
    experience = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)
    creationdate = models.DateField()
    
    def __str__(self):
        return self.title
    
class Apply(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    suser = models.ForeignKey(SUser, on_delete=models.CASCADE)
    resume = models.FileField(null=True)
    applydate = models.DateField()
    
    def __str__(self):
        return f'{self.suser.user.username} applied for {self.job.title}'


class Record(models.Model):
    apply = models.ForeignKey(Apply, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Record for {self.apply}'
    
    
    
    
    

    
    
