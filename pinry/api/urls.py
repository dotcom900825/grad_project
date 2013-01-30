from django.conf.urls import patterns, include, url

from .api import PinResource
from .api import UserResource
from .api import MyProfileResource
from .api import ActivityResource

pin_resource = PinResource()
user_resource = UserResource()
myprofile_resource = MyProfileResource()
activity_resource = ActivityResource()

urlpatterns = patterns('',
    url(r'', include(pin_resource.urls)),
    url(r'', include(user_resource.urls)),
 	url(r'', include(myprofile_resource.urls)),
    url(r'', include(activity_resource.urls)),
)
