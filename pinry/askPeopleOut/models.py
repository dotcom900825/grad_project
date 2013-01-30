# -*- Encoding: utf-8 -*-
from django.db import models
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from accounts.models import MyProfile
from django.utils.translation import ugettext as _
from taggit.managers import TaggableManager
import urllib2
import os
from PIL import Image


class OutActivity(models.Model):
    submitter = models.ForeignKey(MyProfile)
    description = models.TextField(_('活动内容'.decode('utf-8')),blank=True,null=True)
    image = models.ImageField(upload_to='pins/pin/originals/',blank=True,null=True)
    thumbnail = models.ImageField(upload_to='pins/pin/thumbnails/',blank=True,null=True)
    published = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()
    location = models.TextField(_('活动地址'.decode('utf-8')),blank=True,null=True)  
  

    def __unicode__(self):
        return str(self.description)


    def save(self, *args, **kwargs):
        hash_name = os.urandom(32).encode('hex')

        if not self.thumbnail:
            if not self.image:
                pass
            else:
                super(OutActivity, self).save()
                image = Image.open(self.image.path)
                size = image.size
                prop = 200.0 / float(image.size[0])
                size = (int(prop*float(image.size[0])), int(prop*float(image.size[1])))
                image.thumbnail(size, Image.ANTIALIAS)
                temp_thumb = NamedTemporaryFile()
                if image.mode != "RGB":
                    image = image.convert("RGB")
                image.save(temp_thumb.name, 'JPEG')
                self.thumbnail.save(''.join([hash_name, '.jpg']), File(temp_thumb))

        super(OutActivity, self).save(*args, **kwargs)


    class Meta:
        ordering = ['-id']
