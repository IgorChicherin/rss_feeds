from django.shortcuts import render, render_to_response
from django.views.generic import ListView

from rss_crud.models import NewsItems, RssLinks

# Create your views here.


class FeedsListView(ListView):
    model = NewsItems
    context_object_name = 'news_items'
    template_name = 'index.html'