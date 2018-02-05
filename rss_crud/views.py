from django.shortcuts import render

from django.views.generic import UpdateView, ListView, CreateView

from .models import RssLinks
from .forms import RssLinkForm


# Create your views here.

class RssLinksCreateView(CreateView):
    model = RssLinks
    context_object_name = 'rss_links'
    form_class = RssLinkForm
    template_name = 'crud.html'


class RssLinksView(ListView):
    model = RssLinks
    context_object_name = 'rss_links'
    template_name = 'crud.html'


class RssLinksUpdateView(UpdateView):
    model = RssLinks
    form_class = RssLinkForm
    context_object_name = 'rss_links'
    template_name = 'crud.html'
