from django.conf.urls import include, url
from django.contrib import admin

from . import view

urlpatterns = [
    # Examples:
    # url(r'^$', 'state59.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index$', view.index),
    url(r'^admin/', include(admin.site.urls)),
]
