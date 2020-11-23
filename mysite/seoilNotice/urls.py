from django.urls import path
from seoilNotice.views import NoticeListView, EventInfoListView

app_name = 'seoilNotice'
urlpatterns = [
    path('notice', NoticeListView.as_view(), name='notice'),
    path('event', EventInfoListView.as_view(), name='event')
]