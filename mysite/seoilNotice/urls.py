from django.urls import path
from seoilNotice.views import NoticeListView

app_name = 'seoilNotice'
urlpatterns = [
    path('', NoticeListView.as_view(), name='seoilNotice')
]