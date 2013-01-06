from django.conf.urls import patterns, include, url

from .api import PinResource
from .api import UserResource
from .api import MyProfileResource

pin_resource = PinResource()
user_resource = UserResource()
myprofile_resource = MyProfileResource()


urlpatterns = patterns('',
    url(r'', include(pin_resource.urls)),
    url(r'', include(user_resource.urls)),
 	url(r'', include(myprofile_resource.urls)),
       
)
