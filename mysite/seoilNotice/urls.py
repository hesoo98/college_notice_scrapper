from django.urls import path

from seoilNotice import views
from seoilNotice.views import NoticeListView, EventInfoListView, BachelorNoticeListView

app_name = 'seoilNotice'
urlpatterns = [
    path('notice', NoticeListView.as_view(), name='notice'),
    path('event', EventInfoListView.as_view(), name='event'),
    path('bachelor', BachelorNoticeListView.as_view(), name='bachelor'),
    path('search/', views.SearchFormView.as_view(), name='search'),
]