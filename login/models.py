from __future__ import unicode_literals
from django.db import models

# Create your models here.

class login(models.Model):

	name = models.CharField(max_length=30)
	number = models.CharField(max_length=10)
	otp = models.CharField(max_length=6)


	def name(self):
		return self.name

	def number(self):
		return self.number

	def otp(self):
		return self.otp

