from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('myproject/',
    url(r'', include ('task_1.urls')),

#urlpatterns = patterns('myproject.task_1.views',
#    url(r'^index/$', 'index'),
#    url(r'^result/$', 'result'),
#    url(r'^index/work/$', 'work'),
#    url(r'^time/$', 'time'),
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^myproject/', include('myproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
