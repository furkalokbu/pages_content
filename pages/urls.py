
from django.conf.urls import url
from .views import  pages_slug


urlpatterns = [

    url(r'^(?P<slug>[-\.\w\d]+)/$', pages_slug, name='pages_slug'),
]
