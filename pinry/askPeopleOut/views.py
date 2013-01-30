# -*- Encoding: utf-8 -*-

from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from .forms import ActivityForm
from .models import OutActivity
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext


def recent_activity(request):
    return TemplateResponse(request, 'activity/recent_activities.html', None)


def new_activity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST, request.FILES)
        if form.is_valid():
            pin = form.save(commit=False)
            pin.submitter = request.user.get_profile()
            pin.save()
            form.save_m2m()
            messages.success(request, 'New activity successfully added.')
            return HttpResponseRedirect(reverse('pins:recent-pins'))
        else:
            messages.error(request, 'Activity did not pass validation!')
    else:
        form = ActivityForm()
    context = {
        'form': form,
    }
    return TemplateResponse(request, 'activity/new_activity.html', context)



def delete_activity(request, activity_id):
    try:
        activity = OutActivity.objects.get(id=activity_id)
        if activity.submitter == request.user:
            activity.delete()
            messages.success(request, 'Activity successfully deleted.')
        else:
            messages.error(request, 'You are not the submitter and can not '
                                    'delete this Activity.')
    except Pin.DoesNotExist:
        messages.error(request, 'Activity with the given id does not exist.')
        

    return HttpResponseRedirect(reverse('activities:recent-activities'))

