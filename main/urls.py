from django.conf.urls.defaults import *
from oneloudrhours.main.views import *


urlpatterns = patterns('',
#    (r'^captain_fan/$', fan),
#    (r'^express/$', express),
#    (r'^schoolbox/$', school_box),
#    (r'^competition/$', competition),
#
#    (r'^$', fan),
    (r'^/$', admin.site.root),
)