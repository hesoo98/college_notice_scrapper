from django.views.generic import TemplateView
from django.views.generic import ListView

from seoilNotice.views import SeoilNotice

#class HomeView(TemplateView):
#    template_name = 'home.html'

class PostListView(ListView):
    model = SeoilNotice
    context_object_name = 'posts'
    template_name = 'home.html'