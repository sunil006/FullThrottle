from django.db import models



class User(models.Model):
	vat_id = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	

class Activity(models.Model):
	uid = models.ForeignKey(User, on_delete=models.CASCADE)
	startdate = models.DateTimeField()
	enddate = models.DateTimeField()





