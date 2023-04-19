from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
