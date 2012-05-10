from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('task_1.views',
    url(r'^index/$', 'index'),
    url(r'^result/$', 'result'),
    url(r'^index/work/$', 'work'),
    url(r'^time/$', 'time'),
    url(r'^$', 'empty'),
    #url(r'^time/date/$', 'index'),
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^myproject/', include('myproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
