from django.db import models


class Project(models.Model):

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
