from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xyjie.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/(\w+)/(\w+)/(\w+)/$', 'xyjie.views.test'),
    url(r'^$', 'xyjie.views.index'),
)
