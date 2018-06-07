from django.conf.urls import include, url
from django.contrib import admin

from . import view,login,editprofile
from . import editprofile,notification,myappeal,myappeal_details,myhelp,accept

urlpatterns = [
    # Examples:
    # url(r'^$', 'state59.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index$', view.index),
    url(r'^editprofile$', editprofile.index),
    url(r'^notification$', notification.index),
    url(r'^myappeal$', myappeal.index),
    url(r'^myappeal_details$', myappeal_details.index),
    url(r'^accept$', accept.index),
    url(r'^myhelp$', myhelp.index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login', login.index),
]
