from django.shortcuts import render
from django.views.generic import ListView, DetailView
from seoilNotice.models import SeoilNotice, EventInfo

'''class PostListView(ListView):
    model = SeoilNotice'''


class NoticeListView(ListView):
    model = SeoilNotice

class EventInfoListView(ListView):
    model = EventInfo