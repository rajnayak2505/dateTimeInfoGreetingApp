from django.conf.urls import url
from django.contrib import admin
from testApp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/', views.dateinfo),
]
