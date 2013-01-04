from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from accounts.forms import SignupForm,AuthenticationForm


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('pinry.api.urls', namespace='api')),
    url(r'^pins/', include('pinry.pins.urls', namespace='pins')),
    url(r'^about_us/','pinry.core.views.about_us'),
    url(r'', include('pinry.core.urls', namespace='core')),
    url(r'^accounts/signup/$', #because here we are importing the form from account app, therefore we have customized form
 	'userena.views.signup',{'signup_form': SignupForm}),
 	url(r'^accounts/signin/$', #because here we are importing the form from account app, therefore we have customized form
 	'userena.views.signin',{'auth_form': AuthenticationForm}),
    url(r'^accounts/', include('userena.urls')),
    url(r'^messages/', include('userena.contrib.umessages.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
