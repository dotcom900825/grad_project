# -*- Encoding: utf-8 -*-

from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from .forms import PinForm,WishItemForm
from .models import Pin
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from userena.contrib.umessages.models import Message

def recent_pins(request):
    return TemplateResponse(request, 'pins/recent_pins.html', None)


def new_pin(request):
    if request.method == 'POST':
        form = PinForm(request.POST, request.FILES)
        if form.is_valid():
            pin = form.save(commit=False)
            pin.submitter = request.user.get_profile()
            pin.category = 1
            pin.save()
            form.save_m2m()
            messages.success(request, 'New pin successfully added.')
            return HttpResponseRedirect(reverse('pins:recent-pins'))
        else:
            messages.error(request, 'Pin did not pass validation!')
    else:
        form = PinForm()
    context = {
        'form': form,
    }
    return TemplateResponse(request, 'pins/new_pin.html', context)

def new_wish(request):
    if request.method == 'POST':
        form = WishItemForm(request.POST, request.FILES)
        if form.is_valid():
            pin = form.save(commit=False)
            pin.submitter = request.user.get_profile()
            pin.category = 2
            pin.price = 0
            pin.save()
            form.save_m2m()
            messages.success(request, 'New Wish successfully added.')
            return HttpResponseRedirect(reverse('pins:recent-pins'))
        else:
            messages.error(request, 'Pin did not pass validation!')
    else:
        form = WishItemForm()
    context = {
        'form': form,
    }
    return TemplateResponse(request, 'pins/new_wish.html', context)


def delete_pin(request, pin_id):
    try:
        pin = Pin.objects.get(id=pin_id)
        if pin.submitter == request.user:
            pin.delete()
            messages.success(request, 'Pin successfully deleted.')
        else:
            messages.error(request, 'You are not the submitter and can not '
                                    'delete this pin.')
    except Pin.DoesNotExist:
        messages.error(request, 'Pin with the given id does not exist.')
        

    return HttpResponseRedirect(reverse('pins:recent-pins'))

def pin_detail(request, pin_id):
    try:
        pin = Pin.objects.get(id=pin_id)
        comments = Message.objects.filter(pin=pin)
        size_of_comment = len(comments)
        submitter = pin.submitter
        media_root = settings.MEDIA_ROOT
        return render_to_response('pins/detail.html',locals(),context_instance=RequestContext(request))
    except Pin.DoesNotExist:
         messages.error(request, 'Pin with the given id does not exist.')
    return HttpResponseRedirect(reverse('pins:recent-pins'))