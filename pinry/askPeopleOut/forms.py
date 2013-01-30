# -*- Encoding: utf-8 -*-

from django import forms

from taggit.forms import TagField

from .models import OutActivity


class ActivityForm(forms.ModelForm):
    image = forms.ImageField(label='上传照片'.decode('utf-8'), required=False)
    tags = TagField()
    #description = forms.TextField(label='miaoshu',required=True)

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = (
            'description',
            'image',
            'location',
            'tags',
        )


    def check_if_image(self, data):
        # Test file type
        image_file_types = ['png', 'gif', 'jpeg', 'jpg']
        file_type = data.split('.')[-1]
        if file_type.lower() not in image_file_types:
            raise forms.ValidationError("Requested URL is not an image file. "
                                        "Only images are currently supported.")

    def clean(self):
        cleaned_data = super(ActivityForm, self).clean()

        try:
             image = cleaned_data.get('image')
        except:
             pass
       

       
        return cleaned_data

    class Meta:
        model = OutActivity
        exclude = ['submitter', 'thumbnail']

