from django.views.generic import ListView

from rss_crud.models import NewsItems


# Create your views here.


class FeedsListView(ListView):
    model = NewsItems
    context_object_name = 'news_items'
    template_name = 'index.html'

    def get_queryset(self):
        return NewsItems.objects.all().order_by('-date')


class LastFiftyFeedsListView(FeedsListView):

    def get_queryset(self):
        return NewsItems.objects.all().order_by('-date')[:50]
