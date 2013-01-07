# -*- Encoding: utf-8 -*-

from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages

def user_pins(request, username):
    return TemplateResponse(request, 'accounts/user_pins.html', None)

