from django.db import models

# Create your models here.


class MyUpload(models.Model):

	upload = models.FileField(upload_to='media_data')

	def __str__(self):
		return str(self.pk)
