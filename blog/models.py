from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
	STATUS = (
		('rascunho', 'Rascunho'),
		('publicacao', 'Publicacao'))
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=250)
	athor = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField()
    
	publicacao = models.DateTimeField(default=timezone.now) 
	criado = models.DateTimeField(auto_now_add=True)
	alterado = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS, default='rascunho')

	class Meta:
		ordering = ('-publicacao',)

	def __str__(self):
		return f'{self.title}'

# Create your models here.
