from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_social_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', 'django_social_app.views.login'),
    url(r'^home/$', 'django_social_app.views.home'),
    url(r'^logout/$', 'django_social_app.views.logout'),
    url(r'^admin/', include(admin.site.urls)),
)
