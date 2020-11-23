from django.urls import path
from seoilLibraryNotice.views import LibNoticeListView, NewsInfoListView

app_name = 'libNotice'
urlpatterns = [
    path('notice', LibNoticeListView.as_view(), name='notice'),
    path('news', NewsInfoListView.as_view(), name='event'),
]
