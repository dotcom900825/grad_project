# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from weibo import APIClient
from django.shortcuts import render_to_response
from django.conf import settings
from accounts.models import MyProfile
from userena.models import UserenaSignup
from userena import settings as userena_settings

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
		client.set_access_token(access_token,expires_in)
		username = client.users.name
		uid = client.users.id
		avatar = client.users.profile_img_url
		if UserenaSignup.objects.filter(user__username__iexact=uid):
			pass
        else:
            new_user = UserenaSignup.objects.create_user(uid,
                                                     username,
                                                     '',
                                                     access_token,
                                                     not userena_settings.USERENA_ACTIVATION_REQUIRED,
                                                     userena_settings.USERENA_ACTIVATION_REQUIRED)

     #   user.set_password(access_token)
     #   user.save()

            #profile, profile_created = Profile.objects.get_or_create(user=new_user, name=name, avatar=avatar)
            #profile.access_token = access_token
            #profile.save()

            myProfile = MyProfile.objects.get(user=new_user)
            myProfile.socialImageUrl = avatar
            myProfile.save()
        # Authenticate the user and log them in using Django's pre-built
        # functions for these things.
        user = authenticate(username=uid, password=access_token)
        login(request, user)
        return HttpResponseRedirect('/')