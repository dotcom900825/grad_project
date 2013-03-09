# -*- Encoding: utf-8 -*-

from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from userena.models import UserenaSignup
from guardian.decorators import permission_required_or_403
from userena.decorators import secure_required
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from ajaxuploader.views import AjaxFileUploader
from django.middleware.csrf import get_token
from django.conf  import settings 
from PIL import Image  

from pinry.pins.models import Pin

def user_pins(request,username):
	detail_user = User.objects.get(username = username)
	return render_to_response('accounts/user_pins.html',locals(),context_instance=RequestContext(request))

@secure_required
@permission_required_or_403('change_user', (User, 'username', 'username'))
def upload_pic(request,username):
	if UserenaSignup.objects.filter(user__username__iexact=username):
		if request.method == 'POST':
			try:
				pic_name = request.POST['img_name']
				x1 = float(request.POST['x1'])
				y1 = float(request.POST['y1'])
				x2 = float(request.POST['x2'])
				y2 = float(request.POST['y2'])
				w = int(request.POST['w'])
				h = int(request.POST['h'])
				

			except:
				HttpResponse('param error')
			abs_path_big = "%s/%s/" % (settings.MEDIA_ROOT,settings.USER_BIG_PIC_URL)
			abs_path_crop ="%s/%s/" % (settings.MEDIA_ROOT,settings.USER_CROP_PIC_URL)
			try:
				img = Image.open(abs_path_big + pic_name)
			except IOError:
					HttpResponse('io error')
			ratio = img.size[0]/200.0
			img = img.transform((int(w*ratio),int(h*ratio)),Image.EXTENT,(x1*ratio,y1*ratio,x2*ratio,y2*ratio))
			
			img.thumbnail((100,100))
			file_name = "%s_%s" % (pic_name,"_100_100.jpg")
			img.save("%s%s"%(abs_path_crop,file_name),"JPEG")
			profile = User.objects.get(username=username).get_profile()
			profile.socialBigImageUrl = '/media/' + settings.USER_BIG_PIC_URL + '/' + pic_name
			profile.socialImageUrl = '/media/' + settings.USER_CROP_PIC_URL + '/' + file_name
			profile.save()
			return HttpResponseRedirect('/')	
	
	csrf_token = get_token(request)
	return render_to_response('accounts/upload_pic.html',
		        {'csrf_token': csrf_token,'username' : username, 'default_pic_url' : settings.DEFAULT_USER_PIC_URL,}, context_instance = RequestContext(request))


import_uploader = AjaxFileUploader()
          