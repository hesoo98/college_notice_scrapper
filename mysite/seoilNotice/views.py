from django.shortcuts import render
from django.views.generic import ListView, DetailView
from seoilNotice.models import SeoilNotice

class PostListView(ListView):
    model = SeoilNotice

class PostDetailView(DetailView):
    model = SeoilNotice