from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.
class Opinion(models.Model):
	author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	title=models.CharField(max_length=200)
	text=models.TextField()
	created_date=models.DateTimeField(default=timezone.now)
	published_date=models.DateTimeField(null=True,blank=True)

	def __str__(self):
		return self.title

	def publish(self):
		self.published_date=timezone.now()
		self.save()
	def approved_comments(self):
		return self.comments.filter(approved_comment=True)
		
class Comment(models.Model):
    opinion = models.ForeignKey('opinion.Opinion', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text