"""birthday_application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.homepage, name='homepage')
Class-based views
    1. Add an import:  from other_app.views import Homepage
    2. Add a URL to urlpatterns:  url(r'^$', Homepage.as_view(), name='homepage')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^birthday/', include('birthday.urls')),
    url(r'^admin/', admin.site.urls),

]
