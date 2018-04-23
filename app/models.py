from django.db import models


# Create your models here.
class Recipe(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    duration = models.PositiveSmallIntegerField()
    ingredients = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.name