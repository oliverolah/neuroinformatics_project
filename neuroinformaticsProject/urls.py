from django.contrib import admin
from django.urls import path
from homeroots.views import returnHomePage
from submitdata.views import returnSubmitDataPage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(r'', returnHomePage, name='home'), # Root of application
    path(r'admin/', admin.site.urls, name='admin'),
    path(r'submit_data_page/', returnSubmitDataPage, name='submitdatapage'),
] 

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
