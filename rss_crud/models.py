from datetime import date

from django.db import models


# Create your models here.

class NewsItems(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Текст новости')
    date = models.DateField(default=date.today())
    rss_link = models.ForeignKey('RssLinks', on_delete=models.CASCADE, null=True)


class RssLinks(models.Model):
    rss_link = models.URLField(verbose_name='Ссылка на feed')