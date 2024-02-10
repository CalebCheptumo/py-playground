"""
URL configuration for ll_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin #import the admin module from django.contrib
from django.urls import path , include  #import the path function from django.urls module , include function from django.urls module
 #urlpatterns variable includes a set of URLs from the apps in the project, the list includes the module admin.site.urls, which defines all the URLs that can be requested from the admin site.
urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', include('learning_logs.urls')) #include the urls from the learning_logs app. the include function allows us to reference the urls from the learning_logs app.
]
