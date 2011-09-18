from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^captain/', include('captain.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    #(r'^admin/', include(admin.site.urls)),
    
#    (r'^', include('oneloudrhours.main.urls')),

    (r'^$', admin.site.root),
)



if settings.DEBUG:
    urlpatterns += patterns('',
#        (r'^media/cms/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.CMS_MEDIA_ROOT }),

#        (r'^media/cms/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': '/opt/local/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/site-packages/django_cms-2.0.2-py2.6.egg/cms/media/cms' }),

        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)


