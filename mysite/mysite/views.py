from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic import TemplateView
from django.views.generic import ListView, DayArchiveView
from seoilNotice.views import SeoilNotice


class PostListView(ListView):
    model = SeoilNotice
    latest_post = SeoilNotice.objects.all().order_by('date')[:5]
    context_object_name = 'posts'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = SeoilNotice.objects.all().order_by('id')[:5]
        return context



#https://oneone-note.tistory.com/36
def index(request):
    latest_post_list = SeoilNotice.objects.all().order_by('id')[:5]
    template = loader.get_template('home.html')
    context = {
        'latest_post_list': latest_post_list,
    }

    return HttpResponse(template.render(context, request))

class HomePageView(TemplateView):
    template_name = "home.html"
    model = SeoilNotice
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['title'] = SeoilNotice.objects.all()[:5]
        return context
