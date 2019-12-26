from django.db import models

# Create your models here.




class LinkData(models.Model):
	title = models.CharField(max_length=100)
	link = models.URLField()
	detail = models.TextField(null=True,blank=True)
	category = models.ForeignKey('LinkCategory',on_delete=models.CASCADE,null=True,blank=True)

class LinkCategory(models.Model):
	category = models.CharField(max_length=50)