# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Topic (models.Model):
    slug = models.SlugField("Slug",
        max_length=64,
        unique=True)
    name = models.CharField("Name",
        max_length=256)
    order = models.IntegerField("Order",
                                default=999)

    def __str__(self):
        return "%s" % (self.name)

    def get_absolute_url(self):
        return "/workingatkbia/topics/%s/" % (self.slug)

    class Meta:
        ordering = ['order','slug']

class Post (models.Model):
    slug = models.SlugField("Slug",
        max_length=64,
        unique=True)
    name = models.CharField("Name",
        max_length=512)
    text = models.TextField("Text",
        help_text="The post's content. Supports Markdown.")
    topic = models.ForeignKey(Topic,
        related_name="posts",
        related_query_name="post")

    def __str__(self):
        return "%s" % (self.name)

    def get_absolute_url(self):
        return "/workingatkbia/posts/%s/" % (self.slug)

    class Meta:
        ordering = ['slug']

class Video (models.Model):
    slug = models.SlugField("Slug",
        max_length=64,
        unique=True)
    name = models.CharField("Name",
        max_length=512)
    embed_url = models.CharField("Embed URL",
        max_length=2048,
        help_text="The YouTube or Vimeo URL into the vanilla iframe of the video.")
    topic = models.ForeignKey(Topic,
                              related_name="videos",
                              related_query_name="video")

    def __str__(self):
        return "%s" % (self.name)

    def get_absolute_url(self):
        return "/workingatkbia/videos/%s/" % (self.slug)

    class Meta:
        ordering = ['slug']

class File (models.Model):
    slug = models.SlugField("Slug",
        max_length=64,
        unique=True)
    name = models.CharField("Name",
        max_length=512)
    file = models.FileField("Upload File")
    topic = models.ForeignKey(Topic,
                              related_name="files",
                              related_query_name="file")

    def __str__(self):
        return "%s" % (self.name)

    def get_absolute_url(self):
        return self.file.url

    class Meta:
        ordering = ['slug']


class Link (models.Model):
    slug = models.SlugField("Slug",
        max_length=64,
        unique=True)
    name = models.CharField("Name",
        max_length=512)
    url = models.URLField("URL")
    topic = models.ForeignKey(Topic,
                              related_name="links",
                              related_query_name="link")

    def __str__(self):
        return "%s" % (self.name)

    def get_absolute_url(self):
        return self.url

    class Meta:
        ordering = ['slug']
