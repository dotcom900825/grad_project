from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile
from pinry.renren_oauth.models import Profile
from django.conf import settings
class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')
  
    renren = models.OneToOneField(Profile,
    							  unique=True,
    							  verbose_name='renren_profile',
    							  related_name='renren_profile',
    							  blank=True,
    							  null=True
    	)
    university = models.CharField(_('university_name'),
                               max_length=100,
                               choices=settings.UNIVERSITY_LIST,
                               help_text=_('university')
                               )

    school = models.CharField(_('school_name'),
                               max_length=100,
                               choices=settings.SCHOOL_LIST,
                               help_text=_('school')
                               )
    year_of_study =  models.CharField(_('year_of_study'),
                               max_length=100,
                               choices=settings.YEAR_IN_SCHOOL_CHOICES,
                               help_text=_('year of study')
                               )

    snsName = models.CharField(_('sns_name'),
                               max_length=100,
                               help_text=_('renren or weibo account name'),
                               blank=True,
                               null=True)
    socialImageUrl =  models.CharField(_('sns_img_url'),
                               max_length=300,
                               help_text=_('renren or weibo image url'),
                               blank=True,
                               null=True)