from django.views.generic import UpdateView, ListView, CreateView, DeleteView

from .forms import RssLinkForm, RssLinkParseForm
from .models import RssLinks


# Create your views here.

class RssLinksCreateView(CreateView):
    model = RssLinks
    form_class = RssLinkParseForm
    template_name = 'crud.html'
    success_url = '/'


class RssLinksView(ListView):
    model = RssLinks
    context_object_name = 'rss_links'
    template_name = 'crud.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RssLinkParseForm()
        return context


class RssLinksUpdateView(UpdateView):
    model = RssLinks
    form_class = RssLinkForm
    template_name = 'edit-rss.html'
    success_url = '/feeds/'


class RssLinksDeleteView(DeleteView):
    model = RssLinks
    template_name = 'delete-rss-confirm.html'
    success_url = '/feeds/'