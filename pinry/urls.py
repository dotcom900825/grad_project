from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin



admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('pinry.api.urls')),
    url(r'^pins/', include('pinry.pins.urls', namespace='pins')),
    url(r'^activities/', include('pinry.askPeopleOut.urls', namespace='activities')),
    url(r'^about_us/','pinry.core.views.about_us'),
    url(r'', include('pinry.core.urls', namespace='core')),
    url(r'ajax-upload$', 'accounts.views.import_uploader', name="my_ajax_upload"),
    url(r'^accounts/', include('userena.urls')),
    url(r'^messages/', include('userena.contrib.umessages.urls')),
    url(r'^feedback/', 'pinry.core.views.feedback'),
    url(r'^item/(?P<pin_id>[\.\w]+)/detail/$', 'pinry.pins.views.pin_detail'),
   

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
