# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from weibo import APIClient
from django.shortcuts import render_to_response
from django.conf import settings
from accounts.models import MyProfile
from userena.models import UserenaSignup
from userena import settings as userena_settings
from django.contrib.auth import authenticate,login
def weibo_login(request):
	client = APIClient(app_key=settings.WEIBO_APP_KEY, app_secret=settings.WEIBO_APP_SECRET, redirect_uri=settings.WEIBO_REDIRECT)
	url = client.get_authorize_url()
	return HttpResponseRedirect(url)

def register(request):
	if 'code' in request.GET:
		code = request.GET.get('code')
		client = APIClient(app_key=settings.WEIBO_APP_KEY, app_secret=settings.WEIBO_APP_SECRET, redirect_uri=settings.WEIBO_REDIRECT)
		r = client.request_access_token(code)
		access_token = r.access_token
		expires_in = r.expires_in
		uid = r.uid
		client.set_access_token(access_token,expires_in)
		user = client.users.show.get(uid=uid)
		username = user.name
		avatar = user.profile_image_url
		if UserenaSignup.objects.filter(user__username__iexact=username):
			pass
        	else:
            		new_user = UserenaSignup.objects.create_user(username,
                                                     username,
                                                     '',
                                                     uid,
                                                     not userena_settings.USERENA_ACTIVATION_REQUIRED,
                                                     userena_settings.USERENA_ACTIVATION_REQUIRED)

		        myProfile = MyProfile.objects.get(user=new_user)
            		myProfile.socialImageUrl = avatar
            		myProfile.save()
        	user = authenticate(username=username, password=uid)
      		login(request, user)
        	return HttpResponseRedirect('/')
		