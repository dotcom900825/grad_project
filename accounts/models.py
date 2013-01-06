from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile
from pinry.renren_oauth.models import Profile

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
    snsName = models.CharField(_('sns_name'),
                               max_length=100,
                               help_text=_('renren or weibo account name'))
    socialImageUrl =  models.CharField(_('sns_img_url'),
                               max_length=300,
                               help_text=_('renren or weibo image url'))