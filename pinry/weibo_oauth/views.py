# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from weibo import APIClient
from django.shortcuts import render_to_response
from django.conf import settings
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
		return HttpResponse(client.statuses.user_timeline.get())		