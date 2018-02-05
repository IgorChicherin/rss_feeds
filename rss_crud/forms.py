import feedparser
import requests
from django import forms

from .models import NewsItems, RssLinks


class NewsItemForm(forms.ModelForm):
    title = forms.TextInput()
    description = forms.Textarea()

    class Meta:
        model = NewsItems
        fields = '__all__'


class RssLinkForm(forms.ModelForm):
    rss_link = forms.URLField()

    def save(self, commit=True):
        instance = super(RssLinkForm, self).save()
        request = requests.get(self.rss_link)
        news_feeds = feedparser.parse(request.text)
        for feed in news_feeds['entries']:
            news_item = NewsItems(title=feed['title'], description=feed['description'])
            news_item.save()
            RssLinks.objects.create(
                rss_link=feed['link'],
                news_link_id=news_item.id
            )
        return instance

    class Meta:
        model = RssLinks
        fields = '__all__'
