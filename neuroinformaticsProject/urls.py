from django.contrib import admin
from django.urls import path
from homeroots.views import returnHomePage
from submitdata.views import returnSubmitDataPage
from contactus.views import returnContactUsPage
from aboutcontent.views import returnAboutPage
from keysources.views import returnKeySourcesPage
from neurons.views import returnVisualisationPage
from django.conf import settings
from django.conf.urls.static import static
# from neuroinformaticsProject.views import err404Handler # For trying out template designs 

# handler400 = 'neuroinformaticsProject.views.err400Handler'
# handler403 = 'neuroinformaticsProject.views.err403Handler'
# handler404 = 'neuroinformaticsProject.views.err404Handler'
# handler500 = 'neuroinformaticsProject.views.err500Handler'


urlpatterns = [
    path(r'', returnHomePage, name='home'), # Root of application
    path(r'admin/', admin.site.urls, name='admin'),
    path(r'visualisations/', returnVisualisationPage, name='visualisationspage'),
    path(r'submit_data_page/', returnSubmitDataPage, name='submitdatapage'),
    path(r'contact_us_page/', returnContactUsPage, name='contactuspage'),
    path(r'about_page/', returnAboutPage, name='aboutpage'),
    path(r'key_sources/', returnKeySourcesPage, name='keyappsources'),
    # path(r'err404/', err404Handler, name='err404'), # For trying out template designs 
] 

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
