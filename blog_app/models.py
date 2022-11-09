from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
	post = models.CharField(max_length=1000, blank=False, null=True)
	post_created_on = models.DateTimeField(auto_now_add=True, null=True)
	post_author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.post}, {self.post_author}, {self.post_created_on}'

	class Meta:
		ordering = ['-post_created_on']


class Comment(models.Model):
	comment = models.CharField(max_length=1000, blank=False, null=True)
	comment_created_on = models.DateTimeField(auto_now_add=True, null=True)
	commented_post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=False, null=True)
	comment_author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.comment}, {self.commented_post}, {self.comment_author}, {self.comment_created_on}'

	class Meta:
		ordering = ['-comment_created_on']