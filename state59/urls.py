from django.conf.urls import include, url
from django.contrib import admin

import settings
from . import view,login,frontpage,submit
from . import editprofile,notification,myappeal,myhelp

from . import add
urlpatterns = [
    # Examples:
    # url(r'^$', 'state59.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index$', view.index),
    url(r'^submit$', submit.index),
    url(r'^info$', submit.submitinfo),
    url(r'^frontpage$', frontpage.reply),
    url(r'^detail$', frontpage.detail),
    url(r'^editprofile$', editprofile.index),
    url(r'^notification$', notification.index),
    url(r'^myappeal$', myappeal.index),
    url(r'^myappeal_details$', myappeal.details),
    url(r'^myappeal_accept$', myappeal.accept),
    url(r'^myappeal_finish$', myappeal.finish),
    url(r'^myhelp$', myhelp.index),
    url(r'^addhelp$', add.addhelp),
    url(r'^uploadimg$', add.addimage),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login', login.index),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
]
