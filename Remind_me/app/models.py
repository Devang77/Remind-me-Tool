from django.db import models

class remind_user(models.Model):
    username=models.CharField(unique=True,max_length=50,null=True,blank=True)
    password=models.CharField(unique=True,max_length=50,null=True,blank=True)
    email=models.EmailField(max_length=254,null=True,blank=True)
class reminder(models.Model):
    user_id=models.ForeignKey(remind_user,on_delete=models.CASCADE,null=True,blank=True)
    email=models.EmailField(max_length=254,null=True,blank=True)
    reminder_description=models.TextField(max_length=200,null=True,blank=True)
    remind_date=models.DateField(null=True,blank=True)
    reminder_status=models.CharField(max_length=50,null=True,blank=True)


