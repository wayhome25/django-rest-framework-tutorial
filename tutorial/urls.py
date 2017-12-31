"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin

from snippets import views

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^admin/', admin.site.urls),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>\d+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^snippets/$', views.SnippetList.as_view(), name='snippet-list'),
    url(r'^snippets/(?P<pk>\d+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
    url(r'^snippets/(?P<pk>\d+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    url(r'^api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
