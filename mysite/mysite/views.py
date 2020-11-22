from django.views.generic import TemplateView
from django.views.generic import ListView, DayArchiveView

from seoilNotice.views import SeoilNotice

#class HomeView(TemplateView):
#    template_name = 'home.html'

class PostListView(ListView):
    model = SeoilNotice
    #latest_title = SeoilNotice.objects.all().order_by('date')[:5]
    context_object_name = 'posts'
    template_name = 'home.html'

class LastNotice(DayArchiveView):
    model = SeoilNotice
    date_field = 'modify_dt'