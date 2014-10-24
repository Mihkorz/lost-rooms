
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from website.views import IndexPage


admin.autodiscover()

urlpatterns = patterns('',
                       
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', IndexPage.as_view(), name='index'),
    

    
)
