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
        for item in news_json:
            if item['link'] == link_id:
                return render(request, 'news/news_detail.html', item)
        # news/
        return HttpResponse("News not found")