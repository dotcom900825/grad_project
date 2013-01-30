from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization

from django.contrib.auth.models import User
from accounts.models import MyProfile
from pinry.pins.models import Pin
from pinry.askPeopleOut.models import OutActivity


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'password', 'is_superuser']
        # Add it here.
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()

class MyProfileResource(ModelResource):
    user = fields.ForeignKey(UserResource,'user',full=True)
    class Meta:
        queryset = MyProfile.objects.all()
        resource_name = 'myprofile'
        # Add it here.
      #  authentication = BasicAuthentication()
      #  authorization = DjangoAuthorization()

class PinResource(ModelResource):  # pylint: disable-msg=R0904
    tags = fields.ListField()
    userProfile = fields.ForeignKey(MyProfileResource,'submitter',full=True)
    class Meta:
        queryset = Pin.objects.all()
        resource_name = 'pin'
        include_resource_uri = False
        filtering = {
            'published': ['gt'],
        }

    def build_filters(self, filters=None):
        if filters is None:
            filters = {}

        orm_filters = super(PinResource, self).build_filters(filters)

        if 'tag' in filters:
            orm_filters['tags__name__in'] = filters['tag'].split(',')

        return orm_filters

    def dehydrate_tags(self, bundle):
        return map(str, bundle.obj.tags.all())

    def save_m2m(self, bundle):
        tags = bundle.data.get('tags', [])
        bundle.obj.tags.set(*tags)
        return super(PinResource, self).save_m2m(bundle)


class ActivityResource(ModelResource):  # pylint: disable-msg=R0904
    tags = fields.ListField()
    userProfile = fields.ForeignKey(MyProfileResource,'submitter',full=True)
    class Meta:
        queryset = OutActivity.objects.all()
        resource_name = 'activity'
        include_resource_uri = False
        filtering = {
            'published': ['gt'],
        }

    def build_filters(self, filters=None):
        if filters is None:
            filters = {}

        orm_filters = super(ActivityResource, self).build_filters(filters)

        if 'tag' in filters:
            orm_filters['tags__name__in'] = filters['tag'].split(',')

        return orm_filters

    def dehydrate_tags(self, bundle):
        return map(str, bundle.obj.tags.all())

    def save_m2m(self, bundle):
        tags = bundle.data.get('tags', [])
        bundle.obj.tags.set(*tags)
        return super(ActivityResource, self).save_m2m(bundle)


