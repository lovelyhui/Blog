from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=20, blank=True)
    create_time = models.TimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class Classification(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    caption = models.CharField(max_length=50)
    author = models.ForeignKey(Author)
    tags = models.ManyToManyField(Tag, blank=True)
    classification = models.ForeignKey(Classification)
    content = models.TextField()
    publish_time = models.TimeField(auto_now_add=True)

    def __unicode__(self):
        return self.caption


