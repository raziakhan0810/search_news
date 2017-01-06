
import requests

from django.shortcuts import render
from django.conf import settings


def bing_news(request):
    results = []
    if request.method == 'POST':
        q = request.POST['q']
        payload = {
            'q': q,
            'mkt': 'en-in'
        }
        headers = {'Ocp-Apim-Subscription-Key': settings.BING_NEWS_API_KEY}

        print 'url: ', settings.BING_NEWS_API_URL + 'search'
        print 'payload: ', payload
        print 'headers: ', headers

        response = requests.get(
            settings.BING_NEWS_API_URL + 'search',
            params=payload,
            headers=headers
        ).json()
        results = response['value']

    return render(request, 'bing_news.html', {'results': results})
