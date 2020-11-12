from django.urls import path
from seoilNotice.views import PostListView, PostDetailView

app_name = 'seoilNotice'
urlpatterns = [
    path('', PostListView.as_view(), name='index')
]