from django.shortcuts import render
from django.views.generic import ListView, DetailView
from seoilNotice.models import SeoilNotice, EventInfo, BachelorNotice

'''class PostListView(ListView):
    model = SeoilNotice'''


class NoticeListView(ListView):
    model = SeoilNotice
    context_object_name = 'notices'

class EventInfoListView(ListView):
    model = EventInfo
    context_object_name = 'events'

class BachelorNoticeListView(ListView):
    model = BachelorNotice
    context_object_name = 'bachelor'
