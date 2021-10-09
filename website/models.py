from django.db import models

class ExecRole(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7)

class Exec(models.Model):
    name = models.CharField(max_length=100)
    mugshotBase64 = models.CharField(max_length=2500000)
    mugshotImageType = models.CharField(max_length=100)
    role = models.ForeignKey(ExecRole, null=True, on_delete=models.SET_NULL, related_name='execs')

class Tag(models.Model):
    color = models.CharField(max_length=7)
    name = models.CharField(max_length=100)

class Article(models.Model):
    title = models.CharField(max_length=100)
    bodyMarkdown = models.CharField(max_length=40000)
    authors = models.ManyToManyField(Exec, related_name='articles')
    tags = models.ManyToManyField(Tag, related_name='articles')
