from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'(\d+)', 'acorta.views.cortas'),
    url(r'^post$', 'acorta.views.post'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'acorta.views.principal')
)
