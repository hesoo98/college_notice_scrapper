from django.views.generic import ListView
from seoilNotice.models import SeoilNotice, EventInfo, BachelorNotice


class NoticeListView(ListView):
    model = SeoilNotice
    context_object_name = 'notices'


class EventInfoListView(ListView):
    model = EventInfo
    context_object_name = 'events'


class BachelorNoticeListView(ListView):
    model = BachelorNotice
    context_object_name = 'bachelor'
