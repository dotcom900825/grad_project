from django.conf.urls import patterns, url


urlpatterns = patterns('pinry.askPeopleOut.views',
    url(r'^$', 'recent_activity', name='recent-activities'),
    url(r'^tag/.+/$', 'recent_activity', name='tag'),
    url(r'^new-activity/$', 'new_activity', name='new-pin'),
    url(r'^delete-activity/(?P<activity_id>\d+)/$', 'delete_activity', name='delete-activity'),
)
