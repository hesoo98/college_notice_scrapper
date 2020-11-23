from django.views.generic import ListView
from seoilLibraryNotice.models import LibNotice, NewsInfo


class LibNoticeListView(ListView):
    model = LibNotice
    context_object_name = 'lib_notices'


class NewsInfoListView(ListView):
    model = NewsInfo
    context_object_name = 'news'


