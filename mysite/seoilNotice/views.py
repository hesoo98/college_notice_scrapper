from django.views.generic import ListView, FormView
from seoilNotice.models import SeoilNotice, EventInfo, BachelorNotice
from seoilNotice.forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render


class NoticeListView(ListView):
    model = SeoilNotice
    context_object_name = 'notices'


class EventInfoListView(ListView):
    model = EventInfo
    context_object_name = 'events'


class BachelorNoticeListView(ListView):
    model = BachelorNotice
    context_object_name = 'bachelor'


class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'seoilNotice/search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        post_list = SeoilNotice.objects.filter(Q(title__icontains=searchWord) |
                                               Q(date__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)
