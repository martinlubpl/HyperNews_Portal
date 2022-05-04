import os.path

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import json


# Create your views here.
def home(request):
    return HttpResponse("Coming soon")


def news(request, link_id=None):
    full_json_path = os.path.join(settings.BASE_DIR, 'hypernews\\', settings.NEWS_JSON_PATH)
    with open(full_json_path, 'r') as f:
        news_json = json.load(f)

        dates = []
        for item in news_json:
            item_date = item['created'].split()[0]
            # skip and show 1 post
            if item['link'] == link_id:
                return render(request, 'news/news_detail.html', item)

            if item_date not in dates:
                dates.append(item_date)
        dates.sort(reverse=True)

        news_dict = {}
        for date in dates:
            day_list = []
            for news_item in news_json:
                if news_item['created'].split()[0] == date:
                    day_list.append((news_item['title'], news_item['link']))
            news_dict[date] = dict(day_list)
        context = {'news_dict': news_dict}
        print(context)
        # news/
        return render(request, 'news/news_list.html', context)
