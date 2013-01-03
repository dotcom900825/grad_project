from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from accounts.forms import SignupForm

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('pinry.api.urls', namespace='api')),
    url(r'^pins/', include('pinry.pins.urls', namespace='pins')),
    url(r'', include('pinry.core.urls', namespace='core')),
    (r'^accounts/signup/$',
 	'userena.views.signup',{'signup_form': SignupForm}),
    url(r'^accounts/', include('userena.urls')),
    url(r'^messages/', include('userena.contrib.umessages.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
