from django.conf.urls import patterns, include, url
from django.contrib import admin
# from tweets import views
from tweets.views import Index 

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_bookmarks.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', views.index, name='index')
    url(r'^$', Index.as_view()),
)
