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

    def __str__(self):
        return "%s" % (self.name)

    def get_absolute_url(self):
        return "/workingatkbia/topics/%s/" % (self.slug)

    class Meta:
        ordering = ['slug']

class Post (models.Model):
    slug = models.SlugField("Slug",
        max_length=64,
        unique=True)
    name = models.SlugField("Name",
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
    name = models.SlugField("Name",
        max_length=512)
    embed_url = models.CharField("Embed URL",
        max_length=2048,
        help_text="The YouTube or Vimeo URL into the vanilla iframe of the video.")

    def __str__(self):
        return "%s" % (self.name)

    def get_absolute_url(self):
        return "/workingatkbia/videos/%s/" % (self.slug)

    class Meta:
        ordering = ['slug']
