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

    class Meta:
        model = RssLinks
        fields = ('rss_link',)


class RssLinkParseForm(RssLinkForm):

    def save(self, commit=True):
        '''
        Parse added link and write to database
        :param commit: boolean
        :return: class RssLinks
        '''
        instance = super(RssLinkForm, self).save()
        request = requests.get(instance.rss_link)
        news_feeds = feedparser.parse(request.text)
        for feed in news_feeds['entries']:
            news_item = NewsItems(title=feed['title'], description=feed['description'], rss_link=instance)
            news_item.save()
        print(type(instance))
        return instance
