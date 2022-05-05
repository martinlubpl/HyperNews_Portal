from datetime import datetime
import os.path
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
import json
from django.views import View


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


class CreateNews(View):
    def get(self, request):
        return render(request, 'news/create_news.html')

    def post(self, request):
        full_json_path = os.path.join(settings.BASE_DIR, 'hypernews\\', settings.NEWS_JSON_PATH)
        with open(full_json_path, 'r') as f:
            news_json = json.load(f)
        # find max id and add 1
        ids = [x['link'] for x in news_json]
        new_id = max(ids) + 1
        # todo: find first available int for id ?
        # date
        now = datetime.now().strftime("%Y.%m.%d %H:%M:%S")
        # data from form
        title = request.POST['title']
        text = request.POST['text']
        # dictionary to append
        dict_ = {'created': now, 'text': text, 'title': title, 'link': new_id}
        # append to json
        news_json.append(dict_)
        # write to json
        with open(full_json_path, 'w') as f:
            json.dump(news_json, f)
        # redirect to /news/
        return redirect('/news/')
