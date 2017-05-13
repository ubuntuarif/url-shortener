from django.conf.urls import url
from django.contrib import admin
from shortener.views import HomeView, KirrCBView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    # url(r'^a/(?P<shortcode>[\w-]+)/$', kirr_redirect_view),
    url(r'^(?P<shortcode>[\w-]+)/$', KirrCBView.as_view())
]
