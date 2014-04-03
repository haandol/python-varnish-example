#coding: utf-8

import time
from django.shortcuts import render
from django.views.decorators.cache import cache_page, never_cache


@never_cache
def static_view(request):
    return render(request, "static.html", locals())

@cache_page(60*5)
def dynamic_view(request):
    time.sleep(2)
    return render(request, "dynamic.html", locals())

@never_cache
def index_view(request):
    USE_ESI = True
    if not USE_ESI:
        time.sleep(2)
    return render(request, "index.html", locals())
