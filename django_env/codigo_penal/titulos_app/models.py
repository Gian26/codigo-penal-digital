from django.db import models


class Title(models.Model):
    name = models.CharField(max_length=300, db_index=True)
    description = models.CharField(max_length=300, db_index=True)

class Chapter(models.Model):
    chapter = models.IntegerField(unique=False)
    title = models.ForeignKey('titulos_app.Title')
    description = models.CharField(max_length=400)

class Article(models.Model):
    number = models.IntegerField(unique=False)
    body = models.CharField(max_length = 600)
    chapter = models.ForeignKey('titulos_app.Chapter')

class CrimeType(models.Model):
    crime_name = models.CharField(max_length = 400)
    description = models.CharField(max_length = 400)
    category = models.ForeignKey('titulos_app.Category',default=1)

class Category(models.Model):
    name = models.CharField(max_length=400, db_index=True)

class CategoryCrime(models.Model):
    crime_type = models.ForeignKey('titulos_app.CrimeType')
    chapter = models.ForeignKey('titulos_app.Chapter',default=1)
