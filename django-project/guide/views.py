# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from bakery.views import BuildableListView, BuildableDetailView

from .models import Topic,Post,Video

# Create your views here.

class HomePageView(BuildableListView):
    queryset = Post.objects.all()
    model = Post

    template_name = 'guide/home.html'
    build_path = 'workingatkbia/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['topics'] = Topic.objects.all()
        return context

class TopicDetailView(BuildableDetailView):
    model = Topic
    template_name = 'guide/topic_detail.html'

    def get_object(self):
        if self.kwargs['slug']:
            return Topic.objects.get(slug=self.kwargs['slug'])
        return super(TopicDetailView, self).get_objects()

class VideoDetailView(BuildableDetailView):
    model = Video
    template_name = 'guide/video_detail.html'

    def get_object(self):
        if self.kwargs['slug']:
            return Video.objects.get(slug=self.kwargs['slug'])
        return super(VideoDetailView, self).get_objects()

class PostDetailView(BuildableDetailView):
    model = Post
    template_name = 'guide/post_detail.html'

    def get_object(self):
        if self.kwargs['slug']:
            return Post.objects.get(slug=self.kwargs['slug'])
        return super(PostDetailView, self).get_objects()