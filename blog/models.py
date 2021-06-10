from django.db import models


class Blog(models.Model):

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог'

    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title