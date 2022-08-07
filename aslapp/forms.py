from django import forms 
from .models import *
# class ImageForm(forms.ModelForm): 

#         class Meta:
#             model  = Image
#             fields=['name','image']           
class GetImage(forms.Form):
    image_path = forms.ImageField()
