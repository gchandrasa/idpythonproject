from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('views',
    # Examples:
    # url(r'^$', 'idpython.views.home', name='home'),
    # url(r'^idpython/', include('idpython.foo.urls')),

    url(r'^$', 'index'),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    #(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
