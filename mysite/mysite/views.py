from django.http import HttpResponse
from django.template import loader
from seoilNotice.views import SeoilNotice, EventInfo, BachelorNotice
from seoilLibraryNotice.views import NewsInfo, LibNotice

#https://oneone-note.tistory.com/36
def index(request):
    latest_post_list = SeoilNotice.objects.all().order_by('id')[:5]
    latest_event_list = EventInfo.objects.all().order_by('id')[:5]
    latest_bachelor_list = BachelorNotice.objects.all().order_by('id')[:5]
    latest_libnews_list = LibNotice.objects.all().order_by('id')[:5]
    latest_libnotice_list = NewsInfo.objects.all().order_by('id')[:5]

    template = loader.get_template('home.html')
    context = {
        'latest_post_list': latest_post_list,
        'latest_event_list': latest_event_list,
        'latest_bachelor_list': latest_bachelor_list,
        'latest_libnews_list': latest_libnews_list,
        'latest_libnotice_list': latest_libnotice_list,
    }
    return HttpResponse(template.render(context, request))
