from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'pinry.core.views.home', name='home'),
    url(r'^private/$', 'pinry.core.views.private', name='private'),
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'core/login.html'}, name='login'),
    url(r'^login/renren/$','pinry.renren_oauth.views.renren_login',name='renren_login'),
    url(r'^login/weibo/$','pinry.weibo_oauth.views.weibo_login'),
    url(r'^login/weibo/confirm','pinry.weibo_oauth.views.register'),
    url(r'^register/$', 'pinry.core.views.register', name='register'),
    url(r'^logout/$', 'pinry.core.views.logout_user', name='logout'),
)
