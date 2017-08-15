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