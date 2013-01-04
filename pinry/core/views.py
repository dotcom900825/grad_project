from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    return HttpResponseRedirect(reverse('pins:recent-pins'))

def about_us(request):
    return render_to_response('core/about_us.html',locals(),context_instance = RequestContext(request))

def private(request):
    return TemplateResponse(request, 'core/private.html', None)


def register(request):
    if not settings.ALLOW_NEW_REGISTRATIONS:
        messages.error(request, "The admin of this service is not "
                                "allowing new registrations.")
        return HttpResponseRedirect(reverse('pins:recent-pins'))
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for registering, you can now '
                                      'login.')
            return HttpResponseRedirect(reverse('core:login'))
    else:
        form = UserCreationForm()

    return TemplateResponse(request, 'core/register.html', {'form': form})


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return HttpResponseRedirect(reverse('core:home'))
