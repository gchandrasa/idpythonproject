from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('views',
    # Examples:
    # url(r'^$', 'idpython.views.home', name='home'),
    # url(r'^idpython/', include('idpython.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^$', 'index'),
    url(r'^admin/', include(admin.site.urls)),
)
