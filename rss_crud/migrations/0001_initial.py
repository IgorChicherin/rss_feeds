# Generated by Django 2.0.2 on 2018-02-05 20:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Текст новости')),
                ('date', models.DateField(default=datetime.date(2018, 2, 5))),
            ],
        ),
        migrations.CreateModel(
            name='RssLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rss_link', models.URLField(verbose_name='Ссылка на feed')),
                ('news_link_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rss_crud.NewsItems')),
            ],
        ),
    ]
