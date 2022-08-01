"""dtproto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from core import views
from ltp import views as ltp_views
from lineage import views as lineage_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('ruteo/', views.ruteo, name="ruteo"),
    path('inbox', views.inbox, name="inbox"),
    path('do_full_test', views.do_full_test, name="do_full_test"),
    path('upload', views.upload, name="upload"),
    path('do_ini', views.do_ini, name="do_ini"),
    path('do_full', views.do_full, name="do_full"),
    path('do_dropzone', views.do_dropzone, name="do_dropzone"),
    path('lineage', views.lineage, name="lineage"),
    path('main', views.main, name="main"),
    path('wizard', ltp_views.wizard, name="wizard"),
    path('send', ltp_views.send, name="send"),
    path('lineage', lineage_views.lineage, name="lineage"),
    path('jqgrid', lineage_views.jqgrid, name="jqgrid"),
    path('felix', views.felix, name="felix"),
    path('alex', views.alex, name="alex"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)