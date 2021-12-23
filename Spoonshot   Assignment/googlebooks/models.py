from django.db import models
from django.utils import timezone

class Books(models.Model):
	book_name=models.CharField(max_length=200)
	ID= models.CharField(max_length=200, primary_key= True, default= "" )
	created_at =  models.DateTimeField(auto_now_add= True)
	preview_link=models.URLField(max_length=200)
	count= models.IntegerField(default=0)
	def __str__(self):
		return self.book_name
	