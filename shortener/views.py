from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import KirrURL

# Create your views here.

# def kirr_redirect_view(request, shortcode=None, *args, **kwargs):  # function based view FBV
#     obj = get_object_or_404(KirrURL, shortcode=shortcode)
#     print(obj.url)
#     return HttpResponseRedirect(obj.url)

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'shortener/home.html', {})

class KirrCBView(View):  # class based view
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)

    # def post(self, request, *args, **kwargs):
    #     return HttpResponse()
